# Idaho Families Work

Static marketing site for Idaho Families Work, a program of Idaho AEYC.

`index.html` is fully self-contained — brand assets, the Soiren typeface, and all
runtime code are inlined. No build step, no dependencies.

## Deploy

**GitHub Pages** — push to `main`, then Settings → Pages → Source: `main` / root
(or `/site` if the folder is kept nested). The presence of `.nojekyll` keeps Pages
from filtering files.

**Anywhere else** — upload `index.html`. That is the whole site.

## Editing

Do not hand-edit `index.html`; it is compiled. Source of truth is
`Idaho Families Work.dc.html` in the design project — edit there and recompile.

## Outstanding

- Hero and video slots hold placeholders pending final brand photography.
- Event listings are sample entries; wire Register buttons to the external
  registration partner.
- Contact form is not wired to a backend.
