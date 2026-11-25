/* ===== Kapibara + sceny ===== */
const HATS = {
  rpg: '<g transform="translate(78,2)"><path d="M2 26 L16 -6 L30 26 Z" fill="#6b4bd6"/><ellipse cx="16" cy="26" rx="18" ry="4" fill="#5a3cc0"/><text x="12" y="16" font-size="9" fill="#ffd34d">★</text></g>',
  space: '<g><circle cx="92" cy="44" r="29" fill="rgba(170,220,255,.25)" stroke="#bfe6ff" stroke-width="2.5"/><path d="M76 28 q8 -8 18 -6" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" opacity=".8"/><rect x="74" y="70" width="36" height="6" rx="3" fill="#9fb3d9"/></g>',
  neutral: '<g transform="translate(80,10)"><circle cx="11" cy="12" r="10" fill="#ffa62b"/><circle cx="8" cy="9" r="2.5" fill="#ffd08a"/><path d="M11 2 q4 -6 10 -3 q-4 5 -10 3" fill="#4caf50"/></g>'
};
function capy(o = {}) {
  const mood = o.mood || 'happy', hat = o.hat === undefined ? (window.S ? S.theme : 'neutral') : o.hat;
  const eye = mood === 'happy' ? '<path d="M92 39 q3 -4 6 0" stroke="#2b1a10" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    : mood === 'sad' ? '<circle cx="95" cy="40" r="2.8" fill="#2b1a10"/><path d="M95 45 q-1 4 0 6 q1 -2 0 -6" fill="#6cc4ff"/>'
    : mood === 'wow' ? '<circle cx="95" cy="40" r="3.6" fill="#2b1a10"/><circle cx="96" cy="39" r="1.2" fill="#fff"/>'
    : '<circle cx="95" cy="40" r="2.8" fill="#2b1a10"/><circle cx="96" cy="39" r="1" fill="#fff"/>';
  const mouth = mood === 'sad' ? '<path d="M108 58 q4 -3 8 0" stroke="#5a3a24" stroke-width="1.6" fill="none"/>'
    : '<path d="M108 56 q4 4 8 0" stroke="#5a3a24" stroke-width="1.6" fill="none"/>';
  const item = o.item ? `<text x="112" y="80" font-size="20">${o.item}</text>` : '';
  const hatSvg = (hat === 'space') ? '' : (HATS[hat] || '');
  return `<svg class="capy ${o.cls || ''}" viewBox="0 0 130 100" width="${o.size || 110}" aria-hidden="true">
<ellipse cx="62" cy="93" rx="44" ry="5" fill="rgba(0,0,0,.15)"/>
<rect x="30" y="68" width="11" height="24" rx="5" fill="#8a5c3b"/><rect x="47" y="70" width="11" height="22" rx="5" fill="#7a4f31"/>
<rect x="76" y="68" width="11" height="24" rx="5" fill="#8a5c3b"/><rect x="90" y="70" width="10" height="21" rx="5" fill="#7a4f31"/>
<ellipse cx="60" cy="58" rx="45" ry="28" fill="#b98258"/><ellipse cx="55" cy="50" rx="30" ry="12" fill="#c8946a" opacity=".55"/>
<ellipse cx="92" cy="46" rx="24" ry="20" fill="#b98258"/>
<rect x="98" y="38" width="24" height="24" rx="11" fill="#a3714b"/>
<ellipse cx="82" cy="27" rx="6.5" ry="5.5" fill="#7a4f31"/><ellipse cx="82" cy="28" rx="3.5" ry="3" fill="#5d3a22"/>
${eye}<ellipse cx="117" cy="46" rx="1.8" ry="2.8" fill="#3b2414"/><ellipse cx="111" cy="46" rx="1.4" ry="2.4" fill="#3b2414"/>
${mouth}<circle cx="101" cy="54" r="4.5" fill="#ff8fa3" opacity=".45"/>
${hatSvg}${hat === 'space' ? HATS.space : ''}${item}</svg>`;
}

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

/* animated scene registry: id -> {n, step(k), reset()} */
const PLAYERS = {};
let PID = 0;
function player(n, step, reset) {
  const id = 'p' + (++PID);
  PLAYERS[id] = { n, step, reset, k: 0, timer: null };
  return id;
}
function ctrl(id) {
  return `<div class="pctrl"><button class="pbtn" data-play="${id}" aria-label="play">▶</button><button class="pbtn ghost" data-reset="${id}" aria-label="reset">↺</button><span class="pstep" id="${id}-st"></span></div>`;
}
function playScene(id) {
  const P = PLAYERS[id]; if (!P) return;
  if (P.timer) { clearInterval(P.timer); P.timer = null; return; }
  if (P.k >= P.n) { P.reset(); P.k = 0; }
  const tick = () => {
    if (P.k >= P.n) { clearInterval(P.timer); P.timer = null; return; }
    try { P.step(P.k); } catch (e) { clearInterval(P.timer); P.timer = null; delete PLAYERS[id]; return; }
    P.k++;
    const st = document.getElementById(id + '-st'); if (st) st.textContent = P.k + ' / ' + P.n;
  };
  tick(); P.timer = setInterval(tick, 900);
}
function stopAllScenes() { for (const id in PLAYERS) { clearInterval(PLAYERS[id].timer); delete PLAYERS[id]; } }
function resetScene(id) {
  const P = PLAYERS[id]; if (!P) return;
  clearInterval(P.timer); P.timer = null; P.k = 0; try { P.reset(); } catch (e) { }
  const st = document.getElementById(id + '-st'); if (st) st.textContent = '';
}
const $id = i => document.getElementById(i);

function renderScene(sc, ex) {
  const L = t => tr(t);
  const outLines = (ex.out || '').split('\n').filter(x => x !== '');
  const wrap = (inner, mood, extra = '') => `<div class="scene sc-${sc.s}">${extra}<div class="scene-row"><div class="scene-capy">${capy({ mood: mood || 'happy' })}</div><div class="scene-main">${inner}</div></div><div class="scene-cap">🐾 ${sc.cap || ''}</div></div>`;
  switch (sc.s) {
    case 'say': {
      const txt = ex.err ? `<span class="bad">${esc(ex.err)}</span>` : esc(ex.out || '');
      return wrap(`<div class="sign"><div class="sign-board">${txt.replace(/\n/g, '<br>') || '&nbsp;'}</div><div class="sign-pole"></div></div>`);
    }
    case 'boxes':
      return wrap(`<div class="boxes">${sc.vars.map(v => `<div class="vbox t-${v[2]}"><div class="vname">${esc(v[0])}</div><div class="vval">${esc(v[1])}</div><div class="vtype">${v[2]}</div></div>`).join('')}</div>`);
    case 'cards':
      return wrap(`<div class="cards">${sc.items.map(c => `<div class="ccard"><code>${esc(c[0])}</code><span class="arrow">→</span><b>${esc(c[1])}</b>${c[2] ? `<small>${esc(c[2])}</small>` : ''}</div>`).join('')}</div>`);
    case 'share': {
      const q = Math.floor(sc.n / sc.k), r = sc.n % sc.k;
      const id = player(sc.n, k => {
        const b = k < q * sc.k ? 'b' + (k % sc.k) : 'rest';
        const el = $id(id + '-' + b); if (el) el.insertAdjacentHTML('beforeend', '<span class="pop">🍊</span>');
      }, () => { for (let i = 0; i < sc.k; i++) $id(id + '-b' + i).innerHTML = ''; $id(id + '-rest').innerHTML = ''; });
      return wrap(`<div class="share">${Array.from({ length: sc.k }, (_, i) => `<div class="basket"><div class="bk-in" id="${id}-b${i}"></div><div class="bk-lbl">🧺 ${i + 1}</div></div>`).join('')}<div class="basket rest"><div class="bk-in" id="${id}-rest"></div><div class="bk-lbl">${L('left')}</div></div></div><div class="share-res"><code>${sc.n} // ${sc.k} = ${q}</code> <code>${sc.n} % ${sc.k} = ${r}</code></div>${ctrl(id)}`);
    }
    case 'fork':
      return `<div class="scene sc-fork"><div class="fork-cond"><code>if ${esc(sc.cond)}:</code> → <b>${esc(sc.val)}</b></div><div class="fork-paths"><div class="path ${sc.val === 'True' ? 'on' : 'off'}">✔ True<br><span>${esc(sc.yes)}</span>${sc.val === 'True' ? capy({ size: 80 }) : ''}</div><div class="path ${sc.val !== 'True' ? 'on' : 'off'}">✖ else<br><span>${esc(sc.no)}</span>${sc.val !== 'True' ? capy({ size: 80 }) : ''}</div></div><div class="scene-cap">🐾 ${sc.cap}</div></div>`;
    case 'ladder':
      return wrap(`<div class="ladder">${sc.steps.map(s => `<div class="door ${s[1] === true ? 'on' : s[1] === false ? 'no' : 'skip'}"><code>${esc(s[0])}</code><span>${s[1] === true ? '✔ True' : s[1] === false ? '✖ False' : L('skipped')}</span></div>`).join('')}<div class="door res">🚪 → <b>${esc(sc.res)}</b></div></div>`);
    case 'row': {
      const n = sc.items.length, hl = sc.hl || [-1, -1];
      return wrap(`<div class="rowlbl">${esc(sc.label || '')}</div><div class="row">${sc.items.map((x, i) => `<div class="cell ${i >= hl[0] && i < hl[1] ? 'hl' : ''}"><small>${i}</small><span>${esc(x)}</span><small class="neg">${i - n}</small></div>`).join('')}</div>`, 'wow');
    }
    case 'loop': {
      const items = sc.items;
      const id = player(items.length, k => {
        items.forEach((_, i) => $id(`${id}-c${i}`).classList.toggle('cur', i === k));
        if (k > 0) $id(`${id}-c${k - 1}`).classList.add('done');
        const per = outLines.length / items.length;
        const upto = k === items.length - 1 ? outLines.length : Math.round((k + 1) * per);
        $id(id + '-out').textContent = outLines.slice(0, upto).join('\n');
        if (sc.acc) $id(id + '-acc').textContent = `${sc.acc} = ${sc.accv[k]}`;
        const cap = $id(id + '-cp'); cap.style.transform = `translateX(${k * 46}px)`;
      }, () => {
        items.forEach((_, i) => $id(`${id}-c${i}`).classList.remove('cur', 'done'));
        $id(id + '-out').textContent = ''; if (sc.acc) $id(id + '-acc').textContent = `${sc.acc} = ?`;
        $id(id + '-cp').style.transform = 'translateX(0)';
      });
      return `<div class="scene sc-loop"><div class="loop-track"><div class="row">${items.map((x, i) => `<div class="cell" id="${id}-c${i}"><span>${esc(x)}</span></div>`).join('')}</div><div class="walker" id="${id}-cp">${capy({ size: 58 })}</div></div>${sc.acc ? `<div class="acc" id="${id}-acc">${sc.acc} = ?</div>` : ''}<pre class="console" id="${id}-out"></pre>${ctrl(id)}<div class="scene-cap">🐾 ${sc.cap}</div></div>`;
    }
    case 'grid': {
      const cells = [];
      for (let r = 0; r < sc.rows; r++) for (let c = 0; c < sc.cols; c++) if (!sc.tri || c <= r) cells.push([r, c]);
      const id = player(cells.length, k => { const [r, c] = cells[k]; $id(`${id}-${r}-${c}`).textContent = sc.emo; $id(`${id}-${r}-${c}`).classList.add('pop'); },
        () => cells.forEach(([r, c]) => { const e = $id(`${id}-${r}-${c}`); e.textContent = ''; e.classList.remove('pop'); }));
      let g = '';
      for (let r = 0; r < sc.rows; r++) { g += '<div class="grow">'; for (let c = 0; c < sc.cols; c++) g += (!sc.tri || c <= r) ? `<div class="gcell" id="${id}-${r}-${c}"></div>` : '<div class="gcell empty"></div>'; g += '</div>'; }
      return wrap(`<div class="grid">${g}</div>${ctrl(id)}`);
    }
    case 'venn':
      return `<div class="scene sc-venn"><div class="venn"><div class="vc a"><b>${esc(sc.la)}</b>${sc.a.map(esc).join('<br>')}</div><div class="vmid">${sc.both.map(esc).join('<br>')}<small>&amp;</small></div><div class="vc b"><b>${esc(sc.lb)}</b>${sc.b.map(esc).join('<br>')}</div></div><div class="scene-cap">🐾 ${sc.cap}</div></div>`;
    case 'dict':
      return wrap(`<div class="lockers">${sc.pairs.map(p => `<div class="locker ${p[0] === sc.hl ? 'hl' : ''}"><div class="lk-key">🏷️ "${esc(p[0])}"</div><div class="lk-val">${esc(p[1])}</div></div>`).join('')}</div>`);
    case 'machine': {
      const id = player(3, k => { $id(id).dataset.st = k + 1; }, () => { $id(id).dataset.st = 0; });
      return wrap(`<div class="machine" id="${id}" data-st="0"><div class="m-in">${sc.inp.map(x => `<span>${esc(x)}</span>`).join('')}</div><div class="m-box"><div class="gear">⚙️</div><code>${esc(sc.name)}</code></div><div class="m-out">return <b>${esc(sc.out)}</b></div></div>${ctrl(id)}`);
    }
    case 'scope':
      return wrap(`<div class="scope"><div class="room glob"><b>🏠 ${L('global')}</b>${sc.glob.map(v => `<div class="vbox"><div class="vname">${esc(v[0])}</div><div class="vval">${esc(v[1])}</div></div>`).join('')}</div><div class="room loc"><b>⛺ ${esc(sc.fn)} – ${L('local')}</b>${sc.loc.length ? sc.loc.map(v => `<div class="vbox"><div class="vname">${esc(v[0])}</div><div class="vval">${esc(v[1])}</div></div>`).join('') : '<small>global →🏠</small>'}</div></div>`);
    case 'dice':
      return wrap(`<button class="dice" data-dice="1" aria-label="roll">🎲</button><div class="dice-out">${esc(ex.out || '')}</div>`, 'wow');
    case 'file':
      return wrap(`<div class="scroll"><div class="scroll-name">📜 ${esc(sc.name)}</div>${sc.lines.map((l, i) => `<div class="scroll-line"><small>${i + 1}</small>${esc(l)}</div>`).join('')}</div>`);
    case 'err':
      return wrap(`<div class="errbox ${sc.caught ? 'caught' : ''}"><div class="err-ico">${sc.caught ? '🛡️' : '💥'}</div><code>${esc(sc.err)}</code><div class="err-st">${sc.caught ? L('caught') : L('crash')}</div></div>`, sc.caught ? 'happy' : 'sad');
    case 'search': {
      const ti = sc.items.indexOf(sc.target);
      const id = player(ti + 1, k => { const e = $id(`${id}-${k}`); e.classList.add(k === ti ? 'found' : 'miss'); e.querySelector('em').textContent = k === ti ? '✅' : '❌'; },
        () => sc.items.forEach((_, i) => { const e = $id(`${id}-${i}`); e.classList.remove('found', 'miss'); e.querySelector('em').textContent = '🕳️'; }));
      return wrap(`<div class="row">${sc.items.map((x, i) => `<div class="cell nora" id="${id}-${i}"><small>${i}</small><em>🕳️</em><span>${esc(x)}</span></div>`).join('')}</div><div class="rowlbl">🔎 "${esc(sc.target)}"</div>${ctrl(id)}`, 'think');
    }
    case 'sort': {
      const steps = []; const a = sc.arr.slice();
      for (let i = 0; i < a.length - 1; i++) for (let j = 0; j < a.length - 1 - i; j++) { const sw = a[j] > a[j + 1]; if (sw) [a[j], a[j + 1]] = [a[j + 1], a[j]]; steps.push({ j, sw, arr: a.slice(), fixed: a.length - 1 - i, last: j === a.length - 2 - i }); }
      const max = Math.max(...sc.arr);
      const bars = arr => arr.map(v => `<div class="bar" style="height:${30 + v / max * 90}px"><span>${v}</span><i class="cpy"></i></div>`).join('');
      const id = player(steps.length, k => {
        const s = steps[k]; const el = $id(id + '-bars'); el.innerHTML = bars(s.arr);
        [...el.children].forEach((b, i) => { if (i === s.j || i === s.j + 1) b.classList.add(s.sw ? 'swap' : 'cmp'); if (i > s.fixed || (s.last && i === s.fixed)) b.classList.add('fix'); });
        $id(id + '-msg').textContent = `t[${s.j}] ${s.sw ? '>' : '≤'} t[${s.j + 1}] → ${s.sw ? tr('swap') : tr('noswap')}`;
      }, () => { $id(id + '-bars').innerHTML = bars(sc.arr); $id(id + '-msg').textContent = ''; });
      return `<div class="scene sc-sort"><div class="bars" id="${id}-bars">${bars(sc.arr)}</div><div class="rowlbl" id="${id}-msg"></div>${ctrl(id)}<div class="scene-cap">🐾 ${sc.cap}</div></div>`;
    }
    case 'stack': {
      const n = sc.frames.length;
      const id = player(n * 2, k => {
        if (k < n) $id(`${id}-${k}`).classList.add('open');
        else { const i = 2 * n - 1 - k; const e = $id(`${id}-${i}`); e.classList.add('ret'); if (sc.rets[i]) e.querySelector('em').textContent = '↩ ' + sc.rets[i]; }
      }, () => sc.frames.forEach((_, i) => { const e = $id(`${id}-${i}`); e.classList.remove('open', 'ret'); e.querySelector('em').textContent = ''; }));
      return wrap(`<div class="stack">${sc.frames.map((f, i) => `<div class="frame" id="${id}-${i}" style="margin-left:${i * 14}px"><code>${esc(f)}</code><em></em></div>`).join('')}</div>${ctrl(id)}`, 'think');
    }
  }
  return '';
}
