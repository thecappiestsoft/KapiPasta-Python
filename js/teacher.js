/* ===== Teacher panel ===== */
let T = Object.assign({ pin: null, students: {} }, lsGet(LST) || {});
const TV = { auth: false, sort: 'xp', dir: -1, filter: '', msg: '' };
const tsave = () => lsSet(LST, T);
function openTeacher() { V.view = 'teacher'; V.drawer = false; render(); scrollTop(); }
async function hashPin(p) { return fnv(SALT + 'pin' + p) + fnv(p + SALT); }

function stuStats(o) {
  const C = course(); let n = 0, d = 0, first = 0, att = 0; const chs = [];
  C.forEach(ch => { let cn = 0, cd = 0; ch.lessons.forEach(L => L.tasks.forEach(t => { if (t.l > o.stage) return; cn++; const r = o.done[t.id]; if (r && r[0]) { cd++; if (r[1]) first++; } })); n += cn; d += cd; chs.push(cn ? cd / cn : 0); });
  for (const id in o.done) if (o.done[id][2] > 0) att++;
  const lv = levelOf(o.xp).lv;
  return { n, d, p: n ? d / n : 0, acc: d ? first / d : 0, chs, lv, att };
}
function heatColor(p) { if (p <= 0) return 'var(--line)'; const h = Math.round(p * 120); return `hsl(${h} 65% 45%)`; }
function teacherView() {
  if (!T.pin) return `<div class="doc"><div class="crumb"># teacher.py</div><div class="hero">${capy({ size: 120, mood: 'think' })}<div><h1>🧑‍🏫 ${tr('teacher')}</h1><p class="muted">${tr('tPinSet')}</p></div></div>
<div class="readme" style="max-width:360px"><input class="inp" id="tpin" type="password" inputmode="numeric" maxlength="12" placeholder="••••"><div class="row-btns"><button class="btn pri" data-act="tsetpin">${tr('save')}</button></div>${TV.msg ? `<div class="pybox e">${TV.msg}</div>` : ''}</div></div>`;
  if (!TV.auth) return `<div class="doc"><div class="crumb"># teacher.py</div><div class="hero">${capy({ size: 120, mood: 'think' })}<div><h1>🧑‍🏫 ${tr('teacher')}</h1><p class="muted">${tr('tPin')}</p></div></div>
<div class="readme" style="max-width:360px"><input class="inp" id="tpin" type="password" inputmode="numeric" maxlength="12" placeholder="••••"><div class="row-btns"><button class="btn pri" data-act="tlogin">${tr('tEnter')}</button></div>${TV.msg ? `<div class="pybox e">${TV.msg}</div>` : ''}</div></div>`;
  const C = course();
  let list = Object.entries(T.students).map(([k, o]) => ({ k, o, s: stuStats(o) }));
  const classes = [...new Set(list.map(x => x.o.cls || '—'))].sort();
  if (TV.filter) list = list.filter(x => (x.o.cls || '—') === TV.filter);
  const key = { name: x => (x.o.name || '').toLowerCase(), cls: x => x.o.cls || '', stage: x => x.o.stage, lv: x => x.o.xp, xp: x => x.o.xp, prog: x => x.s.p, acc: x => x.s.acc, last: x => x.o.ts }[TV.sort] || (x => x.o.xp);
  list.sort((a, b) => (key(a) > key(b) ? 1 : key(a) < key(b) ? -1 : 0) * TV.dir);
  const avg = f => list.length ? list.reduce((a, x) => a + f(x), 0) / list.length : 0;
  const th = (k, n) => `<th data-act="tsort" data-a="${k}">${n}${TV.sort === k ? (TV.dir < 0 ? ' ▼' : ' ▲') : ''}</th>`;
  // hardest tasks
  const agg = {};
  list.forEach(({ o }) => { for (const id in o.done) { const r = o.done[id]; if (!r[2] && !r[0]) continue; const a = agg[id] || (agg[id] = { att: 0, fail: 0 }); a.att++; if (!r[1]) a.fail++; } });
  const tinfo = {}; C.forEach((ch, ci) => ch.lessons.forEach((L, li) => L.tasks.forEach(t => tinfo[t.id] = { t, L, ci, li })));
  const hard = Object.entries(agg).filter(([id, a]) => a.fail > 0 && tinfo[id]).sort((a, b) => b[1].fail / b[1].att - a[1].fail / a[1].att || b[1].fail - a[1].fail).slice(0, 10);
  const strip = s => s.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  return `<div class="doc" style="max-width:1100px"><div class="crumb"># teacher.py</div>
<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap"><h1 style="flex:1">🧑‍🏫 ${tr('teacher')}</h1><button class="btn sm" data-act="tcsv">${tr('tCsv')}</button><button class="btn sm ghost" data-act="tclear" style="color:var(--bad)">🗑️ ${tr('tClear')}</button><button class="btn sm ghost" data-act="tlogout">🔒 ${tr('tLogout')}</button></div>
<div class="readme"><h3>📥 ${tr('tImport')}</h3><p class="muted">${tr('tImportD')}</p>
<div class="drop" id="tdrop"><input type="file" id="tfile" accept=".txt,.kapi,text/plain" multiple hidden><button class="btn pri" data-act="pickfile" data-a="tfile">${tr('pickFile')}</button></div>
<textarea class="inp" id="tpaste" placeholder="${tr('pasteCode')}" style="margin-top:8px"></textarea><div class="row-btns"><button class="btn" data-act="tpaste">${tr('load')}</button>${TV.msg ? `<span class="chip acc">${TV.msg}</span>` : ''}</div></div>
${Object.keys(T.students).length ? `
<div class="statgrid"><div class="stat"><div class="l">👩‍🎓 ${tr('tStudents')}</div><div class="v">${list.length}</div></div><div class="stat"><div class="l">💎 ${tr('tAvgXp')}</div><div class="v">${Math.round(avg(x => x.o.xp))}</div></div>
<div class="stat"><div class="l">📈 ${tr('tAvgProg')}</div><div class="v">${Math.round(avg(x => x.s.p) * 100)}%</div></div><div class="stat"><div class="l">🎯 ${tr('tAcc')}</div><div class="v">${Math.round(avg(x => x.s.acc) * 100)}%</div></div></div>
<div class="row-btns" style="align-items:center"><span class="muted">${tr('tFilter')}:</span><select class="inp" id="tfilter" style="width:auto">${['', ...classes].map(c => `<option value="${esc(c)}" ${TV.filter === c ? 'selected' : ''}>${c ? esc(c) : tr('tAll')}</option>`).join('')}</select></div>
<div class="tscroll"><table class="tbl"><thead><tr>${th('name', tr('tName'))}${th('cls', tr('tClass'))}${th('stage', tr('tStage'))}${th('lv', tr('tLevel'))}${th('xp', 'XP')}${th('prog', tr('tProg'))}${th('acc', tr('tAcc'))}<th>${tr('tChapters')}</th>${th('last', tr('tLast'))}<th></th></tr></thead><tbody>
${list.map(({ k, o, s }) => `<tr><td><b>${esc(o.name)}</b></td><td>${esc(o.cls || '—')}</td><td>${['🌱', '🚀', '🏆'][o.stage - 1]}</td><td>${s.lv}</td><td>${o.xp}</td><td><div class="pbar" style="width:70px;display:inline-block;vertical-align:middle"><i style="width:${Math.round(s.p * 100)}%"></i></div> ${Math.round(s.p * 100)}%</td><td>${Math.round(s.acc * 100)}%</td>
<td>${s.chs.map((p, i) => `<span class="heat" style="background:${heatColor(p)}" title="${esc(chName(C[i]))}: ${Math.round(p * 100)}%">${i + 1}</span>`).join(' ')}</td><td>${new Date(o.ts).toLocaleDateString()}</td><td><button class="btn sm" data-act="tdet" data-a="${esc(k)}">${tr('tDetails')}</button> <button class="btn sm ghost" data-act="tdel" data-a="${esc(k)}">✕</button></td></tr>`).join('')}
</tbody></table></div>
<h2 style="margin-top:20px">🔥 ${tr('tHard')}</h2><p class="muted">${tr('tHardD')}</p>
${hard.length ? `<div class="projlist">${hard.map(([id, a]) => { const I = tinfo[id]; return `<div class="proj" style="cursor:default"><span class="pi" style="background:${heatColor(1 - a.fail / a.att)}">${{ quiz: '❓', fill: '✍️', bug: '🐞', code: '💻' }[I.t.t]}</span><span style="flex:1;min-width:0"><span class="pn">${esc(strip(I.t.q)).slice(0, 110)}</span><br><span class="pp">${I.ci + 1}.${I.li + 1} ${esc(I.L.title)} · ${tr('tFails', { n: a.fail + '/' + a.att })}</span></span></div>`; }).join('')}</div>` : `<p class="muted">${tr('tNone')}</p>`}
` : `<div class="readme">${capy({ size: 90, mood: 'think' })}<p>${tr('tEmpty')}</p></div>`}</div>`;
}
function studentDetails(k) {
  const o = T.students[k]; if (!o) return; const C = course(); const s = stuStats(o);
  const rows = []; C.forEach((ch, ci) => ch.lessons.forEach((L, li) => { const ts = L.tasks.filter(t => t.l <= o.stage); const d = ts.filter(t => o.done[t.id] && o.done[t.id][0]).length; const f = ts.filter(t => o.done[t.id] && o.done[t.id][1]).length; const tries = ts.reduce((a, t) => a + (o.done[t.id] ? o.done[t.id][2] : 0), 0); rows.push({ ci, li, L, n: ts.length, d, f, tries, st: (o.stars || {})[L.id] || 0 }); }));
  const weak = rows.filter(r => r.d > 0 && r.f / Math.max(r.d, 1) < .6).map(r => `${r.ci + 1}.${r.li + 1} ${esc(r.L.title)}`);
  modal(`<div class="mh">👩‍🎓 ${esc(o.name)} ${o.cls ? '· ' + esc(o.cls) : ''}<button class="btn sm ghost" data-act="close">✕</button></div><div class="mb">
<div class="statgrid"><div class="stat"><div class="l">⭐ ${tr('level')}</div><div class="v">${s.lv}</div></div><div class="stat"><div class="l">💎 XP</div><div class="v">${o.xp}</div></div><div class="stat"><div class="l">✅ ${tr('tasksDone')}</div><div class="v">${s.d}/${s.n}</div></div><div class="stat"><div class="l">🎯 ${tr('accuracy')}</div><div class="v">${Math.round(s.acc * 100)}%</div></div><div class="stat"><div class="l">🔥 ${tr('streak')}</div><div class="v">${o.streak || 0}</div></div><div class="stat"><div class="l">🏅 ${tr('badges')}</div><div class="v">${(o.badges || []).length}</div></div></div>
<h3 style="margin-top:14px">📌 ${tr('tWeak')}</h3><p>${weak.length ? weak.join('<br>') : tr('tNone')}</p>
<div class="tscroll"><table class="tbl"><thead><tr><th>#</th><th>${W().les}</th><th>✅</th><th>🎯</th><th>↻</th><th>⭐</th></tr></thead><tbody>${rows.map(r => `<tr><td>${r.ci + 1}.${r.li + 1}</td><td>${esc(r.L.title)}</td><td>${r.d}/${r.n}</td><td>${r.d ? Math.round(r.f / r.d * 100) + '%' : '—'}</td><td>${r.tries}</td><td>${'⭐'.repeat(r.st)}</td></tr>`).join('')}</tbody></table></div></div>`, 'wide');
}
async function addStudentCodes(texts) {
  let ok = 0, bad = 0;
  for (const tx of texts) {
    const parts = tx.match(/PYKAPI1\.[pz]\.[0-9a-f]{8}\.[A-Za-z0-9_\-\s]+?(?=PYKAPI1\.|$)/g) || [];
    if (!parts.length) { if (tx.trim()) bad++; continue; }
    for (const p of parts) {
      try { const o = await decodeProgress(p); const k = (o.name || '?') + '|' + (o.cls || '') + '|' + (o.created || 0); const old = T.students[k]; if (!old || old.ts <= o.ts) T.students[k] = o; ok++; } catch (e) { bad++; }
    }
  }
  tsave(); TV.msg = tr('tAdded', { n: ok }) + (bad ? ' · ' + tr('tErrors', { n: bad }) : ''); if (ok) beep('ok'); else if (bad) beep('bad');
  renderMain();
}
async function teacherFiles(files) { const texts = []; for (const f of files) texts.push(await f.text()); addStudentCodes(texts); }
function csvExport() {
  const C = course(); const rows = [['name', 'class', 'stage', 'level', 'xp', 'tasks_done', 'tasks_total', 'progress_%', 'first_try_%', 'streak', 'badges', 'last_export', ...C.map((ch, i) => `ch${i + 1}_%`)]];
  Object.values(T.students).forEach(o => { const s = stuStats(o); rows.push([o.name, o.cls || '', o.stage, s.lv, o.xp, s.d, s.n, Math.round(s.p * 100), Math.round(s.acc * 100), o.streak || 0, (o.badges || []).length, new Date(o.ts).toISOString().slice(0, 10), ...s.chs.map(p => Math.round(p * 100))]); });
  return '﻿' + rows.map(r => r.map(v => /[;"\n]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v).join(';')).join('\n');
}
async function teacherAct(act, a, el) {
  switch (act) {
    case 'tsetpin': { const p = document.getElementById('tpin').value.trim(); if (!/^\d{4,12}$/.test(p)) { TV.msg = tr('tPinSet'); renderMain(); return; } T.pin = await hashPin(p); tsave(); TV.auth = true; TV.msg = ''; render(); break; }
    case 'tlogin': { const p = document.getElementById('tpin').value.trim(); if (await hashPin(p) === T.pin) { TV.auth = true; TV.msg = ''; beep('ok'); } else { TV.msg = tr('tPinBad'); beep('bad'); } renderMain(); break; }
    case 'tlogout': TV.auth = false; TV.msg = ''; renderMain(); break;
    case 'tsort': if (TV.sort === a) TV.dir *= -1; else { TV.sort = a; TV.dir = -1; } renderMain(); break;
    case 'tdet': studentDetails(a); break;
    case 'tdel': delete T.students[a]; tsave(); renderMain(); break;
    case 'tclear': confirmBox(tr('tClearQ'), () => { T.students = {}; tsave(); renderMain(); }); break;
    case 'tpaste': addStudentCodes([document.getElementById('tpaste').value]); break;
    case 'tcsv': {
      const csv = csvExport();
      if (canSave()) { try { await saveFile(`kapipasta-klasa-${todayStr()}.csv`, csv, 'text/csv'); toast('✔ ' + tr('saved')); return; } catch (e) { if (e && e.code === 'declined') return; } }
      modal(`<div class="mh">${tr('tCsv')}<button class="btn sm ghost" data-act="close">✕</button></div><div class="mb"><p class="muted">${tr('dlNo')}</p><div class="codeout" id="csvout" style="white-space:pre;max-height:300px">${esc(csv)}</div><div class="row-btns"><button class="btn pri" data-act="copy" data-src="csvout">${tr('copyCode')}</button></div></div>`);
      break; }
  }
}
document.addEventListener('change', e => { if (e.target.id === 'tfilter') { TV.filter = e.target.value; renderMain(); } });
document.addEventListener('dragover', e => { const d = e.target.closest && e.target.closest('#tdrop'); if (d) { e.preventDefault(); d.classList.add('over'); } });
document.addEventListener('dragleave', e => { const d = e.target.closest && e.target.closest('#tdrop'); if (d) d.classList.remove('over'); });
document.addEventListener('drop', e => { const d = e.target.closest && e.target.closest('#tdrop'); if (d) { e.preventDefault(); d.classList.remove('over'); teacherFiles(e.dataTransfer.files); } });
