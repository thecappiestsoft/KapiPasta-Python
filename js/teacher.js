/* ===== Teacher panel ===== */
let T = Object.assign({ pin: null, students: {}, gcfg: null }, lsGet(LST) || {});
const TV = { auth: false, sort: 'xp', dir: -1, filter: '', msg: '', scope: 'all' };
const scopeG = s => TV.scope === 'all' ? s.g : s.chs[+TV.scope];
const tsave = () => lsSet(LST, T);
function openTeacher() { V.view = 'teacher'; V.drawer = false; render(); scrollTop(); }
async function hashPin(p) { return fnv(SALT + 'pin' + p) + fnv(p + SALT); }

function stuDone(o) { const d = {}; for (const id in o.done) { const r = o.done[id]; d[id] = { ok: r[0], first: r[1], tries: r[2], rv: r[3] || 0 }; } return d; }
function stuStats(o) {
  const C = course(), done = stuDone(o), st = o.stage || 1;
  const all = chapTasksOf(C, st);
  const g = gradeOf(done, all, true);
  const chs = C.map(ch => gradeOf(done, chapTasks(ch, st), true));
  let att = 0; for (const id in o.done) if (o.done[id][2] > 0) att++;
  return { n: g.n, d: g.ok, p: g.p, acc: g.ok ? g.first / g.ok : 0, g, chs, lv: levelOf(o.xp).lv, att, time: timeOf(o.time, all), away: o.away || { n: 0, sec: 0 }, done };
}
const chapTasksOf = (C, st) => C.flatMap(ch => chapTasks(ch, st));
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
  const key = { grade: x => scopeG(x.s).grade * 10 + scopeG(x.s).p, time: x => x.s.time, away: x => x.s.away.n, name: x => (x.o.name || '').toLowerCase(), cls: x => x.o.cls || '', stage: x => x.o.stage, lv: x => x.o.xp, xp: x => x.o.xp, prog: x => x.s.p, acc: x => x.s.acc, last: x => x.o.ts }[TV.sort] || (x => x.o.xp);
  list.sort((a, b) => (key(a) > key(b) ? 1 : key(a) < key(b) ? -1 : 0) * TV.dir);
  const avg = f => list.length ? list.reduce((a, x) => a + f(x), 0) / list.length : 0;
  const th = (k, n) => `<th data-act="tsort" data-a="${k}">${n}${TV.sort === k ? (TV.dir < 0 ? ' ▼' : ' ▲') : ''}</th>`;
  // hardest tasks
  const agg = {};
  list.forEach(({ o }) => { for (const id in o.done) { const r = o.done[id]; if (!r[2] && !r[0]) continue; const a = agg[id] || (agg[id] = { att: 0, fail: 0, time: 0 }); a.att++; if (!r[1]) a.fail++; a.time += (o.time || {})[id] || 0; } });
  const tinfo = {}; C.forEach((ch, ci) => ch.lessons.forEach((L, li) => L.tasks.forEach(t => tinfo[t.id] = { t, L, ci, li })));
  const hard = Object.entries(agg).filter(([id, a]) => a.fail > 0 && tinfo[id]).sort((a, b) => b[1].fail / b[1].att - a[1].fail / a[1].att || b[1].fail - a[1].fail).slice(0, 10);
  const strip = s => s.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
  return `<div class="doc" style="max-width:1100px"><div class="crumb"># teacher.py</div>
<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap"><h1 style="flex:1">🧑‍🏫 ${tr('teacher')}</h1><button class="btn sm" data-act="tcsv">${tr('tCsv')}</button><button class="btn sm ghost" data-act="tclear" style="color:var(--bad)">🗑️ ${tr('tClear')}</button><button class="btn sm ghost" data-act="tlogout">🔒 ${tr('tLogout')}</button></div>
<details class="readme" ${TV.cfgOpen ? 'open' : ''}><summary><b>⚙️ ${tr('tCfg')}</b> <span class="muted">${normCfg(T.gcfg).th.join(' / ')}% · 6: ${tr(normCfg(T.gcfg).six === 'ff90' ? 'six90' : 'sixAll')} · ${tr('rvShort')} ${normCfg(T.gcfg).rv} · 🔓 ${normCfg(T.gcfg).unlock.length}</span></summary>
${(() => { const c = normCfg(T.gcfg); return `<p class="muted">${tr('tCfgD')}</p>
<div class="cfggrid">${[2, 3, 4, 5].map((g, i) => `<label>${gradeChip({ grade: g, started: true })} ${tr('gname' + g)} ${tr('from')}<input class="inp" type="number" min="1" max="100" id="tth${i}" value="${c.th[i]}"> %</label>`).join('')}</div>
<label class="lbl">${gradeChip({ grade: 6, started: true })} ${tr('gname6')}</label><select class="inp" id="tsix"><option value="flawless" ${c.six === 'flawless' ? 'selected' : ''}>${tr('lg6')}</option><option value="ff90" ${c.six === 'ff90' ? 'selected' : ''}>${tr('lg6b')}</option></select>
<label class="lbl">${tr('rvLabel')}</label><select class="inp" id="trv">${[[0.5, 'rvHalf'], [0, 'rvZero'], [1, 'rvOne']].map(([v, k]) => `<option value="${v}" ${c.rv === v ? 'selected' : ''}>${tr(k)}</option>`).join('')}</select>
<label class="lbl">🔓 ${tr('tUnlock')}</label><p class="muted" style="font-size:12.5px;margin:0 0 6px">${tr('tUnlockD')}</p>
<div class="cfggrid">${course().slice(1).map(ch => `<label><input type="checkbox" class="tun" value="${ch.id}" ${c.unlock.includes(ch.id) ? 'checked' : ''}> ${ch.icon[S.theme]} ${esc(chName(ch))}</label>`).join('')}</div>
<div class="row-btns"><button class="btn pri" data-act="tcfgsave">${tr('save')}</button><button class="btn ghost" data-act="tcfgdef">${tr('tCfgDef')}</button><button class="btn" data-act="tcfgcode">🏫 ${tr('clsMake')}</button></div>${gradeLegend(c, 1)}${gradeLegend(c, 2)}${gradeLegend(c, 3)}`; })()}</details>
<div class="readme"><h3>📥 ${tr('tImport')}</h3><p class="muted">${tr('tImportD')}</p>
<div class="drop" id="tdrop"><input type="file" id="tfile" accept=".txt,.kapi,text/plain" multiple hidden><button class="btn pri" data-act="pickfile" data-a="tfile">${tr('pickFile')}</button></div>
<textarea class="inp" id="tpaste" placeholder="${tr('pasteCode')}" style="margin-top:8px"></textarea><div class="row-btns"><button class="btn" data-act="tpaste">${tr('load')}</button>${TV.msg ? `<span class="chip acc">${TV.msg}</span>` : ''}</div></div>
${Object.keys(T.students).length ? `
<div class="statgrid"><div class="stat"><div class="l">👩‍🎓 ${tr('tStudents')}</div><div class="v">${list.length}</div></div><div class="stat"><div class="l">💎 ${tr('tAvgXp')}</div><div class="v">${Math.round(avg(x => x.o.xp))}</div></div>
<div class="stat"><div class="l">📈 ${tr('tAvgProg')}</div><div class="v">${Math.round(avg(x => x.s.p) * 100)}%</div></div><div class="stat"><div class="l">🎯 ${tr('tAcc')}</div><div class="v">${Math.round(avg(x => x.s.acc) * 100)}%</div></div><div class="stat"><div class="l">📝 ${tr('tGrade')}</div><div class="v">${avg(x => scopeG(x.s).grade).toFixed(2)}</div></div><div class="stat"><div class="l">⏱ ${tr('tAvgTime')}</div><div class="v">${fmtTime(avg(x => x.s.time))}</div></div></div>
<p class="muted" style="font-size:12.5px">ℹ️ ${tr('tGradeInfo')}</p><details class="readme"><summary>${tr('scale')}</summary>${gradeLegend()}</details>
<div class="row-btns" style="align-items:center"><span class="muted">📝 ${tr('tScope')}:</span><select class="inp" id="tscope" style="width:auto"><option value="all" ${TV.scope === 'all' ? 'selected' : ''}>${tr('tScopeAll')}</option>${C.map((ch, i) => `<option value="${i}" ${TV.scope === String(i) ? 'selected' : ''}>${i + 1}. ${esc(chName(ch))}</option>`).join('')}</select><span class="muted">${tr('tFilter')}:</span><select class="inp" id="tfilter" style="width:auto">${['', ...classes].map(c => `<option value="${esc(c)}" ${TV.filter === c ? 'selected' : ''}>${c ? esc(c) : tr('tAll')}</option>`).join('')}</select></div>
<div class="tscroll"><table class="tbl"><thead><tr>${th('name', tr('tName'))}${th('cls', tr('tClass'))}${th('stage', tr('tStage'))}${th('lv', tr('tLevel'))}${th('xp', 'XP')}${th('prog', tr('tProg'))}${th('acc', tr('tAcc'))}${th('grade', tr('tGrade'))}${th('time', tr('tTime'))}${th('away', tr('tAway'))}<th>${tr('tChapters')}</th>${th('last', tr('tLast'))}<th></th></tr></thead><tbody>
${list.map(({ k, o, s }) => `<tr><td><b>${esc(o.name)}</b></td><td>${esc(o.cls || '—')}</td><td>${['🌱', '🚀', '🏆'][o.stage - 1]}</td><td>${s.lv}</td><td>${o.xp}</td><td><div class="pbar" style="width:70px;display:inline-block;vertical-align:middle"><i style="width:${Math.round(s.p * 100)}%"></i></div> ${Math.round(s.p * 100)}%</td><td>${Math.round(s.acc * 100)}%</td><td>${scopeG(s).started ? starsHtml(scopeG(s)) + gradeChip(scopeG(s)) : '–'}</td><td>${fmtTime(s.time)}</td><td>${s.away.n ? `👀 ${s.away.n} <small class="muted">(${fmtTime(s.away.sec)})</small>` : '0'}</td>
<td>${s.chs.map((g, i) => `<span class="heat ${g.started ? 'g' + g.grade : ''}" style="${g.started ? '' : 'background:var(--line)'}" title="${esc(chName(C[i]))}: ${Math.round(g.p * 100)}%${g.started ? ' → ' + g.grade : ''}">${g.started ? g.grade : i + 1}</span>`).join(' ')}</td><td>${new Date(o.ts).toLocaleDateString()}</td><td><button class="btn sm" data-act="tdet" data-a="${esc(k)}">${tr('tDetails')}</button> <button class="btn sm ghost" data-act="tdel" data-a="${esc(k)}">✕</button></td></tr>`).join('')}
</tbody></table></div>
<h2 style="margin-top:20px">🔥 ${tr('tHard')}</h2><p class="muted">${tr('tHardD')}</p>
${hard.length ? `<div class="projlist">${hard.map(([id, a]) => { const I = tinfo[id]; return `<div class="proj" style="cursor:default"><span class="pi" style="background:${heatColor(1 - a.fail / a.att)}">${{ quiz: '❓', fill: '✍️', bug: '🐞', code: '💻' }[I.t.t]}</span><span style="flex:1;min-width:0"><span class="pn">${esc(strip(I.t.q)).slice(0, 110)}</span><br><span class="pp">${I.ci + 1}.${I.li + 1} ${esc(I.L.title)} · ${tr('tFails', { n: a.fail + '/' + a.att })} · ⏱ ${tr('tAvgTime')} ${fmtTime(a.time / a.att)}</span></span></div>`; }).join('')}</div>` : `<p class="muted">${tr('tNone')}</p>`}
` : `<div class="readme">${capy({ size: 90, mood: 'think' })}<p>${tr('tEmpty')}</p></div>`}</div>`;
}
function studentDetails(k) {
  const o = T.students[k]; if (!o) return; const C = course(); const s = stuStats(o); const st = o.stage || 1;
  const rows = []; C.forEach((ch, ci) => ch.lessons.forEach((L, li) => { const ts = tasksFor(L, st); const g = gradeOf(s.done, ts); const tries = ts.reduce((a, t) => a + (s.done[t.id] ? s.done[t.id].tries : 0), 0); rows.push({ ci, li, L, g, tries, time: timeOf(o.time, ts), aw: (o.awayL || {})[L.id] }); }));
  const weak = rows.filter(r => r.g.started && r.g.grade <= 3).map(r => `${r.ci + 1}.${r.li + 1} ${esc(r.L.title)} ${gradeChip(r.g)}`);
  modal(`<div class="mh">👩‍🎓 ${esc(o.name)} ${o.cls ? '· ' + esc(o.cls) : ''} · ${['🌱', '🚀', '🏆'][st - 1]} ${tr('st' + st)}<button class="btn sm ghost" data-act="close">✕</button></div><div class="mb">
<div class="statgrid"><div class="stat"><div class="l">📝 ${tr('tGrade')}</div><div class="v">${s.g.started ? gradeChip(s.g) + ' ' + starsHtml(s.g) : '–'}</div></div><div class="stat"><div class="l">⭐ ${tr('level')}</div><div class="v">${s.lv}</div></div><div class="stat"><div class="l">💎 XP</div><div class="v">${o.xp}</div></div><div class="stat"><div class="l">✅ ${tr('tasksDone')}</div><div class="v">${s.d}/${s.n}</div></div><div class="stat"><div class="l">🎯 ${tr('accuracy')}</div><div class="v">${Math.round(s.acc * 100)}%</div></div><div class="stat"><div class="l">⏱ ${tr('tTime')}</div><div class="v">${fmtTime(s.time)}</div></div><div class="stat"><div class="l">👀 ${tr('tAway')}</div><div class="v">${s.away.n} <small>(${fmtTime(s.away.sec)})</small></div></div><div class="stat"><div class="l">🔥 ${tr('streak')}</div><div class="v">${o.streak || 0}</div></div></div>
<h3 style="margin-top:14px">📌 ${tr('tWeak')}</h3><p>${weak.length ? weak.join('<br>') : tr('tNone')}</p>
<div class="tscroll"><table class="tbl"><thead><tr><th>#</th><th>${W().les}</th><th>✅</th><th>🎯</th><th>↻</th><th>⭐</th><th>${tr('tGrade')}</th><th>⏱</th><th>👀</th></tr></thead><tbody>${rows.map(r => `<tr><td>${r.ci + 1}.${r.li + 1}</td><td>${esc(r.L.title)}</td><td>${r.g.ok}/${r.g.n}</td><td>${r.g.ok ? Math.round(r.g.first / r.g.ok * 100) + '%' : '—'}</td><td>${r.tries}</td><td>${r.g.started ? starsHtml(r.g) : '–'}</td><td>${gradeChip(r.g) || '–'}</td><td>${r.time ? fmtTime(r.time) : '–'}</td><td>${r.aw && r.aw.n ? `${r.aw.n} (${fmtTime(r.aw.sec)})` : '–'}</td></tr>`).join('')}</tbody></table></div></div>`, 'wide');
}
async function addStudentCodes(texts) {
  let ok = 0, bad = 0;
  for (const tx of texts) {
    const parts = tx.match(/PYKAPI1\.[pz]\.[0-9a-f]{8}\.[A-Za-z0-9_\-\s]+?(?=PYKAPI1\.|$)/g) || [];
    if (!parts.length) { if (tx.trim()) bad++; continue; }
    for (const p of parts) {
      try { const o = await decodeProgress(p); if (o.kind === 'cfg') throw 0; const k = (o.name || '?') + '|' + (o.cls || '') + '|' + (o.created || 0); const old = T.students[k]; if (!old || old.ts <= o.ts) T.students[k] = o; ok++; } catch (e) { bad++; }
    }
  }
  tsave(); TV.msg = tr('tAdded', { n: ok }) + (bad ? ' · ' + tr('tErrors', { n: bad }) : ''); if (ok) beep('ok'); else if (bad) beep('bad');
  renderMain();
}
async function teacherFiles(files) { const texts = []; for (const f of files) texts.push(await f.text()); addStudentCodes(texts); }
function csvExport() {
  const C = course(); const rows = [['name', 'class', 'stage', 'tasks_per_lesson', 'grade', 'stars', 'flawless', 'tasks_done', 'tasks_total', 'progress_%', 'first_try_%', 'time_min', 'left_app_count', 'left_app_min', 'level', 'xp', 'streak', 'badges', 'last_export', ...C.map((ch, i) => `ch${i + 1}_grade`), ...C.map((ch, i) => `ch${i + 1}_%`)]];
  Object.values(T.students).forEach(o => { const s = stuStats(o); rows.push([o.name, o.cls || '', o.stage, [6, 12, 18][(o.stage || 1) - 1], s.g.started ? s.g.grade : '', s.g.stars, s.g.flawless ? 1 : 0, s.d, s.n, Math.round(s.p * 100), Math.round(s.acc * 100), Math.round(s.time / 60), s.away.n, Math.round(s.away.sec / 60), s.lv, o.xp, o.streak || 0, (o.badges || []).length, new Date(o.ts).toISOString().slice(0, 10), ...s.chs.map(g => g.started ? g.grade : ''), ...s.chs.map(g => Math.round(g.p * 100))]); });
  return '\ufeff' + rows.map(r => r.map(v => /[;"\n]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v).join(';')).join('\n');
}
async function teacherAct(act, a, el) {
  switch (act) {
    case 'tsetpin': { const p = document.getElementById('tpin').value.trim(); if (!/^\d{4,12}$/.test(p)) { TV.msg = tr('tPinSet'); renderMain(); return; } T.pin = await hashPin(p); tsave(); TV.auth = true; TV.msg = ''; render(); break; }
    case 'tlogin': { const p = document.getElementById('tpin').value.trim(); if (await hashPin(p) === T.pin) { TV.auth = true; TV.msg = ''; beep('ok'); } else { TV.msg = tr('tPinBad'); beep('bad'); } renderMain(); break; }
    case 'tlogout': TV.auth = false; TV.msg = ''; renderMain(); break;
    case 'tcfgsave': {
      const th = [0, 1, 2, 3].map(i => Math.round(+document.getElementById('tth' + i).value));
      if (!th.every((x, i) => x >= 1 && x <= 100 && (i === 0 || x > th[i - 1]))) { toast('⚠️ ' + tr('tCfgBad')); return; }
      T.gcfg = { th, six: document.getElementById('tsix').value, rv: +document.getElementById('trv').value, unlock: [...document.querySelectorAll('.tun:checked')].map(x => x.value) }; tsave(); TV.cfgOpen = true; toast('✔ ' + tr('saved2')); renderMain(); break; }
    case 'tcfgdef': T.gcfg = null; tsave(); TV.cfgOpen = true; renderMain(); break;
    case 'tcfgcode': { const code = await encodeCfg(T.gcfg); modal(`<div class="mh">🏫 ${tr('clsMake')}<button class="btn sm ghost" data-act="close">✕</button></div><div class="mb"><p class="muted">${tr('clsMakeD')}</p><div class="codeout" id="clsout">${esc(code)}</div><div class="row-btns"><button class="btn pri" data-act="copy" data-src="clsout">${tr('copyCode')}</button></div></div>`); break; }
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
document.addEventListener('change', e => { if (e.target.id === 'tfilter') { TV.filter = e.target.value; renderMain(); } if (e.target.id === 'tscope') { TV.scope = e.target.value; renderMain(); } });
document.addEventListener('dragover', e => { const d = e.target.closest && e.target.closest('#tdrop'); if (d) { e.preventDefault(); d.classList.add('over'); } });
document.addEventListener('dragleave', e => { const d = e.target.closest && e.target.closest('#tdrop'); if (d) d.classList.remove('over'); });
document.addEventListener('drop', e => { const d = e.target.closest && e.target.closest('#tdrop'); if (d) { e.preventDefault(); d.classList.remove('over'); teacherFiles(e.dataTransfer.files); } });
