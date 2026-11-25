/* ================= KapiPasta - Python ================= */
const LS = 'pykapi-v1', LST = 'pykapi-teacher-v1';
const DEF = { onboarded: false, name: '', cls: '', stage: 1, theme: 'rpg', mode: null, lang: 'pl', sound: true, unlockAll: false,
  xp: 0, done: {}, stars: {}, badges: {}, streak: { last: '', n: 0 }, today: { d: '', xp: 0 }, combo: 0, bestCombo: 0, codeRuns: 0, sbRuns: 0, drafts: {}, created: 0, lastSeen: 0 };
function lsGet(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }
function lsSet(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { } }
let S = Object.assign({}, DEF, lsGet(LS) || {});
if (!S.mode) S.mode = (window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
const save = () => { S.lastSeen = Date.now(); lsSet(LS, S); };
window.S = S;

function tr(k, p) {
  let s = (UI[S.lang] && UI[S.lang][k] !== undefined) ? UI[S.lang][k] : (UI.pl[k] !== undefined ? UI.pl[k] : k);
  if (p && typeof s === 'string') for (const x in p) s = s.split('{' + x + '}').join(p[x]);
  return s;
}
const pick = a => a[Math.floor(Math.random() * a.length)];
const W = () => WORDS[S.theme][S.lang] || WORDS[S.theme].pl;
const course = () => (window.COURSE[S.lang] && window.COURSE[S.lang].length) ? COURSE[S.lang] : COURSE.pl;
const todayStr = (d = new Date()) => d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
const stageTasks = L => L.tasks.filter(t => t.l <= S.stage);
const slug = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ł/g, 'l').replace(/Ł/g, 'L').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '').slice(0, 24).replace(/_+$/, '');
const fname = (ci, li, L) => `${String(li + 1).padStart(2, '0')}_${slug(L.title)}.py`;
const chName = ch => ch.name[S.theme];

/* ===== progress math ===== */
function lessonProg(L) { const ts = stageTasks(L); const d = ts.filter(t => S.done[t.id] && S.done[t.id].ok).length; return { d, n: ts.length }; }
function chapProg(ch) { let d = 0, n = 0; ch.lessons.forEach(L => { const p = lessonProg(L); d += p.d; n += p.n; }); return { d, n, p: n ? d / n : 0 }; }
function unlocked(ci) { if (ci === 0 || S.unlockAll) return true; return chapProg(course()[ci - 1]).p >= 0.5; }
const LVT = k => 50 * k * (k + 1);
function levelOf(xp) { let l = 0; while (xp >= LVT(l + 1)) l++; return { lv: l + 1, cur: xp - LVT(l), need: LVT(l + 1) - LVT(l) }; }
const lvTitle = lv => W().lv[Math.min(lv - 1, 9)];
function statsOf(st) {
  const C = course(); let okCount = 0, first = 0, codeOk = 0, bugOk = 0;
  const types = {}; C.forEach(ch => ch.lessons.forEach(L => L.tasks.forEach(t => types[t.id] = t.t)));
  for (const id in st.done) { const d = st.done[id]; if (d.ok) { okCount++; if (d.first) first++; if (types[id] === 'code') codeOk++; if (types[id] === 'bug') bugOk++; } }
  const perfect = Object.values(st.stars || {}).filter(x => x >= 3).length;
  return { okCount, first, codeOk, bugOk, perfect, bestCombo: st.bestCombo || 0, streak: (st.streak && st.streak.n) || 0, xp: st.xp || 0, sbRuns: st.sbRuns || 0 };
}

/* ===== sound / fx ===== */
let AC = null;
function beep(type) {
  if (!S.sound) return;
  try {
    AC = AC || new (window.AudioContext || window.webkitAudioContext)();
    const seq = { ok: [[660, .08], [880, .12]], bad: [[220, .15]], lvl: [[523, .1], [659, .1], [784, .1], [1046, .2]], click: [[500, .03]] }[type] || [];
    let t = AC.currentTime;
    seq.forEach(([f, d]) => { const o = AC.createOscillator(), g = AC.createGain(); o.type = type === 'bad' ? 'sawtooth' : 'triangle'; o.frequency.value = f; g.gain.setValueAtTime(.12, t); g.gain.exponentialRampToValueAtTime(.001, t + d); o.connect(g); g.connect(AC.destination); o.start(t); o.stop(t + d); t += d; });
  } catch (e) { }
}
function confetti(n = 60) {
  const cols = ['#ff6b6b', '#ffd93d', '#6bcB77', '#4d96ff', '#c77dff', '#ff9f43'];
  for (let i = 0; i < n; i++) {
    const c = document.createElement('div'); c.className = 'confetti';
    c.style.left = Math.random() * 100 + 'vw'; c.style.background = pick(cols);
    c.style.animationDuration = (1.6 + Math.random() * 1.6) + 's'; c.style.animationDelay = Math.random() * .4 + 's';
    document.body.appendChild(c); setTimeout(() => c.remove(), 3600);
  }
}
function toast(html, ms = 2600) {
  let box = document.querySelector('.toasts'); if (!box) { box = document.createElement('div'); box.className = 'toasts'; document.body.appendChild(box); }
  const t = document.createElement('div'); t.className = 'toast'; t.innerHTML = html; box.appendChild(t); setTimeout(() => t.remove(), ms);
}
function kapiSay(msg, mood = 'happy') {
  KAPI = { msg, mood };
  const p = document.getElementById('kp');
  if (p && p.offsetParent !== null) { p.innerHTML = kapiInner(); }
  else toast(`${capy({ size: 44, mood })}<span>${msg}</span>`, 3000);
}
let KAPI = null;
function kapiInner() {
  const k = KAPI || { msg: `<b>${tr('kapiSays')}</b><br>${pick(tr('tips'))}`, mood: 'happy' };
  return `<div class="bubble">${k.msg}</div><div class="kp-capy">${capy({ size: 170, mood: k.mood })}</div>`;
}

/* ===== XP / rewards ===== */
const BASE = { quiz: 10, fill: 15, bug: 15, code: 25 };
function touchStreak() {
  const td = todayStr(); if (S.streak.last === td) return;
  const y = new Date(); y.setDate(y.getDate() - 1);
  S.streak.n = (S.streak.last === todayStr(y)) ? S.streak.n + 1 : 1; S.streak.last = td;
}
function addXP(n) {
  const before = levelOf(S.xp).lv; S.xp += n;
  const td = todayStr(); if (S.today.d !== td) S.today = { d: td, xp: 0 };
  const wasGoal = S.today.xp >= 50; S.today.xp += n; touchStreak();
  const after = levelOf(S.xp).lv;
  if (after > before) setTimeout(() => { beep('lvl'); confetti(90); modal(`<div class="mb" style="text-align:center">${capy({ size: 170, mood: 'wow' })}<h2>🎉 ${tr('levelUp')}</h2><h1>${tr('level')} ${after} – ${lvTitle(after)}</h1></div><div class="mf"><button class="btn pri" data-act="close">${tr('ok')}</button></div>`); }, 700);
  if (!wasGoal && S.today.xp >= 50) setTimeout(() => toast('🎯 ' + tr('dailyDone')), 1200);
}
function checkBadges() {
  const st = statsOf(S);
  const all = BADGES.map(b => ({ id: b.id, ico: b.ico, name: b[S.lang][0], ok: b.f(st) }));
  course().forEach(ch => { const p = chapProg(ch); all.push({ id: 'ch_' + ch.id, ico: ch.icon[S.theme], name: chName(ch), ok: p.n > 0 && p.d === p.n }); });
  all.forEach(b => { if (b.ok && !S.badges[b.id]) { S.badges[b.id] = Date.now(); setTimeout(() => { beep('lvl'); toast(`<span style="font-size:26px">${b.ico}</span><span>${tr('newBadge')}<br>${b.name}</span>`, 3500); }, 900); } });
}
function award(t, extra = {}) {
  const prev = S.done[t.id] || { tries: 0 };
  if (prev.ok) { return 0; }
  const first = (prev.tries || 0) === 0 && !prev.revealed;
  let xp = BASE[t.t] + (t.l - 1) * 5 + (first ? 5 : 0);
  if (prev.revealed || extra.self) xp = Math.round(xp / 2);
  S.done[t.id] = { ok: 1, first: first ? 1 : 0, tries: (prev.tries || 0) + 1, ts: Date.now() };
  if (first) { S.combo++; S.bestCombo = Math.max(S.bestCombo, S.combo); } else S.combo = 0;
  addXP(xp);
  if (first && S.combo > 0 && S.combo % 5 === 0) { addXP(10); setTimeout(() => toast('🔥 ' + tr('combo', { n: S.combo, xp: 10 })), 500); }
  checkBadges(); save(); beep('ok');
  return xp;
}
function fail(t) { const d = S.done[t.id] || { tries: 0 }; if (!d.ok) { d.tries = (d.tries || 0) + 1; S.done[t.id] = d; } S.combo = 0; save(); beep('bad'); }
function reveal(t) { const d = S.done[t.id] || { tries: 0 }; if (!d.ok) { d.revealed = 1; S.done[t.id] = d; save(); } }

/* ===== syntax highlight ===== */
const KW = new Set('False None True and as break continue def del elif else except finally for from global if import in is lambda not or pass return try while with yield nonlocal'.split(' '));
const BI = new Set('print input int float str bool len range list dict set tuple type sum min max abs round sorted open enumerate chr ord reversed zip map filter isinstance'.split(' '));
function hl(code) {
  const re = /(#[^\n]*)|((?:[fFrR]{1,2})?(?:"""[\s\S]*?"""|'''[\s\S]*?'''|"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*'))|(\b\d+(?:\.\d+)?\b)|([A-Za-z_À-ſ][\wÀ-ſ]*)(\s*\()?/g;
  let out = '', last = 0, m;
  while ((m = re.exec(code))) {
    out += esc(code.slice(last, m.index)); last = re.lastIndex;
    if (m[1]) out += `<span class="c">${esc(m[1])}</span>`;
    else if (m[2]) out += `<span class="s">${esc(m[2])}</span>`;
    else if (m[3]) out += `<span class="n">${m[3]}</span>`;
    else if (m[4]) { const w = m[4]; const cls = KW.has(w) ? 'k' : BI.has(w) ? 'b' : m[5] ? 'f' : ''; out += (cls ? `<span class="${cls}">${esc(w)}</span>` : esc(w)) + (m[5] ? esc(m[5]) : ''); }
  }
  return out + esc(code.slice(last));
}
function codeBlock(code, o = {}) {
  const lines = code.split('\n'); const hlines = hl(code).split('\n');
  const gut = lines.map((_, i) => `<div>${i === 0 && o.run ? `<span class="rg" data-act="${o.run}" data-a="${o.runArg || ''}" title="Run">▶</span>` : ''}${i + 1}</div>`).join('');
  const body = hlines.map((h, i) => `<div class="ln" data-ln="${i}">${h || ' '}</div>`).join('');
  return `<div class="code ${o.cls || ''}">${o.head !== false ? `<div class="code-head">🐍 <span>${esc(o.title || 'main.py')}</span><span class="sp"></span>${o.right || ''}</div>` : ''}<div class="code-body"><div class="gutter">${gut}</div><div class="lines">${body}</div></div></div>`;
}
function runWin(title, r, cmdline) {
  let h = `<span class="cmd">${esc(cmdline || '$ python ' + title)}</span>\n`;
  if (r.loading) h += `<span class="cmd">${tr('running')}</span>`;
  else {
    h += esc(r.disp !== undefined ? r.disp : (r.out || ''));
    if (r.err) {
      h += `<span class="err">Traceback (most recent call last):\n${r.line ? `  File "${title}", line ${r.line}\n` : ''}${esc(r.err)}</span>\n`;
      const hk = 'hint_' + r.etype; const hint = tr(hk);
      if (hint !== hk) h += `<div class="errhint"><i class="cpy"></i> ${hint}</div>`;
      h += `\n<span class="fin">Process finished with exit code 1</span>`;
    } else h += `\n<span class="fin">Process finished with exit code 0</span>`;
  }
  return `<div class="runwin"><div class="rh">▶ Run: <b>${esc(title)}</b></div><pre>${h}</pre></div>`;
}

/* ===== Python (Pyodide) ===== */
const PYO = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/';
const Py = {
  state: 'idle', mode: null, worker: null, main: null, pending: {}, seq: 0, ready: null,
  init() {
    if (this.state === 'ready' || this.state === 'loading') return this.ready;
    this.state = 'loading'; pyBadge();
    this.ready = new Promise((res, rej) => { this._res = res; this._rej = rej; }); this.ready.catch(() => { });
    this.startWorker(); return this.ready;
  },
  startWorker() {
    try {
      const src = `self.RUNNER=${JSON.stringify(window.RUNNER)};importScripts("${PYO}pyodide.js");let py;const R=(async()=>{py=await loadPyodide({indexURL:"${PYO}"});py.runPython(self.RUNNER);postMessage({t:'ready'})})().catch(e=>postMessage({t:'fail',m:String(e)}));onmessage=async e=>{await R;const d=e.data;try{const f=py.globals.get('_run_json');const r=f(d.code,d.stdin||'',d.setup||'',d.check||'');f.destroy();postMessage({t:'res',id:d.id,r:JSON.parse(r)})}catch(err){postMessage({t:'res',id:d.id,r:{err:String(err),etype:'InternalError',out:'',disp:''}})}};`;
      const w = new Worker(URL.createObjectURL(new Blob([src], { type: 'text/javascript' })));
      this.worker = w;
      const giveUp = setTimeout(() => { if (this.state !== 'ready') { try { w.terminate(); } catch (e) { } this.worker = null; this.startMain(); } }, 45000);
      w.onmessage = e => {
        const m = e.data;
        if (m.t === 'ready') { clearTimeout(giveUp); this.mode = 'worker'; this.state = 'ready'; this._res(); pyBadge(); }
        else if (m.t === 'fail') { clearTimeout(giveUp); w.terminate(); this.worker = null; this.startMain(); }
        else if (m.t === 'res') { const p = this.pending[m.id]; if (p) { clearTimeout(p.to); delete this.pending[m.id]; p.res(m.r); } }
      };
      w.onerror = () => { if (this.state !== 'ready') { clearTimeout(giveUp); try { w.terminate(); } catch (e) { } this.worker = null; this.startMain(); } };
    } catch (e) { this.startMain(); }
  },
  startMain() {
    if (this.mainTried) return this.fail(); this.mainTried = true;
    const go = async () => { try { this.main = await loadPyodide({ indexURL: PYO }); this.main.runPython(window.RUNNER); this.mode = 'main'; this.state = 'ready'; this._res(); pyBadge(); } catch (e) { this.fail(e); } };
    if (window.loadPyodide) return go();
    const s = document.createElement('script'); s.src = PYO + 'pyodide.js'; s.onload = go; s.onerror = () => this.fail('script'); document.head.appendChild(s);
    setTimeout(() => { if (this.state === 'loading') this.fail('timeout'); }, 60000);
  },
  fail(e) { if (this.state === 'fail') return; this.state = 'fail'; if (this._rej) this._rej(e); pyBadge(); const ct = curTask(); if (V.view === 'sandbox' || (V.view === 'lesson' && V.phase === 'tasks' && ct && ct.t === 'code')) renderMain(); },
  async run(code, stdin = '', setup = '', check = '') {
    await this.init();
    S.codeRuns++; save();
    if (this.mode === 'main') { const f = this.main.globals.get('_run_json'); const r = f(code, stdin, setup, check); f.destroy(); return JSON.parse(r); }
    return new Promise(res => {
      const id = ++this.seq;
      const to = setTimeout(() => { delete this.pending[id]; try { this.worker.terminate(); } catch (e) { } this.worker = null; this.state = 'idle'; this.init(); res({ err: 'TimeoutError: ' + tr('timeout'), etype: 'TimeoutError', out: '', disp: '' }); }, 20000);
      this.pending[id] = { res, to }; this.worker.postMessage({ id, code, stdin, setup, check });
    });
  }
};
function pyBadge() { const e = document.getElementById('pyst'); if (e) e.innerHTML = pyStatus(); }
function pyStatus() {
  const st = Py.state; const cls = st === 'ready' ? 'ok' : st === 'fail' ? 'bad' : st === 'loading' ? 'load' : '';
  const txt = st === 'ready' ? tr('pyReady') : st === 'fail' ? 'Python ✖' : st === 'loading' ? tr('pyLoading') : 'Python 3.12';
  return `<span class="dot ${cls}"></span> 🐍 ${txt}`;
}
const norm = s => (s || '').replace(/\r/g, '').split('\n').map(l => l.replace(/\s+$/, '')).join('\n').replace(/\n+$/, '');

/* ===== view state ===== */
const V = { view: 'welcome', ci: 0, li: 0, phase: 'theory', ti: 0, tabs: [], open: {}, drawer: false, ans: {} };
function openLesson(ci, li, phase = 'theory') {
  V.view = 'lesson'; V.ci = ci; V.li = li; V.phase = phase; V.ti = firstUndone(course()[ci].lessons[li]); V.ans = {};
  const key = ci + ':' + li; if (!V.tabs.includes(key)) V.tabs.push(key); if (V.tabs.length > 6) V.tabs.shift();
  V.open[course()[ci].id] = true; V.drawer = false; Py.init(); render(); scrollTop();
}
function firstUndone(L) { const ts = stageTasks(L); const i = ts.findIndex(t => !(S.done[t.id] && S.done[t.id].ok)); return i < 0 ? 0 : i; }
function go(view) { V.view = view; V.drawer = false; if (view === 'sandbox') Py.init(); render(); scrollTop(); }
const scrollTop = () => { const e = document.querySelector('.editor-scroll'); if (e) e.scrollTop = 0; };

/* ===== render frame ===== */
function render() {
  stopAllScenes();
  document.body.className = `${S.theme} ${S.mode}`;
  document.documentElement.lang = S.lang;
  if (!S.onboarded) { document.getElementById('app').innerHTML = frame(onboardView()); return; }
  document.getElementById('app').innerHTML = frame(mainView());
  afterRender();
}
function renderMain() { stopAllScenes(); const m = document.querySelector('.editor-scroll'); if (!m) return render(); const sc = m.scrollTop; m.innerHTML = mainView(); m.scrollTop = sc; afterRender(); const t = document.querySelector('.tabs'); if (t) t.outerHTML = tabsHtml(); const tr2 = document.getElementById('proj'); if (tr2) tr2.innerHTML = treeHtml(); const sb = document.querySelector('.statusbar'); if (sb) sb.outerHTML = statusHtml(); }
function frame(inner) {
  const lv = levelOf(S.xp); const C = course();
  const projName = V.view === 'lesson' ? chName(C[V.ci]) : 'KapiPasta';
  return `<div id="ide">
<header class="toolbar">
 <button class="tb-btn menu-btn" data-act="drawer" aria-label="menu">☰</button>
 <button class="tb-logo" data-act="go" data-a="welcome"><span class="lg"><i class="cpy big"></i></span><span>KapiPasta - Python</span></button>
 <button class="tb-proj" data-act="go" data-a="welcome">📁 ${esc(projName)} ▾</button>
 <span class="tb-sp"></span>
 ${S.onboarded ? `<button class="tb-btn tb-run" data-act="runcur" title="Run">▶</button>` : ''}
 <div class="seg" role="group" aria-label="language"><button class="${S.lang === 'pl' ? 'on' : ''}" data-act="lang" data-a="pl">PL</button><button class="${S.lang === 'en' ? 'on' : ''}" data-act="lang" data-a="en">EN</button></div>
 <button class="tb-btn" data-act="mode" title="${S.mode === 'dark' ? tr('modeLight') : tr('modeDark')}" aria-label="${S.mode === 'dark' ? tr('modeLight') : tr('modeDark')}">${S.mode === 'dark' ? '☀️' : '🌙'}</button>
 ${S.onboarded ? `<button class="tb-btn" data-act="settings" title="${tr('settings')}">⚙️</button>` : ''}
</header>
<div class="workspace">
 ${S.onboarded ? `<nav class="stripe">
  <button class="${V.view === 'welcome' || V.view === 'lesson' ? 'on' : ''}" data-act="go" data-a="welcome" title="Project">📁</button>
  <button class="${V.view === 'sandbox' ? 'on' : ''}" data-act="go" data-a="sandbox" title="${tr('sandbox')}">🏖️</button>
  <button class="${V.view === 'profile' ? 'on' : ''}" data-act="go" data-a="profile" title="${tr('profile')}">🏅</button>
  <button data-act="progress" title="${tr('progress')}">💾</button>
  <span class="sp"></span>
  <button class="${V.view === 'teacher' ? 'on' : ''}" data-act="go" data-a="teacher" title="${tr('teacher')}">🧑‍🏫</button>
 </nav>
 <aside class="project ${V.drawer ? 'show' : ''}" id="proj">${treeHtml()}</aside>` : ''}
 <div class="main-col">${S.onboarded ? tabsHtml() : ''}<div class="editor-scroll">${inner}</div></div>
 ${S.onboarded ? `<aside class="kapi-panel"><div class="pane-title"><span><i class="cpy"></i> Kapi Assistant</span></div><div class="kp-body" id="kp">${kapiInner()}</div></aside>` : ''}
</div>
${statusHtml()}
<footer>${tr('footer')}</footer>
</div>`;
}
function statusHtml() {
  const lv = levelOf(S.xp);
  return `<div class="statusbar">
 <span class="it" id="pyst">${pyStatus()}</span>
 ${S.onboarded ? `<span class="it">⭐ ${tr('level')} ${lv.lv} · ${esc(lvTitle(lv.lv))}</span>
 <span class="it"><span class="xpbar"><i style="width:${Math.round(lv.cur / lv.need * 100)}%"></i></span> ${S.xp} XP</span>
 <span class="it">🔥 ${S.streak.n}</span>
 <span class="it">🎯 ${tr('daily')} ${Math.min(S.today.d === todayStr() ? S.today.xp : 0, 50)}/50</span>` : ''}
 <span class="it desk-only">UTF-8</span><span class="it desk-only">4 spaces</span>
</div>`;
}
function tabsHtml() {
  const C = course();
  const t = [`<button class="tab ${V.view === 'welcome' ? 'on' : ''}" data-act="go" data-a="welcome">🏠 Welcome</button>`];
  V.tabs.forEach(k => { const [ci, li] = k.split(':').map(Number); const L = C[ci] && C[ci].lessons[li]; if (!L) return; const on = V.view === 'lesson' && V.ci === ci && V.li === li;
    t.push(`<button class="tab ${on ? 'on' : ''}" data-act="lesson" data-a="${k}"><span class="pyfile">🐍</span>${fname(ci, li, L)}<span class="x" data-act="closetab" data-a="${k}">✕</span></button>`); });
  if (V.view === 'sandbox') t.push(`<button class="tab on">🏖️ playground.py</button>`);
  if (V.view === 'profile') t.push(`<button class="tab on">🏅 badges.md</button>`);
  if (V.view === 'teacher') t.push(`<button class="tab on">🧑‍🏫 teacher.py</button>`);
  return `<div class="tabs">${t.join('')}</div>`;
}
function treeHtml() {
  const C = course();
  let h = `<div class="pane-title"><span>Project</span><span class="chip">${tr('st' + S.stage)}</span></div><ul class="tree"><li class="open"><div data-act="go" data-a="welcome"><span class="tw">▶</span>📂 <span class="nm"><b>KapiPasta</b> <span class="muted">~/python</span></span></div><ul>`;
  C.forEach((ch, ci) => {
    const p = chapProg(ch), ul = unlocked(ci), open = V.open[ch.id];
    h += `<li class="${open ? 'open' : ''} ${ul ? '' : 'lock'}"><div data-act="${ul ? 'fold' : 'locked'}" data-a="${ch.id}"><span class="tw">▶</span>${ul ? ch.icon[S.theme] : '🔒'} <span class="nm">${String(ci + 1).padStart(2, '0')}_${esc(chName(ch))}</span><span class="pct">${Math.round(p.p * 100)}%</span></div>`;
    if (open && ul) {
      h += '<ul>';
      ch.lessons.forEach((L, li) => { const lp = lessonProg(L); const st = S.stars[L.id] || 0; const sel = V.view === 'lesson' && V.ci === ci && V.li === li;
        h += `<li><div class="${sel ? 'sel' : ''}" data-act="lesson" data-a="${ci}:${li}"><span class="pyfile">🐍</span><span class="nm">${fname(ci, li, L)}</span>${lp.d === lp.n && lp.n ? `<span class="stars">${'⭐'.repeat(st || 1)}</span>` : `<span class="pct">${lp.d}/${lp.n}</span>`}</div></li>`; });
      h += '</ul>';
    }
    h += '</li>';
  });
  return h + '</ul></li></ul>';
}
function mainView() {
  switch (V.view) {
    case 'lesson': return lessonView();
    case 'sandbox': return sandboxView();
    case 'profile': return profileView();
    case 'teacher': return teacherView();
    default: return welcomeView();
  }
}

/* ===== onboarding ===== */
function onboardView() {
  const st = [1, 2, 3].map(i => `<button class="choice ${S.stage === i ? 'on' : ''}" data-act="setstage" data-a="${i}"><span class="ce">${['🌱', '🚀', '🏆'][i - 1]}</span><b>${tr('st' + i)}</b><small>${tr('st' + i + 'd')}</small></button>`).join('');
  const th = ['rpg', 'space', 'neutral'].map(x => `<button class="choice ${S.theme === x ? 'on' : ''}" data-act="settheme" data-a="${x}"><span class="ce">${{ rpg: '🏰', space: '🚀', neutral: '💻' }[x]}</span><b>${tr('th_' + x)}</b><small>${tr('th_' + x + 'd')}</small></button>`).join('');
  return `<div class="doc"><div class="hero">${capy({ size: 160, mood: 'wow' })}<div><h1>${tr('tagline')}</h1><p>${tr('intro')}</p></div></div>
<div class="readme"><label class="lbl">${tr('yourName')}</label><input class="inp" id="ob-name" maxlength="30" placeholder="${tr('namePh')}" value="${esc(S.name)}">
<label class="lbl">${tr('yourClass')}</label><input class="inp" id="ob-cls" maxlength="12" placeholder="${tr('classPh')}" value="${esc(S.cls)}">
<h3 style="margin-top:16px">${tr('chooseStage')}</h3><div class="choices">${st}</div>
<h3 style="margin-top:16px">${tr('chooseTheme')}</h3><div class="choices">${th}</div>
<div class="row-btns" style="justify-content:space-between;margin-top:18px"><button class="btn ghost" data-act="teacherstart">${tr('teacherLink')}</button><button class="btn pri" data-act="startapp">${tr('start')}</button></div></div></div>`;
}

/* ===== welcome ===== */
function welcomeView() {
  const C = course(), lv = levelOf(S.xp), st = statsOf(S);
  const tx = S.today.d === todayStr() ? S.today.xp : 0;
  const cols = ['#e5534b', '#e0a52b', '#57965c', '#3574f0', '#a855f7', '#20b2aa', '#ff7ac6', '#8b5cf6', '#d9a441'];
  let next = null; C.some((ch, ci) => unlocked(ci) && ch.lessons.some((L, li) => { const p = lessonProg(L); if (p.d < p.n) { next = [ci, li]; return true; } }));
  return `<div class="doc welcome">
<div class="hero">${capy({ size: 130 })}<div style="flex:1"><h1>${tr('hello', { name: esc(S.name || 'Kapi') })}</h1><div class="muted">${tr('kapiSays')} ${pick(tr('tips'))}</div>
${next ? `<div class="row-btns"><button class="btn pri" data-act="lesson" data-a="${next[0]}:${next[1]}">▶ ${esc(C[next[0]].lessons[next[1]].title)}</button></div>` : ''}</div>
<div class="ring" style="--p:${Math.min(100, tx * 2)}"><span>${Math.min(tx, 50)}/50</span></div></div>
<div class="statgrid">
 <div class="stat"><div class="l">⭐ ${tr('level')} ${lv.lv}</div><div class="v">${esc(lvTitle(lv.lv))}</div><div class="xpbar" style="width:100%;margin-top:6px"><i style="width:${Math.round(lv.cur / lv.need * 100)}%"></i></div></div>
 <div class="stat"><div class="l">💎 XP</div><div class="v">${S.xp}</div></div>
 <div class="stat"><div class="l">🔥 ${tr('streak')}</div><div class="v">${S.streak.n}</div></div>
 <div class="stat"><div class="l">🏅 ${tr('badges')}</div><div class="v">${Object.keys(S.badges).length}</div></div>
</div>
<div class="quick">
 <button class="qk" data-act="go" data-a="sandbox"><span class="e">🏖️</span><span><b>${tr('sandbox')}</b><small>${tr('sandboxD')}</small></span></button>
 <button class="qk" data-act="go" data-a="profile"><span class="e">🏅</span><span><b>${tr('profile')}</b><small>${tr('profileD')}</small></span></button>
 <button class="qk" data-act="progress"><span class="e">💾</span><span><b>${tr('progress')}</b><small>${tr('progressD')}</small></span></button>
 <button class="qk" data-act="go" data-a="teacher"><span class="e">🧑‍🏫</span><span><b>${tr('teacher')}</b><small>${tr('teacherD')}</small></span></button>
</div>
<div><h2>📁 ${W().ch}</h2><div class="projlist">${C.map((ch, ci) => { const p = chapProg(ch), ul = unlocked(ci);
  return `<button class="proj ${ul ? '' : 'lk'}" data-act="${ul ? 'opench' : 'locked'}" data-a="${ci}"><span class="pi" style="background:${cols[ci]}">${ul ? ch.icon[S.theme] : '🔒'}</span><span style="flex:1;min-width:0"><span class="pn">${W().ch} ${ci + 1}: ${esc(chName(ch))}</span><br><span class="pp">~/KapiPasta/${String(ci + 1).padStart(2, '0')}_${ch.id} · ${esc(ch.topic)}</span></span><span class="pb"><span class="pbar"><i style="width:${Math.round(p.p * 100)}%"></i></span><small class="muted">${p.d}/${p.n}</small></span></button>`; }).join('')}</div></div></div>`;
}

/* ===== lesson ===== */
function lessonView() {
  const C = course(), ch = C[V.ci], L = ch.lessons[V.li], ts = stageTasks(L), lp = lessonProg(L);
  const head = `<div class="crumb"># ${esc(chName(ch))} › ${fname(V.ci, V.li, L)}</div><h1>${ch.icon[S.theme]} ${W().les} ${V.ci + 1}.${V.li + 1}: ${esc(L.title)}</h1>
<div class="lesson-nav"><button class="${V.phase === 'theory' ? 'on' : ''}" data-act="phase" data-a="theory">📖 ${tr('theory')}</button><button class="${V.phase !== 'theory' ? 'on' : ''}" data-act="phase" data-a="tasks">🧩 ${tr('tasks')} (${lp.d}/${lp.n})</button></div>`;
  if (V.phase === 'theory') {
    const exs = L.ex.filter(e => !e.lvl || e.lvl <= S.stage);
    let h = `<div class="readme">${L.theory}</div>`;
    if (L.more) h += S.stage >= 2 ? `<div class="readme more"><b>${tr('more')}</b>${L.more}</div>` : `<details class="readme more"><summary>${tr('more')}</summary>${L.more}</details>`;
    exs.forEach((ex, i) => {
      const k = L.id + '-ex' + i;
      h += `<h3>🧪 ${tr('example')} ${i + 1}</h3>` + codeBlock(ex.code, { title: `example_${i + 1}.py`, run: 'runex', runArg: i, right: `<button class="btn sm ghost" data-act="tryex" data-a="${i}">✏️</button><button class="btn sm" data-act="runex" data-a="${i}" style="color:#5fb865">▶ Run</button>` });
      if (ex.inp) h += `<div class="muted" style="font-size:12px">⌨️ input: <code>${esc(ex.inp.replace(/\n/g, ' ⏎ '))}</code></div>`;
      h += `<div id="exout-${i}">${V.ans[k] ? runWin(`example_${i + 1}.py`, V.ans[k]) : ''}</div>`;
      h += `<div class="scene-head"><i class="cpy"></i> Kapi Preview</div>` + renderScene(ex.scene, ex);
    });
    h += `<div class="row-btns"><button class="btn pri" data-act="phase" data-a="tasks">${tr('toTasks', { n: ts.length })}</button></div>`;
    return `<div class="doc">${head}${h}</div>`;
  }
  if (V.phase === 'done') return `<div class="doc">${head}${doneView(L)}</div>`;
  if (V.ti >= ts.length || V.ti < 0) V.ti = 0;
  const t = ts[V.ti];
  const dots = ts.map((x, i) => { const d = S.done[x.id]; return `<i class="${d && d.ok ? 'ok' : d && d.tries ? 'fail' : ''} ${i === V.ti ? 'cur' : ''}" data-act="gotask" data-a="${i}" title="${i + 1}"></i>`; }).join('');
  return `<div class="doc">${head}<div class="tprog">${dots}</div>${taskView(t, ts)}</div>`;
}
function typeChip(t) { return `<span class="chip acc">${{ quiz: '❓', fill: '✍️', bug: '🐞', code: '💻' }[t.t]} ${t.t === 'quiz' && t.out ? tr('t_quiz') : t.t === 'quiz' ? tr('t_quizGen') : tr('t_' + t.t)}</span>`; }
function seeded(id) { let h = 2166136261; for (const c of id) { h ^= c.charCodeAt(0); h = Math.imul(h, 16777619) >>> 0; } return () => { h ^= h << 13; h >>>= 0; h ^= h >> 17; h ^= h << 5; h >>>= 0; return h / 4294967296; }; }
function taskView(t, ts) {
  const A = V.ans[t.id] || (V.ans[t.id] = {});
  const done = S.done[t.id] && S.done[t.id].ok;
  let h = `<div class="task"><div class="qh">${typeChip(t)}<span class="chip">${tr('q', { i: V.ti + 1, n: ts.length })}</span><span class="chip">${'●'.repeat(t.l)}${'○'.repeat(3 - t.l)}</span>${done ? '<span class="chip" style="color:var(--ok)">✔</span>' : ''}</div><div class="qt">${t.q}</div>`;
  if (t.t === 'quiz') {
    if (t.code) h += codeBlock(t.code, { title: 'quiz.py' });
    if (t.inp) h += `<div class="muted" style="font-size:12px">⌨️ input: <code>${esc(t.inp.replace(/\n/g, ' ⏎ '))}</code></div>`;
    const rnd = seeded(t.id), order = t.opts.map((_, i) => i);
    for (let i = order.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [order[i], order[j]] = [order[j], order[i]]; }
    h += `<div class="opts">${order.map((oi, k) => { const cls = A.right && oi === t.a ? 'right' : (A.wrong || []).includes(oi) ? 'wrong' : (done && oi === t.a && !A.right ? 'right' : '');
      return `<button class="opt ${cls}" data-act="quiz" data-a="${oi}" ${A.right ? 'disabled' : ''}><span class="lt">${'ABCD'[k]}</span>${esc(t.opts[oi])}</button>`; }).join('')}</div>`;
  } else if (t.t === 'fill') {
    const parts = t.code.split('___'); let html = '';
    parts.forEach((p, i) => { html += hl(p); if (i < parts.length - 1) { const v = A.vals ? A.vals[i] : ''; const w = Math.max(3, ...t.ans[i].map(a => a.length)) + 1;
      html += `<input class="blank ${A.res ? (A.res[i] ? 'okb' : 'badb') : ''}" data-blank="${i}" style="width:${w + 1}ch" value="${esc(v || '')}" autocapitalize="off" autocomplete="off" spellcheck="false" ${A.right ? 'disabled' : ''}>`; } });
    const lines = html.split('\n');
    h += `<div class="code"><div class="code-head">🐍 <span>fill.py</span></div><div class="code-body"><div class="gutter">${lines.map((_, i) => `<div>${i + 1}</div>`).join('')}</div><div class="lines">${lines.map(l => `<div class="ln">${l || ' '}</div>`).join('')}</div></div></div>`;
    if (!A.right) h += `<div class="row-btns"><button class="btn pri" data-act="checkfill">${tr('check')}</button>${(S.done[t.id] && S.done[t.id].tries >= 2) ? `<button class="btn ghost" data-act="revealfill">${tr('showAns')}</button>` : ''}</div>`;
  } else if (t.t === 'bug') {
    if (t.err) h += `<div class="pybox e">${tr('pyTalks')}<br><code>${t.errline ? 'File "bug.py", line ' + t.errline + '<br>' : ''}${esc(t.err)}</code></div>`;
    else h += `<div class="pybox l">${tr('logicBug')}${t.got ? `<br>${tr('prints')} <code>${esc(t.got).replace(/\n/g, ' ⏎ ')}</code>` : ''}</div>`;
    if (t.inp) h += `<div class="muted" style="font-size:12px">⌨️ input: <code>${esc(t.inp.replace(/\n/g, ' ⏎ '))}</code></div>`;
    h += `<div class="muted" style="font-size:13px">${tr('clickLine')}</div>`;
    h += codeBlock(t.code, { title: 'bug.py', cls: 'bug' }).replace(/<div class="ln" data-ln="(\d+)">/g, (m, n) => `<div class="ln ${A.right && +n === t.line ? 'right' : (A.wrong || []).includes(+n) ? 'wrong' : ''}" data-ln="${n}" data-act="${A.right ? '' : 'bugline'}" data-a="${n}">`);
  } else if (t.t === 'code') {
    const draft = S.drafts[t.id] !== undefined ? S.drafts[t.id] : t.start;
    const sample = (t.tests[0] && t.tests[0].i) || '';
    const nl = Math.max(8, draft.split('\n').length + 1);
    h += `<div class="code"><div class="code-head">🐍 <span>solution.py</span><span class="sp"></span><button class="btn sm ghost" data-act="resetcode">${tr('reset')}</button></div><div class="ed-wrap"><div class="gutter" id="edg">${Array.from({ length: nl }, (_, i) => `<div>${i + 1}</div>`).join('')}</div><textarea class="ed" id="ed" spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off" rows="${nl}">${esc(draft)}</textarea></div>${keysBar()}</div>`;
    if (sample || /input\(/.test(t.sol)) h += `<label class="lbl">⌨️ ${tr('stdin')}</label><textarea class="stdin" id="stdin" placeholder="${esc(tr('stdinPh'))}">${esc(A.stdin !== undefined ? A.stdin : sample)}</textarea>`;
    if (t.setup) h += `<div class="muted" style="font-size:12px">📁 ${(t.setup.match(/open\('([^']+)'/) || [])[1] || ''}</div>`;
    h += `<div class="row-btns"><button class="btn" data-act="runcode" style="color:#5fb865">${tr('run')}</button><button class="btn pri" data-act="checkcode" ${A.busy ? 'disabled' : ''}>${tr('check')}</button>${t.hint ? `<button class="btn ghost" data-act="hint">${tr('hint')}</button>` : ''}${((S.done[t.id] && S.done[t.id].tries >= 2) || Py.state === 'fail' || done) ? `<button class="btn ghost" data-act="showsol">${tr('showSol')}</button>` : ''}</div>`;
    if (A.hint) h += `<div class="pybox l">💡 ${esc(t.hint)}</div>`;
    if (Py.state === 'fail' && !done) h += `<div class="pybox e">${tr('pyFail')}</div>`;
    if (A.sol) h += `<h3>${tr('solution')}</h3>` + codeBlock(t.sol, { title: 'solution.py' }) + (Py.state === 'fail' && !done ? `<button class="btn ok" data-act="selfok">${tr('selfCheck')}</button>` : '');
    if (A.run) h += runWin('solution.py', A.run);
    if (A.tests) h += `<div class="tests">${A.tests.map((r, i) => `<div class="trow ${r.ok ? 'okt' : 'badt'}">${r.ok ? '✅' : '❌'} ${tr('test', { i: i + 1 })} ${r.ok ? tr('testOk') : ''}${r.ok ? '' : `${r.i ? `<pre>${tr('input')}:\n${esc(r.i)}</pre>` : ''}${r.err ? `<pre class="err" style="color:var(--bad)">${esc(r.err)}${r.line ? ` (${tr('lineN', { n: r.line })})` : ''}</pre>${tr('hint_' + r.etype) !== 'hint_' + r.etype ? `<div class="errhint"><i class="cpy"></i> ${tr('hint_' + r.etype)}</div>` : ''}` : r.checkfail ? `<pre>${tr('checkFail')} ${esc(r.checkfail)}</pre>` : `<pre>${tr('expected')}:\n${esc(r.o)}\n${tr('got')}:\n${esc(r.got) || tr('noOut')}</pre>`}`}</div>`).join('')}</div>`;
  }
  if (A.right || (done && A.showDone)) h += feedback(t, A);
  else if (A.badMsg) h += `<div class="fb badf"><div class="big">🙈 ${A.badMsg}</div>${tr('retry')}</div>`;
  if (done && !A.right) h += `<div class="row-btns"><button class="btn pri" data-act="nexttask">${V.ti === ts.length - 1 ? tr('finish') : tr('next')}</button></div>`;
  return h + '</div>';
}
function feedback(t, A) {
  return `<div class="fb good"><div class="big">🎉 ${A.praise || ''} ${A.xp ? `<span class="xpfly">+${A.xp} XP</span>` : ''}</div>${t.why ? `<div><b>${tr('why')}</b> ${t.why}</div>` : ''}${t.t === 'bug' && t.fix ? `<div style="margin-top:6px"><b>${tr('fixIs')}</b> <code>${esc(t.fix)}</code></div>` : ''}
<div class="row-btns"><button class="btn pri" data-act="nexttask">${V.ti === stageTasks(course()[V.ci].lessons[V.li]).length - 1 ? tr('finish') : tr('next')}</button></div></div>`;
}
function keysBar() { return `<div class="keys">${['⇥', ':', '(', ')', '"', '[', ']', '{', '}', '=', '+', '*', '#', '_', '<', '>'].map(k => `<button data-key="${esc(k)}">${esc(k)}</button>`).join('')}</div>`; }
function doneView(L) {
  const ts = stageTasks(L); const first = ts.filter(t => S.done[t.id] && S.done[t.id].first).length;
  const r = ts.length ? first / ts.length : 1; const stars = r === 1 ? 3 : r >= .6 ? 2 : 1;
  const C = course(); let nxt = null;
  if (V.li + 1 < C[V.ci].lessons.length) nxt = [V.ci, V.li + 1]; else if (V.ci + 1 < C.length && unlocked(V.ci + 1)) nxt = [V.ci + 1, 0];
  return `<div class="task" style="text-align:center">${capy({ size: 170, mood: 'wow' })}<h1>${tr('done')}</h1><div style="font-size:42px;letter-spacing:4px">${'⭐'.repeat(stars)}${'☆'.repeat(3 - stars)}</div>
<p class="muted">${tr('accuracy')}: ${first}/${ts.length}</p><div class="row-btns" style="justify-content:center">${nxt ? `<button class="btn pri" data-act="lesson" data-a="${nxt[0]}:${nxt[1]}">${tr('nextLesson')}</button>` : ''}<button class="btn" data-act="go" data-a="welcome">${tr('backMap')}</button><button class="btn ghost" data-act="gotask" data-a="0">${tr('again')}</button></div></div>`;
}
function finishLesson() {
  const L = course()[V.ci].lessons[V.li], ts = stageTasks(L);
  if (ts.every(t => S.done[t.id] && S.done[t.id].ok)) {
    const first = ts.filter(t => S.done[t.id].first).length; const r = ts.length ? first / ts.length : 1; const stars = r === 1 ? 3 : r >= .6 ? 2 : 1;
    S.stars[L.id] = Math.max(S.stars[L.id] || 0, stars); checkBadges(); save(); V.phase = 'done'; confetti(); beep('lvl'); kapiSay(pick(tr('correct')), 'wow');
  } else { V.ti = firstUndone(L); }
  renderMain(); scrollTop();
}

/* ===== sandbox ===== */
let SB = { code: null, stdin: '', run: null };
function sandboxView() {
  if (SB.code === null) SB.code = tr('sbHello');
  const nl = Math.max(14, SB.code.split('\n').length + 2);
  return `<div class="doc"><div class="crumb"># playground.py</div><h1>🏖️ ${tr('sbTitle')}</h1>
<div class="code"><div class="code-head">🐍 <span>playground.py</span><span class="sp"></span><button class="btn sm" data-act="sbrun" style="color:#5fb865">${tr('run')}</button></div><div class="ed-wrap"><div class="gutter" id="edg">${Array.from({ length: nl }, (_, i) => `<div>${i + 1}</div>`).join('')}</div><textarea class="ed" id="ed" spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off" rows="${nl}">${esc(SB.code)}</textarea></div>${keysBar()}</div>
<label class="lbl">⌨️ ${tr('stdin')}</label><textarea class="stdin" id="stdin" placeholder="${esc(tr('stdinPh'))}">${esc(SB.stdin)}</textarea>
<div class="row-btns"><button class="btn pri" data-act="sbrun">${tr('run')}</button></div>${SB.run ? runWin('playground.py', SB.run) : ''}</div>`;
}

/* ===== profile ===== */
function profileView() {
  const st = statsOf(S), lv = levelOf(S.xp), total = course().reduce((a, ch) => a + chapProg(ch).n, 0);
  const list = BADGES.map(b => ({ ico: b.ico, n: b[S.lang][0], d: b[S.lang][1], ok: !!S.badges[b.id] }));
  course().forEach(ch => list.push({ ico: ch.icon[S.theme], n: chName(ch), d: '100% ' + W().ch, ok: !!S.badges['ch_' + ch.id] }));
  return `<div class="doc"><div class="crumb"># badges.md</div><div class="hero">${capy({ size: 120 })}<div><h1>${esc(S.name)}</h1><div class="muted">${S.cls ? esc(S.cls) + ' · ' : ''}${tr('st' + S.stage)} · ${tr('level')} ${lv.lv} ${esc(lvTitle(lv.lv))}</div></div></div>
<h2>📊 ${tr('stats')}</h2><div class="statgrid"><div class="stat"><div class="l">💎 XP</div><div class="v">${S.xp}</div></div><div class="stat"><div class="l">✅ ${tr('tasksDone')}</div><div class="v">${st.okCount}/${total}</div></div>
<div class="stat"><div class="l">🎯 ${tr('accuracy')}</div><div class="v">${st.okCount ? Math.round(st.first / st.okCount * 100) : 0}%</div></div><div class="stat"><div class="l">🔥 ${tr('bestCombo')}</div><div class="v">${S.bestCombo}</div></div>
<div class="stat"><div class="l">📅 ${tr('streak')}</div><div class="v">${S.streak.n}</div></div><div class="stat"><div class="l">▶ ${tr('codeRuns')}</div><div class="v">${S.codeRuns}</div></div></div>
<h2>🏅 ${tr('badges')}</h2><div class="badges">${list.map(b => `<div class="badge ${b.ok ? '' : 'off'}"><div class="bi">${b.ico}</div><b>${esc(b.n)}</b><small>${esc(b.d)}</small></div>`).join('')}</div>
<div class="row-btns" style="margin-top:18px"><button class="btn pri" data-act="progress">💾 ${tr('progress')}</button></div></div>`;
}

/* ===== modal ===== */
function modal(html, cls = '') { closeModal(); const o = document.createElement('div'); o.className = 'ov'; o.id = 'ov'; o.innerHTML = `<div class="modal ${cls}">${html}</div>`; o.addEventListener('click', e => { if (e.target === o) closeModal(); }); document.body.appendChild(o); }
function closeModal() { const o = document.getElementById('ov'); if (o) o.remove(); }
function confirmBox(msg, onYes) { modal(`<div class="mb">${capy({ size: 80, mood: 'think' })}<p>${msg}</p></div><div class="mf"><button class="btn" data-act="close">${tr('no')}</button><button class="btn pri" id="yesbtn">${tr('yes')}</button></div>`); document.getElementById('yesbtn').onclick = () => { closeModal(); onYes(); }; }
let SETTAB = 'look';
function settingsModal() {
  const sec = {
    look: `<h3>${tr('chooseTheme')}</h3><div class="choices">${['rpg', 'space', 'neutral'].map(x => `<button class="choice ${S.theme === x ? 'on' : ''}" data-act="settheme" data-a="${x}"><span class="ce">${{ rpg: '🏰', space: '🚀', neutral: '💻' }[x]}</span><b>${tr('th_' + x)}</b><small>${tr('th_' + x + 'd')}</small></button>`).join('')}</div>
      <div class="switch"><span>${tr('sound')}</span><input type="checkbox" data-set="sound" ${S.sound ? 'checked' : ''}></div>`,
    learn: `<label class="lbl">${tr('yourName')}</label><input class="inp" data-set="name" value="${esc(S.name)}" maxlength="30"><label class="lbl">${tr('yourClass')}</label><input class="inp" data-set="cls" value="${esc(S.cls)}" maxlength="12">
      <h3 style="margin-top:14px">${tr('chooseStage')}</h3><div class="choices">${[1, 2, 3].map(i => `<button class="choice ${S.stage === i ? 'on' : ''}" data-act="setstage" data-a="${i}"><span class="ce">${['🌱', '🚀', '🏆'][i - 1]}</span><b>${tr('st' + i)}</b><small>${tr('st' + i + 'd')}</small></button>`).join('')}</div>
      <div class="switch"><span>${tr('unlockAll')}</span><input type="checkbox" data-set="unlockAll" ${S.unlockAll ? 'checked' : ''}></div>`,
    prog: `<div class="row-btns"><button class="btn pri" data-act="progress">💾 ${tr('progress')}</button></div><div class="row-btns"><button class="btn" style="color:var(--bad)" data-act="resetall">🗑️ ${tr('resetProg')}</button></div>`
  };
  modal(`<div class="mh">⚙️ ${tr('settings')}<button class="btn sm ghost" data-act="close">✕</button></div><div class="settings"><nav>${[['look', '🎨 ' + tr('look')], ['learn', '🎓 ' + tr('chooseStage')], ['prog', '💾 ' + tr('progress')]].map(([k, n]) => `<button class="${SETTAB === k ? 'on' : ''}" data-act="settab" data-a="${k}">${n}</button>`).join('')}</nav><section>${sec[SETTAB]}</section></div><div class="mf"><button class="btn pri" data-act="close">${tr('close')}</button></div>`, 'wide');
}

/* ===== events ===== */
document.addEventListener('click', async e => {
  const kb = e.target.closest('[data-key]');
  if (kb) { const ed = document.getElementById('ed'); if (ed) { const k = kb.dataset.key === '⇥' ? '    ' : kb.dataset.key; insertAt(ed, k); } return; }
  if (e.target.closest('[data-dice]')) { const d = e.target.closest('[data-dice]'); d.classList.remove('roll'); void d.offsetWidth; d.classList.add('roll'); d.textContent = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'][Math.floor(Math.random() * 6)]; return; }
  const pb = e.target.closest('[data-play]'); if (pb) { playScene(pb.dataset.play); return; }
  const rb = e.target.closest('[data-reset]'); if (rb) { resetScene(rb.dataset.reset); return; }
  const el = e.target.closest('[data-act]'); if (!el || !el.dataset.act) { if (V.drawer && !e.target.closest('#proj')) { V.drawer = false; document.getElementById('proj')?.classList.remove('show'); } return; }
  const act = el.dataset.act, a = el.dataset.a;
  const C = course();
  switch (act) {
    case 'close': closeModal(); render(); break;
    case 'drawer': V.drawer = !V.drawer; document.getElementById('proj')?.classList.toggle('show', V.drawer); e.stopPropagation(); break;
    case 'go': if (a === 'teacher') return openTeacher(); go(a); break;
    case 'lang': S.lang = a; save(); render(); if (document.getElementById('ov')) closeModal(); break;
    case 'mode': S.mode = S.mode === 'dark' ? 'light' : 'dark'; save(); render(); break;
    case 'settings': SETTAB = 'look'; settingsModal(); break;
    case 'settab': SETTAB = a; settingsModal(); break;
    case 'setstage': S.stage = +a; save(); if (S.onboarded) { settingsModal(); render(); } else render(); break;
    case 'settheme': S.theme = a; save(); render(); if (S.onboarded && document.getElementById('ov')) settingsModal(); break;
    case 'startapp': S.name = (document.getElementById('ob-name').value || '').trim() || 'Kapi'; S.cls = (document.getElementById('ob-cls').value || '').trim(); S.onboarded = true; S.created = Date.now(); touchStreak(); save(); confetti(); render(); kapiSay(tr('hello', { name: esc(S.name) }) + ' <i class="cpy"></i>'); break;
    case 'teacherstart': S.onboarded = true; save(); openTeacher(); break;
    case 'fold': V.open[a] = !V.open[a]; document.getElementById('proj').innerHTML = treeHtml(); break;
    case 'locked': beep('bad'); kapiSay('🔒 ' + tr('locked'), 'sad'); break;
    case 'opench': { const ci = +a; V.open[C[ci].id] = true; const L = C[ci].lessons; let li = L.findIndex(x => { const p = lessonProg(x); return p.d < p.n; }); openLesson(ci, li < 0 ? 0 : li); break; }
    case 'lesson': { const [ci, li] = a.split(':').map(Number); if (!unlocked(ci)) { kapiSay('🔒 ' + tr('locked'), 'sad'); break; } openLesson(ci, li); break; }
    case 'closetab': e.stopPropagation(); V.tabs = V.tabs.filter(x => x !== a); if (V.view === 'lesson' && a === V.ci + ':' + V.li) V.view = 'welcome'; render(); break;
    case 'phase': V.phase = a; if (a === 'tasks') V.ti = firstUndone(C[V.ci].lessons[V.li]); renderMain(); scrollTop(); break;
    case 'gotask': V.phase = 'tasks'; V.ti = +a; renderMain(); break;
    case 'runex': case 'runcur': {
      if (V.view === 'sandbox') return sbRun();
      if (V.view === 'lesson' && V.phase !== 'theory') { if (document.getElementById('ed')) return codeRun(); return; }
      if (V.view !== 'lesson') { go('sandbox'); return; }
      const L = C[V.ci].lessons[V.li]; const exs = L.ex.filter(x => !x.lvl || x.lvl <= S.stage); const i = act === 'runcur' ? 0 : +a; const ex = exs[i]; if (!ex) return;
      const k = L.id + '-ex' + i; V.ans[k] = ex.err ? { disp: ex.out ? ex.out + '\n' : '', err: ex.err, line: ex.errline, etype: ex.etype } : { disp: ex.out + (ex.out ? '\n' : '') };
      document.getElementById('exout-' + i).innerHTML = runWin(`example_${i + 1}.py`, V.ans[k]); beep('click');
      if (ex.rnd && Py.state === 'ready') { const r = await Py.run(ex.code, ex.inp || ''); V.ans[k] = r; document.getElementById('exout-' + i).innerHTML = runWin(`example_${i + 1}.py`, r); }
      break; }
    case 'tryex': { const L = C[V.ci].lessons[V.li]; const ex = L.ex.filter(x => !x.lvl || x.lvl <= S.stage)[+a]; SB.code = ex.code; SB.stdin = ex.inp || ''; SB.run = null; go('sandbox'); break; }
    case 'quiz': quizAnswer(+a); break;
    case 'checkfill': fillCheck(); break;
    case 'revealfill': { const t = curTask(); reveal(t); const A = V.ans[t.id]; A.vals = t.ans.map(x => x[0]); A.res = null; renderMain(); break; }
    case 'bugline': bugAnswer(+a); break;
    case 'runcode': codeRun(); break;
    case 'checkcode': codeCheck(); break;
    case 'hint': V.ans[curTask().id].hint = true; renderMain(); break;
    case 'showsol': { const t = curTask(); if (!(S.done[t.id] && S.done[t.id].ok)) reveal(t); V.ans[t.id].sol = true; renderMain(); break; }
    case 'selfok': { const t = curTask(); const A = V.ans[t.id]; A.xp = award(t, { self: true }); A.right = true; A.praise = pick(tr('correct')); renderMain(); break; }
    case 'resetcode': { const t = curTask(); delete S.drafts[t.id]; save(); renderMain(); break; }
    case 'nexttask': { const ts = stageTasks(C[V.ci].lessons[V.li]); if (V.ti < ts.length - 1) { V.ti++; renderMain(); scrollToTask(); } else finishLesson(); break; }
    case 'sbrun': sbRun(); break;
    case 'progress': progressModal(); break;
    case 'resetall': confirmBox(tr('resetQ'), () => { const keep = { lang: S.lang, mode: S.mode, theme: S.theme }; S = Object.assign({}, DEF, keep); window.S = S; save(); V.view = 'welcome'; V.tabs = []; render(); }); break;
    case 'copy': copyText(el.dataset.src ? document.getElementById(el.dataset.src).textContent : ''); el.textContent = '✔ ' + tr('copied'); break;
    case 'dl': downloadProgress(); break;
    case 'pickfile': document.getElementById(a).click(); break;
    case 'impcode': importStudentText(document.getElementById('impta').value); break;
    default: if (typeof teacherAct === 'function') teacherAct(act, a, el);
  }
});
document.addEventListener('change', e => {
  const s = e.target.dataset.set;
  if (s) { S[s] = e.target.type === 'checkbox' ? e.target.checked : e.target.value; save(); if (s !== 'name' && s !== 'cls') render(); return; }
  if (e.target.id === 'impfile' && e.target.files[0]) e.target.files[0].text().then(importStudentText);
  if (e.target.id === 'tfile') teacherFiles(e.target.files);
});
document.addEventListener('input', e => {
  if (e.target.id === 'ob-name') S.name = e.target.value;
  if (e.target.id === 'ob-cls') S.cls = e.target.value;
  if (e.target.id === 'ed') {
    const v = e.target.value;
    if (V.view === 'sandbox') SB.code = v; else { const t = curTask(); if (t) { S.drafts[t.id] = v; saveSoon(); } }
    const g = document.getElementById('edg'); const n = Math.max(8, v.split('\n').length + 1);
    if (g && g.children.length !== n) g.innerHTML = Array.from({ length: n }, (_, i) => `<div>${i + 1}</div>`).join(''); e.target.rows = n;
  }
  if (e.target.id === 'stdin') { if (V.view === 'sandbox') SB.stdin = e.target.value; else { const t = curTask(); if (t) V.ans[t.id].stdin = e.target.value; } }
  if (e.target.classList.contains('blank')) { const t = curTask(); const A = V.ans[t.id]; A.vals = A.vals || []; A.vals[+e.target.dataset.blank] = e.target.value; e.target.classList.remove('okb', 'badb'); }
});
document.addEventListener('keydown', e => {
  if (e.target.id === 'ed') {
    const ed = e.target;
    if (e.key === 'Tab') { e.preventDefault(); insertAt(ed, '    '); }
    else if (e.key === 'Enter') {
      const pos = ed.selectionStart, before = ed.value.slice(0, pos), line = before.split('\n').pop();
      let ind = (line.match(/^\s*/) || [''])[0]; if (/:\s*$/.test(line)) ind += '    ';
      e.preventDefault(); insertAt(ed, '\n' + ind);
    } else if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); V.view === 'sandbox' ? sbRun() : codeRun(); }
  }
  if (e.target.classList && e.target.classList.contains('blank') && e.key === 'Enter') { e.preventDefault(); fillCheck(); }
  if (e.key === 'Escape') closeModal();
});
let saveT; const saveSoon = () => { clearTimeout(saveT); saveT = setTimeout(save, 500); };
function insertAt(ed, s) { const a = ed.selectionStart, b = ed.selectionEnd; ed.setRangeText(s, a, b, 'end'); ed.dispatchEvent(new Event('input', { bubbles: true })); ed.focus(); }
function curTask() { if (V.view !== 'lesson') return null; return stageTasks(course()[V.ci].lessons[V.li])[V.ti]; }
function scrollToTask() { const t = document.querySelector('.task'); if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
function afterRender() {}

/* ===== answer handlers ===== */
function good(t, A) { A.xp = award(t); A.right = true; A.praise = pick(tr('correct')); kapiSay(`<b>${A.praise}</b>${A.xp ? ` +${A.xp} XP` : ''}`, 'happy'); if (A.xp) confetti(25); }
function bad(t, A, msg) { fail(t); A.badMsg = msg || pick(tr('wrong')); kapiSay(A.badMsg + (t.why && (S.done[t.id].tries >= 2) ? '<br><small>' + t.why + '</small>' : ''), 'sad'); }
function quizAnswer(oi) {
  const t = curTask(), A = V.ans[t.id];
  if (oi === t.a) { A.badMsg = null; good(t, A); } else { A.wrong = (A.wrong || []).concat(oi); bad(t, A); }
  renderMain();
}
const nrm = s => (s || '').replace(/\s+/g, '').replace(/'/g, '"');
function fillCheck() {
  const t = curTask(), A = V.ans[t.id];
  document.querySelectorAll('.blank').forEach(b => { A.vals = A.vals || []; A.vals[+b.dataset.blank] = b.value; });
  A.res = t.ans.map((acc, i) => acc.some(x => nrm(x) === nrm((A.vals || [])[i])));
  if (A.res.every(Boolean)) { A.badMsg = null; good(t, A); } else bad(t, A);
  renderMain();
}
function bugAnswer(n) {
  const t = curTask(), A = V.ans[t.id];
  if (n === t.line) { A.badMsg = null; good(t, A); } else { A.wrong = (A.wrong || []).concat(n); bad(t, A); }
  renderMain();
}
async function codeRun() {
  const t = curTask(); if (!t || t.t !== 'code') return; const A = V.ans[t.id];
  const code = document.getElementById('ed').value, stdin = (document.getElementById('stdin') || {}).value || '';
  A.run = { loading: true }; A.tests = null; renderMain();
  try { A.run = await Py.run(code, stdin, t.setup || ''); } catch (e) { A.run = null; }
  renderMain();
}
async function codeCheck() {
  const t = curTask(); if (!t) return; const A = V.ans[t.id];
  const code = document.getElementById('ed').value; S.drafts[t.id] = code;
  A.busy = true; A.run = { loading: true }; A.tests = null; renderMain();
  try {
    const tests = t.tests.length ? t.tests : [{ i: '', o: null }]; const res = [];
    for (const tc of tests) {
      const r = await Py.run(code, tc.i, t.setup || '', t.check || '');
      const ok = !r.err && !r.checkfail && (tc.o === null || norm(r.out) === norm(tc.o));
      res.push({ ok, i: tc.i, o: tc.o, got: norm(r.out), err: r.err, etype: r.etype, line: r.line, checkfail: r.checkfail });
    }
    A.tests = res; A.run = null; A.busy = false;
    if (res.every(x => x.ok)) { A.badMsg = null; good(t, A); A.praise = tr('allOk') + ' ' + A.praise; } else bad(t, A);
  } catch (e) { A.busy = false; A.run = null; }
  renderMain();
}
async function sbRun() {
  const ed = document.getElementById('ed'); if (ed) SB.code = ed.value; const si = document.getElementById('stdin'); if (si) SB.stdin = si.value;
  SB.run = { loading: true }; renderMain();
  try { SB.run = await Py.run(SB.code, SB.stdin); S.sbRuns++; checkBadges(); save(); } catch (e) { SB.run = { err: tr('pyFail'), etype: '', disp: '' }; }
  renderMain();
}

/* ===== progress encode / decode ===== */
const SALT = 'CappySoft.pl/PyKapi#2026';
function fnv(str) { let h = 0x811c9dc5; for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h.toString(16).padStart(8, '0'); }
const xorb = b => { const k = new TextEncoder().encode(SALT); return b.map((x, i) => x ^ k[i % k.length] ^ (i * 7 & 255)); };
const b64e = b => { let s = ''; for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000)); return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''); };
const b64d = s => { s = s.replace(/-/g, '+').replace(/_/g, '/'); while (s.length % 4) s += '='; const r = atob(s); const b = new Uint8Array(r.length); for (let i = 0; i < r.length; i++) b[i] = r.charCodeAt(i); return b; };
async function zip(b, mode) { const st = mode === 'c' ? new CompressionStream('deflate-raw') : new DecompressionStream('deflate-raw'); return new Uint8Array(await new Response(new Blob([b]).stream().pipeThrough(st)).arrayBuffer()); }
function payload() {
  const done = {}; for (const id in S.done) { const d = S.done[id]; done[id] = [d.ok ? 1 : 0, d.first ? 1 : 0, d.tries || 0]; }
  return { app: 'pykapi', v: 1, name: S.name, cls: S.cls, stage: S.stage, xp: S.xp, done, stars: S.stars, badges: Object.keys(S.badges), streak: S.streak.n, bestCombo: S.bestCombo, codeRuns: S.codeRuns, created: S.created, ts: Date.now(), lang: S.lang };
}
async function encodeProgress(obj) {
  const json = JSON.stringify(obj); const sum = fnv(SALT + json); let bytes = new TextEncoder().encode(json); let fl = 'p';
  if (window.CompressionStream) { try { bytes = await zip(bytes, 'c'); fl = 'z'; } catch (e) { bytes = new TextEncoder().encode(json); } }
  return `PYKAPI1.${fl}.${sum}.${b64e(xorb(bytes))}`;
}
async function decodeProgress(text) {
  const m = (text || '').replace(/\s+/g, '').match(/PYKAPI1\.([pz])\.([0-9a-f]{8})\.([A-Za-z0-9_-]+)/); if (!m) throw new Error('fmt');
  let bytes = xorb(b64d(m[3])); if (m[1] === 'z') bytes = await zip(bytes, 'd');
  const json = new TextDecoder().decode(bytes); if (fnv(SALT + json) !== m[2]) throw new Error('sum');
  const o = JSON.parse(json); if (o.app !== 'pykapi') throw new Error('app'); return o;
}
let DL = null;
const IN_CLAUDE = !!(window.claude && window.claude.use);
const canSave = () => !!DL || !IN_CLAUDE;
async function saveFile(filename, data, mime = 'text/plain') {
  if (DL) { await DL.save({ filename, data }); return; }
  const url = URL.createObjectURL(new Blob([data], { type: mime + ';charset=utf-8' }));
  const a = document.createElement('a'); a.href = url; a.download = filename; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 2000);
}
(async () => { try { if (window.claude && claude.use) DL = await claude.use('downloads'); } catch (e) { DL = null; } })();
function fileName() { return `kapipasta-${(S.name || 'uczen').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^\w-]+/g, '_')}${S.cls ? '-' + S.cls.replace(/[^\w-]+/g, '') : ''}-${todayStr()}.txt`; }
async function progressModal() {
  const code = await encodeProgress(payload());
  const fileTxt = `# KapiPasta - Python – ${S.lang === 'en' ? 'student progress (encoded file, do not edit)' : 'postęp ucznia (plik zakodowany, nie edytuj)'}\n# ${S.name}${S.cls ? ' / ' + S.cls : ''} · ${new Date().toLocaleString()}\n${code.match(/.{1,76}/g).join('\n')}\n`;
  window._PF = fileTxt;
  modal(`<div class="mh">💾 ${tr('progress')}<button class="btn sm ghost" data-act="close">✕</button></div><div class="mb">
<h3>📤 ${tr('expTitle')}</h3><p class="muted">${tr('expDesc')}</p>
<div class="row-btns">${canSave() ? `<button class="btn pri" data-act="dl">${tr('dlFile')}</button>` : ''}<button class="btn" data-act="copy" data-src="pcode">${tr('copyCode')}</button></div>
${canSave() ? '' : `<p class="muted" style="font-size:12px">${tr('dlNo')}</p>`}<div class="codeout" id="pcode">${esc(code)}</div>
<h3 style="margin-top:18px">📥 ${tr('impTitle')}</h3><p class="muted">${tr('impDesc')}</p>
<input type="file" id="impfile" accept=".txt,.kapi,text/plain" hidden><div class="row-btns"><button class="btn" data-act="pickfile" data-a="impfile">${tr('pickFile')}</button></div>
<textarea class="inp" id="impta" placeholder="${tr('pasteCode')}"></textarea><div class="row-btns"><button class="btn pri" data-act="impcode">${tr('load')}</button></div></div>`);
}
async function downloadProgress() {
  if (!canSave()) return;
  try { await saveFile(fileName(), window._PF); toast('✔ ' + tr('saved')); }
  catch (e) { if (e && (e.code === 'unavailable' || e.code === 'not_granted')) { DL = null; progressModal(); } }
}
function copyText(s) {
  const done = () => toast('📋 ' + tr('copied'));
  try { navigator.clipboard.writeText(s).then(done, () => fallbackCopy(s)); } catch (e) { fallbackCopy(s); }
}
function fallbackCopy(s) { const ta = document.createElement('textarea'); ta.value = s; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); toast('📋 ' + tr('copied')); } catch (e) { } ta.remove(); }
async function importStudentText(text) {
  let o; try { o = await decodeProgress(text); } catch (e) { toast('⚠️ ' + tr('badCode')); return; }
  confirmBox(tr('impQ', { name: esc(o.name), xp: o.xp }), () => {
    const done = {}; for (const id in o.done) { const d = o.done[id]; done[id] = { ok: d[0], first: d[1], tries: d[2] }; }
    Object.assign(S, { name: o.name, cls: o.cls || '', stage: o.stage, xp: o.xp, done, stars: o.stars || {}, bestCombo: o.bestCombo || 0, codeRuns: o.codeRuns || 0, onboarded: true });
    S.badges = {}; (o.badges || []).forEach(b => S.badges[b] = Date.now()); S.streak = { last: todayStr(), n: o.streak || 1 };
    save(); render(); confetti(); toast('✔ ' + tr('impOk'));
  });
}

window.addEventListener('DOMContentLoaded', () => { render(); });
