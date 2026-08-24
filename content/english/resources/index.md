+++
title = "Resources for Researchers"
subtitle = "The hidden curriculum for finance and accounting research — datasets, tools, writing, and workflows."
type = "page"
toc = true
+++

The hidden curriculum — what PhD programs rarely teach but researchers need: writing, presenting, coding, managing projects, and staying current with the literature. This page collects tools and guides I use in my own work on corporate finance and financial accounting.

## On this page

- [My curated tips](#curated-tips)
- [My original guides](#original-guides)
- [Data and databases](#data-databases)
- [Literature and working papers](#literature)
- [Stata, R, and LaTeX workflow](#workflow)
- [Writing, publishing, and refereeing](#writing)
- [Presentations and seminars](#presentations)
- [AI for research](#ai-research)
- [PhD and early-career advice](#phd-advice)
- [Other great resource pages](#other-pages)

## My curated tips {#curated-tips}

**Staying current.** Subscribe to [NBER](https://www.nber.org/papers/) and [SSRN](https://www.ssrn.com/) alerts in corporate finance and accounting. For finance specifically, the [*Insights for Young Researchers in Finance*](https://insight4finance.substack.com/) newsletter is worth following. I also monitor [RePEc](https://ideas.repec.org/) notifications for new working papers on cash holdings, policy uncertainty, and managerial ability.

**Workflow.** Organize each empirical project so you can return to it six months later without frustration: raw data, cleaned data, do-files, and output in separate folders; a README noting data sources and sample construction; and version-controlled code on GitHub. [Asjad Naqvi's Stata workflow guide](https://asjadnaqvi.github.io/stata/) generalizes well to corporate finance papers.

**Talk to junior faculty.** Ask not only about research topics, but about practical matters — how they organize projects, handle referees, choose journals, and split time between research and teaching. Their perspective is often more actionable than senior faculty's.

## My original guides {#original-guides}

- **[NotebookLM paper briefings](/en/#podcasts)** — narrated audio summaries of my publications, starting with [*The Effect of Proximity to Political Power on Corporate Cash Policy*](https://podcasters.spotify.com/pod/show/stathis-magerakis/episodes/Episode-1-The-Effect-of-Proximity-to-Political-Power-on-Corporate-Cash-Policy-e2q8jui) (*Journal of Corporate Finance*, 2023).
- **[Interactive choropleth map](/visualizations/choropleth_map.html)** — animated visualization of US political proximity and corporate cash policy, linked to Magerakis, Pantzalis & Park (2023).

## Data and databases {#data-databases}

### Macro and policy uncertainty

- [FRED — Economic Data](https://fred.stlouisfed.org/)
- [Baker, Bloom and Davis — Policy Uncertainty Index](http://www.policyuncertainty.com/)

### Firm-level finance

- [Kenneth French — Data Library](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
- [Hoberg-Phillips — Text-based Industry Classifications](http://hobergphillips.tuck.dartmouth.edu/)

### Accounting and managerial quality

- [Demerjian, Lev, and McVay — Managerial Ability](http://faculty.washington.edu/pdemerj/data.html)

### Market news

- [Google Finance](https://www.google.com/finance) · [Yahoo Finance](https://finance.yahoo.com/) · [Bloomberg](https://www.bloomberg.com/europe) · [WSJ](https://www.wsj.com/europe)

{{% alert note %}}
**Tip.** Document every Compustat or WRDS merge step in a README before you move on to analysis — future you will thank present you.
{{% /alert %}}

## Literature and working papers {#literature}

- [Google Scholar](https://scholar.google.gr/)
- [SSRN](https://www.ssrn.com/index.cfm/en/)
- [EconLit](https://www.aeaweb.org/econlit/)
- [NBER Working Papers](https://www.nber.org/papers/)
- [RePEc / IDEAS](https://ideas.repec.org/)

## Stata, R, and LaTeX workflow {#workflow}

### Tools

- [Stata](https://www.stata.com/) · [R Project](https://www.r-project.org/) · [LaTeX Project](https://www.latex-project.org/) · [Overleaf](https://www.overleaf.com/) · [Markdown](https://www.markdownguide.org/) · [Mendeley](https://www.mendeley.com/) · [GitHub](https://github.com/)

### Guides

- [Asjad Naqvi — The Stata workflow guide](https://asjadnaqvi.github.io/stata/)
- [Asjad Naqvi — The Stata-to-LaTeX guide](https://asjadnaqvi.github.io/diwave/)
- [Daniel Bischof — Stata figure schemes](https://www.danielbischof.de/stata/)
- [Paul Goldsmith-Pinkham — Best figure page](https://paulgp.github.io/best_figure.html)
- [Jonathan Schwabish — Ten Guidelines for Better Tables](https://www.archives.gov/files/open/pdf/schwabish-ten-guidelines.pdf)
- [Arthur Turell — Coding for Economists](https://aeturrell.com/posts/coding-for-economists/)

{{% alert note %}}
**Tip.** Install the `lean` graph scheme for clean, publication-ready Stata figures.
{{% /alert %}}

## Writing, publishing, and refereeing {#writing}

### Books

- [Marc Bellemare — *Doing Economics*](https://marcfbellemare.com/doing-economics/)
- [Deirdre McCloskey — *Economical Writing*](https://press.uchicago.edu/ucp/books/book/chicago/E/bo6786238.html)
- [Steven Pinker — *The Sense of Style*](https://stevenpinker.com/publications/sense-style-thinking-persons-guide-writing-21st-century)

### Guides and articles

- [John Cochrane — Writing Tips for Ph.D. Students](https://www.johnhcochrane.com/research-all/writing-tips-for-phd-students)
- [Keith Head — The Introduction Formula](https://blogs.ubc.ca/tedhelsbreth/2013/03/25/the-introduction-formula/)
- [Marc Bellemare — How to Write Applied Papers in Economics](https://marcfbellemare.com/wordpress/1289)
- [Marc Bellemare — The Conclusion Formula](https://marcfbellemare.com/wordpress/1080)
- [Alex Edmans — Learnings From 1,000 Rejections](https://alexedmans.com/blog/learnings-from-1000-rejections/)
- [Campbell Harvey — Reflections on Editing the *Journal of Finance*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2141954)
- [Berk, Harvey & Hirshleifer — How to Write an Effective Referee Report](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1692620)
- [James J. Choi — How to Give a Good Paper Discussion](https://jameschoi.org/wp-content/uploads/2016/06/How-to-Give-a-Good-Discussion.pdf)
- [Plamen Nikolov — Referee report template](https://sites.google.com/site/plamennikolov/referee-report-template)

## Presentations and seminars {#presentations}

- [Marc Bellemare — 22 tips for conference and seminar presentations](https://marcfbellemare.com/wordpress/1208)
- [Jon Schwabish — *Better Presentations*](https://policyviz.com/book/)
- [Paul Goldsmith-Pinkham — Beamer tips](https://paulgp.github.io/beamer_tips.pdf)
- [Jesse M. Shapiro — How to give an applied micro talk](https://www.brown.edu/Research/Shapiro/pdfs/applied_micro_slides.pdf)
- [Rachael Meager — Public speaking for academic economists](https://www.rachaelmeager.com/resources)

{{% alert note %}}
**Tip.** Have fellow PhD students take notes during your practice talks and solicit feedback from colleagues before the real seminar.
{{% /alert %}}

## AI for research {#ai-research}

- [My NotebookLM podcasts](/en/#podcasts)
- [Aakash Gupta — Complete Guide to NotebookLM](https://www.product-growth.com/p/the-complete-guide-to-googles-notebooklm)
- [Aniket Panjwani — AI Agents for Economics Research](https://aniketpanjwani.com/blog/ai-agents-for-economics-research/)
- [Benjamin Golub — Modern AI for Economics Research (Princeton)](https://benjamin-golub.github.io/ai-econ/)
- [Claes Bäckman — AI guides for researchers](https://claesbackman.com/ai-guides.html)

## PhD and early-career advice {#phd-advice}

- [Luke Taylor — Tips for Finance Ph.D. students](https://pages.stern.nyu.edu/~ltaylo3/PhDAdvice.html)
- [Chris Brooks — Your PhD in accounting or finance](https://chrisbrooks.org.uk/phd-advice/)
- [Amy Finkelstein — An unofficial guide to trying to do empirical work](https://economics.mit.edu/files/9614)
- [Daniel Hamermesh — The Young Economist's Guide to Professional Etiquette](https://www.aeaweb.org/about-aea/code-of-conduct/young-economist)
- [Claudia Sahm — Economists must build a better community](https://stay-at-home-macro.tidyverse.org/blog.html)

## Other great resource pages {#other-pages}

Pages I have learned from — consider bookmarking these alongside this one:

- [Claes Bäckman — Resources](https://claesbackman.com/resources.html)
- [Masayuki Kudamatsu — Tips for economists](https://www.kudamatsu.com/tips.html)
- [Plamen Nikolov — Resources](https://sites.google.com/site/plamennikolov/resources)
- [Kevin Bryan — Guide to AI, Git, and LaTeX](https://github.com/kb22/AEA-AI-Git-LaTeX)
- [Arthur Turell — Coding for Economists](https://aeturrell.com/posts/coding-for-economists/)
- [Shanjun Li — PhD resources](https://sites.google.com/site/shanjunlihomepage/phd-resources)
- [AEA — Mentoring links](https://www.aeaweb.org/resources/mentoring)

---

Missing something useful? Email me at [smagerakis@upatras.gr](mailto:smagerakis@upatras.gr).
