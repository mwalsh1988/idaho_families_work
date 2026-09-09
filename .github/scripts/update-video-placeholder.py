from pathlib import Path

path = Path("idaho_families_work_revised.html")
html = path.read_text(encoding="utf-8")

start = html.index(".video{")
end = html.index(".play:after{", start)

new_css = '''.video{
  position:relative;
  aspect-ratio:16/9;border-radius:6px;overflow:hidden;
  background:
    linear-gradient(rgba(20,42,29,.34),rgba(20,42,29,.34)),
    url("./Modern Workplace Rendering.png") center center / cover no-repeat;
  display:flex;align-items:center;justify-content:center
}
.video:before{
  content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(39,74,124,.04) 0%,rgba(18,48,27,.30) 100%);
  pointer-events:none
}
.play{
  position:relative;z-index:2;
  width:66px;height:66px;border-radius:50%;background:var(--gold);
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 12px 30px rgba(0,0,0,.28)
}
'''

html = html[:start] + new_css + html[end:]
path.write_text(html, encoding="utf-8")
