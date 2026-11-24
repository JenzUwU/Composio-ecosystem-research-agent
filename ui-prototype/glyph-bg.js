/* =========================================================
   Glyph background — vanilla port of the React <GlyphBackground>
   (backgrounds-glyph.tsx). Same WebGL shader; the React/motion
   pieces are replaced with plain JS:
     motion animate()/motionValue  -> wave age computed from the clock
     useInView / usePageVisible    -> margin check + visibilitychange
     useShouldReduceMotion         -> removed (always animates)
   Mounted as a fixed full-viewport layer BEHIND the page. Content
   panels are opaque, so glyphs only show in the empty margins
   around the 1440px layout. Clicking a margin sends a blue wave.
   ========================================================= */
(function () {
  "use strict";

  const CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  const MAX_WAVES = 12, TRAIL = 12, TRAIL_LIFE = 700;
  const WAVE_LIFE = 4, WAVE_GAP = 0.3, WAVE_SPEED = 560, WAVE_SLOWDOWN = 0.66;
  const WAVE_EDGE = 10, WAVE_TAIL = 30;
  const DRIFT = [-30, 12], ACTIVITY_DECAY = 900;

  // Look — tuned for the Monochrome Signal palette
  const OPTIONS = {
    color: "#171717",   // glyph ink
    accent: "#0000DD",  // wave rings
    fontSize: 10,
    rest: 0.035,        // baseline ink everywhere
    haze: 0.32,         // ink inside drifting noise clouds
    hoverInk: 0.45,     // ink under the pointer trail
    layoutMax: 1440,    // matches --max in styles.css
  };

  const VERTEX = `
attribute vec2 position;
void main() { gl_Position = vec4(position, 0.0, 1.0); }`;

  const FRAGMENT = `
precision highp float;
uniform sampler2D atlas;
uniform vec2 size;
uniform vec2 cell;
uniform float dpr;
uniform float count;
uniform float time;
uniform float rest;
uniform float haze;
uniform float hoverInk;
uniform float activity;
uniform vec2 drift;
uniform vec3 color;
uniform vec3 accent;
uniform vec4 waves[${MAX_WAVES * 2}];
uniform vec4 trail[${TRAIL}];

float hash(vec2 p) { return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
float smoothNoise(vec2 p) {
  vec2 i = floor(p); vec2 f = fract(p); vec2 u = f * f * (3.0 - 2.0 * f);
  return mix(mix(hash(i), hash(i + vec2(1.0, 0.0)), u.x), mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x), u.y);
}
float outline(float kind, float angle, float phase) {
  if (kind < 0.5) return 1.0;
  if (kind < 1.5) {
    float s = sin(angle); float c = cos(angle);
    return (2.0 - 2.0 * s + s * sqrt(abs(c)) / (s + 1.4)) * 0.42;
  }
  return 1.0 + 0.14 * sin(3.0 * angle + phase) + 0.08 * sin(5.0 * angle - phase * 1.3);
}
void main() {
  vec2 pixel = vec2(gl_FragCoord.x, size.y - gl_FragCoord.y);
  vec2 index = floor(pixel / cell);
  vec2 point = (index + 0.5) * cell / dpr;

  float ring = 0.0;
  for (int i = 0; i < ${MAX_WAVES}; i++) {
    vec4 a = waves[i * 2]; vec4 b = waves[i * 2 + 1];
    if (a.w <= 0.0) continue;
    vec2 v = point - a.xy;
    float angle = atan(-v.y, v.x);
    float shape = mix(1.0, outline(b.x, angle, b.z), b.y);
    shape *= 1.0 + 0.07 * sin(3.0 * angle + b.z + b.w) + 0.05 * sin(5.0 * angle - b.z * 1.7 - b.w * 1.3) + 0.03 * sin(9.0 * angle + b.w * 2.1);
    float d = length(v) - a.z * shape;
    float k = d > 0.0 ? d / ${WAVE_EDGE.toFixed(1)} : d / ${WAVE_TAIL.toFixed(1)};
    ring = max(ring, exp(-k * k) * a.w);
  }

  float hover = 0.0;
  for (int i = 0; i < ${TRAIL}; i++) {
    vec4 t = trail[i];
    if (t.w <= 0.0) continue;
    vec2 v = point - t.xy;
    hover += t.w * exp(-dot(v, v) / (2.0 * t.z * t.z));
  }
  hover = min(hover, 1.0);

  mat2 turn = mat2(0.82, 0.57, -0.57, 0.82);
  vec2 q = turn * (point - drift);
  float blob = smoothNoise(vec2(q.x / 140.0, q.y / 80.0) + vec2(time * 0.04, 0.0)) * 0.62
    + smoothNoise(vec2(q.x / 62.0, q.y / 36.0) + vec2(3.7, time * 0.06)) * 0.38;
  float grain = smoothNoise(vec2(q.x / 30.0, q.y / 14.0) + vec2(time * 0.2, 7.3));
  float cloud = blob * (0.82 + 0.24 * grain);
  float mask = pow(smoothstep(0.47 - 0.2 * activity, 0.84, cloud), 2.6);

  float seed = hash(index);
  float epoch = floor(time * 0.08 * (0.4 + seed) + seed * 97.0);
  float character = floor(hash(index + epoch * 0.137) * count);
  vec2 local = fract(pixel / cell);
  float ink = pow(texture2D(atlas, vec2((character + local.x) / count, local.y)).a, 1.7);

  float grey = ink * clamp(rest + haze * mask * (1.0 + 0.3 * activity) + hoverInk * hover * (0.6 + 0.4 * mask), 0.0, 1.0);
  float blue = ink * ring * 0.72;
  float alpha = grey + blue - grey * blue;
  vec3 tint = color * grey * (1.0 - blue) + accent * blue;
  gl_FragColor = vec4(tint, alpha);
}`;

  const reduceMq = { matches: false }; // reduced-motion gating removed on request: always animate

  const canvas = document.createElement("canvas");
  canvas.className = "glyph-bg";
  canvas.setAttribute("aria-hidden", "true");
  document.body.prepend(canvas);

  const gl = canvas.getContext("webgl", { premultipliedAlpha: true, preserveDrawingBuffer: true, antialias: false });
  if (!gl) { canvas.remove(); return; }

  function compile(type, src) {
    const s = gl.createShader(type);
    if (!s) return null;
    gl.shaderSource(s, src); gl.compileShader(s);
    return gl.getShaderParameter(s, gl.COMPILE_STATUS) ? s : null;
  }
  const vs = compile(gl.VERTEX_SHADER, VERTEX), fs = compile(gl.FRAGMENT_SHADER, FRAGMENT);
  const program = gl.createProgram();
  if (!vs || !fs || !program) { canvas.remove(); return; }
  gl.attachShader(program, vs); gl.attachShader(program, fs); gl.linkProgram(program);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) { canvas.remove(); return; }
  gl.useProgram(program);

  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  const pos = gl.getAttribLocation(program, "position");
  gl.enableVertexAttribArray(pos);
  gl.vertexAttribPointer(pos, 2, gl.FLOAT, false, 0, 0);

  const texture = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_2D, texture);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
  gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);

  const U = {};
  ["atlas", "size", "cell", "dpr", "count", "time", "rest", "haze", "hoverInk", "activity", "drift", "color", "accent", "waves", "trail"]
    .forEach((n) => (U[n] = gl.getUniformLocation(program, n)));
  gl.uniform1i(U.atlas, 0);
  gl.uniform1f(U.count, CHARACTERS.length);
  gl.uniform1f(U.rest, OPTIONS.rest);
  gl.uniform1f(U.haze, OPTIONS.haze);
  gl.uniform1f(U.hoverInk, OPTIONS.hoverInk);

  function toRgb(c) {
    const p = document.createElement("canvas").getContext("2d");
    p.fillStyle = c; p.fillRect(0, 0, 1, 1);
    const d = p.getImageData(0, 0, 1, 1).data;
    return [d[0] / 255, d[1] / 255, d[2] / 255];
  }
  gl.uniform3f(U.color, ...toRgb(OPTIONS.color));
  gl.uniform3f(U.accent, ...toRgb(OPTIONS.accent));

  let width = 0, height = 0, dpr = 1, cell = [7, 13];
  let time = 0, last = 0, running = false;
  let waves = [], trail = [], activity = { value: 0, at: 0 };
  const waveBuf = new Float32Array(MAX_WAVES * 8);
  const trailBuf = new Float32Array(TRAIL * 4);

  // Only worth animating when the viewport is wider than the layout.
  const marginsVisible = () => window.innerWidth > OPTIONS.layoutMax + 24;
  const shouldPlay = () => !document.hidden && !reduceMq.matches && marginsVisible();

  function resize() {
    width = window.innerWidth; height = window.innerHeight;
    dpr = Math.max(1, Math.min(window.devicePixelRatio || 1, 2));
    canvas.width = Math.max(1, Math.round(width * dpr));
    canvas.height = Math.max(1, Math.round(height * dpr));
    const font = `${OPTIONS.fontSize * dpr}px "JetBrains Mono", Menlo, ui-monospace, Consolas, monospace`;
    const m = document.createElement("canvas").getContext("2d");
    m.font = font;
    cell = [Math.round(m.measureText("0").width), Math.round(OPTIONS.fontSize * 1.25 * dpr)];
    const atlas = document.createElement("canvas");
    atlas.width = Math.ceil(cell[0] * CHARACTERS.length); atlas.height = Math.ceil(cell[1]);
    const a = atlas.getContext("2d");
    a.font = font; a.textAlign = "center"; a.textBaseline = "middle"; a.fillStyle = "#fff";
    for (let i = 0; i < CHARACTERS.length; i++) a.fillText(CHARACTERS[i], (i + 0.5) * cell[0], cell[1] / 2);
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, atlas);
  }

  function draw() {
    if (!width || !height) return;
    const sec = time / 1000;
    waveBuf.fill(0);
    waves = waves.filter((w) => sec - w.start - w.delay < WAVE_LIFE);
    waves.forEach((w, i) => {
      const age = sec - w.start - w.delay;
      if (age <= 0) return;
      const radius = (WAVE_SPEED * age) / (1 + WAVE_SLOWDOWN * age);
      const fade = Math.min(1, age / 0.05) * Math.exp(-Math.max(0, age - 0.4) / 1.3) * Math.min(1, (WAVE_LIFE - age) / 0.5);
      waveBuf.set([w.x, w.y, radius, fade * w.strength, w.kind, 0.12 + 0.5 * Math.min(1, age / 2.2), w.phase, age * 3], i * 8);
    });
    trailBuf.fill(0);
    trail.forEach((p, i) => {
      const age = (time - p.t) / TRAIL_LIFE;
      if (age < 0 || age >= 1) return;
      trailBuf.set([p.x, p.y, 40 + 25 * age, 0.3 * (1 - age) * (1 - age)], i * 4);
    });
    const act = activity.value * Math.exp(-Math.max(0, time - activity.at) / ACTIVITY_DECAY);

    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.uniform2f(U.size, canvas.width, canvas.height);
    gl.uniform2f(U.cell, cell[0], cell[1]);
    gl.uniform1f(U.dpr, dpr);
    gl.uniform1f(U.time, sec);
    gl.uniform1f(U.activity, act);
    gl.uniform2f(U.drift, DRIFT[0] * sec, DRIFT[1] * sec);
    gl.uniform4fv(U.waves, waveBuf);
    gl.uniform4fv(U.trail, trailBuf);
    gl.clearColor(0, 0, 0, 0);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }

  function tick(t) {
    if (!shouldPlay()) { running = false; last = 0; return; }
    time += last ? Math.min(t - last, 64) : 16;
    last = t;
    draw();
    requestAnimationFrame(tick);
  }
  function kick() {
    if (running || !shouldPlay()) return;
    running = true; last = 0; requestAnimationFrame(tick);
  }

  // Pointer: trail everywhere (only visible in margins); waves only when the margin itself is clicked.
  // <main> spans the full width, so "margin" = not inside any layout panel.
  const PANELS = ".hero, .sec, .topbar, .foot, .data-banner, .index-panel, .to-top";
  const inMargin = (e) => !(e.target instanceof Element && e.target.closest(PANELS));
  window.addEventListener("pointermove", (e) => {
    if (reduceMq.matches) return;
    const x = e.clientX, y = e.clientY, now = time;
    const lastP = trail[trail.length - 1];
    const dist = lastP ? Math.hypot(x - lastP.x, y - lastP.y) : 0;
    const cur = activity.value * Math.exp(-Math.max(0, now - activity.at) / ACTIVITY_DECAY);
    activity = { value: Math.min(1, cur + dist / 600), at: now };
    if (lastP && dist < 18) return;
    trail = trail.filter((p) => now - p.t < TRAIL_LIFE).slice(1 - TRAIL).concat({ x, y, t: now });
  }, { passive: true });
  window.addEventListener("pointerdown", (e) => {
    if (reduceMq.matches || !inMargin(e)) return;
    const kind = 1 + Math.floor(Math.random() * 2), phase = Math.random() * Math.PI * 2, start = time / 1000;
    [[0, 1], [WAVE_GAP, 0.55]].forEach(([delay, strength]) => {
      waves = waves.slice(1 - MAX_WAVES).concat({ x: e.clientX, y: e.clientY, kind, phase, strength, start, delay });
    });
    kick();
  });
  // Scrolling moves the page past the fixed layer; keep the trail anchored to the viewport.
  window.addEventListener("resize", () => { resize(); draw(); kick(); });
  document.addEventListener("visibilitychange", kick);
  if (reduceMq.addEventListener) reduceMq.addEventListener("change", () => { draw(); kick(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => { resize(); draw(); });

  resize();
  draw();   // first frame
  kick();
})();
