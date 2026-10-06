'use strict';
// Preserve the corresponding section when switching a translated article.
for (const link of document.querySelectorAll('[data-language-switch]')) {
  link.addEventListener('click', () => { if (location.hash) link.hash = location.hash; });
}
const form = document.querySelector('.search-form');
if (form) {
  const input = document.querySelector('#query');
  const language = document.querySelector('#language-filter');
  const kind = document.querySelector('#kind-filter');
  const status = document.querySelector('#search-status');
  const results = document.querySelector('#search-results');
  const params = new URLSearchParams(location.search);
  input.value = params.get('q') || '';
  if (['en', 'zh', 'all'].includes(params.get('lang'))) language.value = params.get('lang');
  if (['guide', 'term', 'all'].includes(params.get('kind'))) kind.value = params.get('kind');
  let index = null;
  const normalize = s => s.normalize('NFKC').toLocaleLowerCase();
  function render(updateURL = true) {
    if (!index) return;
    const query = normalize(input.value.trim());
    const terms = query.split(/\s+/u).filter(Boolean);
    const matches = index.filter(a => language.value === 'all' || a.lang === language.value)
      .filter(a => kind.value === 'all' || a.kind === kind.value)
      .map(a => ({a, haystack: normalize(a.title + ' ' + a.summary + ' ' + a.text)}))
      .filter(({haystack}) => terms.every(t => haystack.includes(t)))
      .map(({a}) => ({a, exactTitle: normalize(a.title) === query, score: terms.reduce((n,t) => n + (normalize(a.title).includes(t) ? 10 : 0) + (normalize(a.summary).includes(t) ? 3 : 0),0)}))
      .sort((a,b) => Number(b.exactTitle)-Number(a.exactTitle) || b.score-a.score);
    results.replaceChildren();
    for (const {a} of matches) {
      const item = document.createElement('li');
      const tag = document.createElement('small'); tag.textContent = (a.kind === 'term' ? 'Term' : 'Guide') + ' · ' + a.group + ' · ' + a.lang.toUpperCase();
      const heading = document.createElement('div');
      const link = document.createElement('a'); link.href = a.url; link.textContent = a.title; link.lang = a.lang;
      heading.append(link);
      const text = document.createElement('p'); text.textContent = a.summary; text.lang = a.lang;
      item.append(tag,heading,text); results.append(item);
    }
    status.textContent = matches.length ? `${matches.length} article${matches.length === 1 ? '' : 's'}${query ? ' found' : ' — enter a term to filter'}.` : 'No articles found. Try a broader term or another article language.';
    if (updateURL) {
      const p = new URLSearchParams();
      if (input.value.trim()) p.set('q',input.value.trim());
      if (language.value !== 'en') p.set('lang',language.value);
      if (kind.value !== 'all') p.set('kind',kind.value);
      history.replaceState(null,'',location.pathname+(p.size ? '?'+p : ''));
    }
  }
  form.addEventListener('submit', e => { e.preventDefault(); render(); });
  input.addEventListener('input', () => render()); language.addEventListener('change', () => render());
  kind.addEventListener('change', () => render());
  fetch('/assets/search-index.json').then(r => {if (!r.ok) throw new Error('Index unavailable'); return r.json();})
    .then(data => {index=data;render(false);})
    .catch(() => {status.textContent='Search is temporarily unavailable. Browse Guides or Terminology from the navigation above.';});
}
