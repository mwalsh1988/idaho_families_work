from pathlib import Path

path = Path('idaho_families_work_revised.html')
html = path.read_text(encoding='utf-8')

pillar_css = '''
.pillar-list{display:flex;flex-direction:column;gap:20px}
.pillar-card{
  background:#fff;border:1px solid var(--line);border-radius:6px;overflow:hidden
}
.pillar-header{padding:26px 30px 20px}
.pillar-header h3{font-size:30px}
.pillar-grid{
  display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line)
}
.pillar-detail{padding:24px 30px 28px}
.pillar-detail+.pillar-detail{border-left:1px solid var(--line)}
.pillar-label{
  display:block;margin-bottom:10px;
  font-family:"IBM Plex Mono",monospace;
  font-size:10px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--gold)
}
.pillar-detail p{font-size:16px;color:var(--body)}
@media(max-width:850px){
  .pillar-grid{grid-template-columns:1fr}
  .pillar-detail+.pillar-detail{border-left:0;border-top:1px solid var(--line)}
}

'''

if '.pillar-list{' not in html:
    anchor = '.models{background:var(--wash)}'
    if anchor not in html:
        raise SystemExit('CSS insertion anchor not found')
    html = html.replace(anchor, pillar_css + anchor, 1)

new_section = '''<section class="pillars" id="first-steps">
  <div class="container">
    <div class="section-head">
      <div class="copy">
        <span class="eyebrow">The Four Pillars</span>
        <h2>Start with minimal financial investment.</h2>
        <p>You cannot solve every challenge for every family. You can take sensible steps to remove friction and keep your people showing up and growing.</p>
      </div>
    </div>

    <div class="pillar-list">
      <article class="pillar-card">
        <div class="pillar-header"><h3>Flexibility</h3></div>
        <div class="pillar-grid">
          <div class="pillar-detail">
            <span class="pillar-label">What It Is</span>
            <p>Give employees reasonable ways to adjust when and how work gets done where operations allow.</p>
          </div>
          <div class="pillar-detail">
            <span class="pillar-label">Why It Works</span>
            <p>Family needs do not always follow a fixed schedule. Practical flexibility can keep a short-term disruption from becoming a missed shift, absence or reason to leave.</p>
          </div>
          <div class="pillar-detail">
            <span class="pillar-label">How To Try It</span>
            <p>Test one change for 30 days, such as flexible start times, easier shift swaps or limited scheduling flexibility during high-need periods.</p>
          </div>
        </div>
      </article>

      <article class="pillar-card">
        <div class="pillar-header"><h3>Predictability</h3></div>
        <div class="pillar-grid">
          <div class="pillar-detail">
            <span class="pillar-label">What It Is</span>
            <p>Give employees enough advance notice and consistency in their schedules to plan child care and other family responsibilities.</p>
          </div>
          <div class="pillar-detail">
            <span class="pillar-label">Why It Works</span>
            <p>Reliable schedules make reliable care easier to arrange. Fewer last-minute changes can reduce callouts, late arrivals and scrambling for coverage.</p>
          </div>
          <div class="pillar-detail">
            <span class="pillar-label">How To Try It</span>
            <p>Post schedules earlier, limit avoidable last-minute changes or identify one team where hours can be made more consistent for 30 days.</p>
          </div>
        </div>
      </article>

      <article class="pillar-card">
        <div class="pillar-header"><h3>Supportive Culture</h3></div>
        <div class="pillar-grid">
          <div class="pillar-detail">
            <span class="pillar-label">What It Is</span>
            <p>Equip managers to respond consistently and constructively when employees face family-related disruptions.</p>
          </div>
          <div class="pillar-detail">
            <span class="pillar-label">Why It Works</span>
            <p>A supervisor's response can determine whether a temporary problem gets solved quickly or becomes a source of disengagement, absenteeism or turnover.</p>
          </div>
          <div class="pillar-detail">
            <span class="pillar-label">How To Try It</span>
            <p>Give managers a simple decision tree, clear escalation options and examples of reasonable responses they can use when family needs affect work.</p>
          </div>
        </div>
      </article>

      <article class="pillar-card">
        <div class="pillar-header"><h3>Resource Connection</h3></div>
        <div class="pillar-grid">
          <div class="pillar-detail">
            <span class="pillar-label">What It Is</span>
            <p>Make existing child care, family and community resources easy for employees to find and use.</p>
          </div>
          <div class="pillar-detail">
            <span class="pillar-label">Why It Works</span>
            <p>Employers do not need to build every solution themselves. Connecting employees to trusted resources can solve problems sooner with little or no direct employer cost.</p>
          </div>
          <div class="pillar-detail">
            <span class="pillar-label">How To Try It</span>
            <p>Create one easy-to-find family resources page or guide and make sure managers know where to direct employees when a need comes up.</p>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

'''

start = html.index('<section class="pillars"')
end = html.index('<section class="models"', start)
html = html[:start] + new_section + html[end:]
path.write_text(html, encoding='utf-8')
