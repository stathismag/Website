+++
# A Projects section created with the Portfolio widget.
widget = "portfolio"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 80  # Order that this section will appear.

title = "Resources"
subtitle = ""

[content]
  # Page type to display. E.g. project.
  page_type = "project"
  
  # Filter toolbar (optional).
  # Add or remove as many filters (`[[content.filter_button]]` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove toolbar, delete/comment all instances of `[[content.filter_button]]` below.
  
  # Default filter index (e.g. 0 corresponds to the first `[[filter_button]]` instance below).
  filter_default = 0
  
  # [[content.filter_button]]
  #   name = "All"
  #   tag = "*"
  
  # [[content.filter_button]]
  #   name = "Deep Learning"
  #   tag = "Deep Learning"
  
  # [[content.filter_button]]
  #   name = "Other"
  #   tag = "Demo"

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "2"

  # Toggle between the various page layout types.
  #   1 = List
  #   3 = Card
  #   5 = Showcase
  view = 3

  # For Showcase view, flip alternate rows?
  flip_alt_rows = false

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.
  
  # Background color.
  # color = "navy"
  
  # Background gradient.
  # gradient_start = "DeepSkyBlue"
  # gradient_end = "SkyBlue"
  
  # Background image.
  # image = "background.jpg"  # Name of image in `static/img/`.
  # image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  # text_color_light = true  
  
[advanced]
 # Custom CSS. 
 css_style = ""
 
 # CSS class.
 css_class = ""
+++
<div class="resources-callout">

**My work**

- [Podcasts](#podcasts) — AI-narrated audio summaries of my published papers.
- [Choropleth map](/visualizations/choropleth_map.html) — interactive map of US political proximity and corporate cash policy (Magerakis, Pantzalis & Park, 2023).

</div>

<details class="res-group"><summary>Literature <span class="res-count">(5)</span></summary>

- [Google Scholar](https://scholar.google.gr/) — search academic papers and follow citations.
- [SSRN](https://www.ssrn.com/index.cfm/en/) — working papers and preprints, especially strong in finance and accounting.
- [EconLit](https://www.aeaweb.org/econlit/) — the American Economic Association's index of economics research.
- [NBER](https://www.nber.org/papers/) — working papers from the National Bureau of Economic Research.
- [RePEc](https://ideas.repec.org/) — open database of economics working papers, articles and author profiles.

</details>

<details class="res-group"><summary>Staying current <span class="res-count">(3)</span></summary>

- [NBER email alerts](https://www.nber.org/prefs_front.html) — weekly emails with new NBER working papers in the programs you choose.
- [RePEc NEP reports](http://nep.repec.org/) — subject alerts for new working papers, including corporate finance and accounting.
- [Insights for Young Researchers in Finance](https://www.iwh-halle.de/ueber-das-iwh/forschungsabteilungen/insights-for-young-researchers-in-finance/) — IWH Halle series aimed at early-career finance researchers.

</details>

<details class="res-group"><summary>Financial data <span class="res-count">(5)</span></summary>

- [FRED](https://fred.stlouisfed.org/) — macroeconomic and financial time series from the Federal Reserve Bank of St. Louis.
- [Fama/French](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) — factor returns and portfolio data from Kenneth French's data library.
- [Hoberg-Phillips](http://hobergphillips.tuck.dartmouth.edu/) — text-based industry classifications and product-market competition measures.
- [Policy Uncertainty Index](http://www.policyuncertainty.com/) — Baker, Bloom and Davis's economic policy uncertainty indices.
- [Managerial Ability](https://sites.google.com/view/peterdemerjian/data) — Demerjian, Lev and McVay's managerial ability scores.

</details>

<details class="res-group"><summary>Programming and tools <span class="res-count">(7)</span></summary>

- [Stata](https://www.stata.com/) — statistical software for empirical research.
- [R](https://www.r-project.org/) — free language for statistics and graphics.
- [LaTeX](https://www.latex-project.org/) — typesetting system for academic papers.
- [Overleaf](https://www.overleaf.com/) — online LaTeX editor for writing with coauthors.
- [Markdown](https://www.markdownguide.org/) — guide to the lightweight syntax for formatted text.
- [Mendeley](https://www.mendeley.com/) — reference manager for organising papers and citations.
- [GitHub](https://github.com/) — version control and code sharing.

</details>

<details class="res-group"><summary>Workflow, tables and graphs <span class="res-count">(6)</span></summary>

- [Naqvi — The Stata workflow guide](https://medium.com/the-stata-guide/the-stata-workflow-guide-52418ce35006) — organise a Stata project so you can pick it up again months later.
- [Gentzkow & Shapiro — Code and data for the social sciences](https://www.brown.edu/Research/Shapiro/pdfs/CodeAndData.pdf) — practical rules for keeping empirical code and data reproducible.
- [Stein — Stata output for LaTeX](https://lukestein.github.io/stata-latex-workflows/) — ways to move regression tables from Stata to LaTeX, with a gallery of examples.
- [Schwabish — Ten guidelines for better tables](https://www.cambridge.org/core/journals/journal-of-benefit-cost-analysis/article/ten-guidelines-for-better-tables/74C6FD9FEB12038A52A95B9FBCA05A12) — short, evidence-based advice on designing readable tables.
- [Naqvi — Stata graph tips for academic articles](https://medium.com/the-stata-guide/stata-graph-tips-for-academic-articles-8d962d5e8b75) — settings that make Stata figures publication-ready.
- [Goldsmith-Pinkham — Best figures](https://paulgp.github.io/best_figures.html) — a collection of well-designed figures from economics papers.

</details>

<details class="res-group"><summary>AI for research <span class="res-count">(10)</span></summary>

- [Bäckman — AI guides for academic economists](https://claesbackman.com/ai-guides.html) — practical guides to Claude Code and Codex for empirical research, including a 28-page PDF guide.
- [Sant'Anna — My Claude Code setup](https://psantanna.com/claude-code-my-workflow/) — Pedro Sant'Anna's Claude Code workflow for research projects.
- [Goldsmith-Pinkham — Getting started with Claude Code](https://paulgp.substack.com/p/getting-started-with-claude-code) — a step-by-step introduction for researchers.
- [Goldsmith-Pinkham — From EDGAR filings to a structured database](https://paulgp.substack.com/p/from-edgar-filings-to-a-structured) — using Claude Code to turn SEC filings into research data.
- [Golub — Modern AI for economics research](https://bcf.princeton.edu/events/benjamin-golub-on-modern-ai-for-economics-research-an-overview-of-tools/) — Benjamin Golub's overview of AI tools for economists (Princeton).
- [Cunningham — Claude Code, faculty adoption and security risks](https://causalinf.substack.com/p/claude-code-21-faculty-adoption-of) — Scott Cunningham on how faculty use Claude Code and what can go wrong.
- [Thinking with Agents](https://thinkingwithagents.github.io/) — Aslim and Beam's bootcamp on AI tools for teaching and research.
- [Black — An AI-assisted research flow](https://black-jl.github.io/Research-Project-Flow/) — Jared Black's template for running a research project with AI.
- [Bryan — Guide to AI, Git and LaTeX](https://kevinbryanecon.com/techstack.html) — Kevin Bryan's research tech stack.
- [Guide to NotebookLM](https://www.news.aakashg.com/p/complete-guide-to-notebooklm) — Aakash Gupta's complete guide to Google's NotebookLM, the tool behind my podcasts.

</details>

<details class="res-group"><summary>Claude Code skills for research <span class="res-count">(3)</span></summary>

- [Bäckman — Automated paper feedback](https://github.com/claesbackman/AI-research-feedback) — a skill that reviews a draft paper and returns structured feedback.
- [Hirshleifer — Academic presentations skill](https://github.com/Gabberflast/academic-pptx-skill) — turns a paper into an academic slide deck.
- [Lopez-Lira — Research idea evaluation pipeline](https://github.com/alejandroll10/idea-evaluation-pipeline) — a pipeline for stress-testing new research ideas.

</details>

<details class="res-group"><summary>Writing <span class="res-count">(6)</span></summary>

- [Cochrane — writing tips](https://static1.squarespace.com/static/5e6033a4ea02d801f37e15bb/t/5eda74919c44fa5f87452697/1591374993570/phd_paper_writing.pdf) — John Cochrane's classic advice for PhD students on writing a paper.
- [Head — introduction formula](http://blogs.ubc.ca/khead/research/research-advice/formula) — Keith Head's recipe for structuring an introduction.
- [Bellemare — applied papers](http://marcfbellemare.com/wordpress/wp-content/uploads/2020/09/BellemareHowToPaperSeptember2020.pdf) — Marc Bellemare's guide to writing applied economics papers.
- [Bellemare — The conclusion formula](https://marcfbellemare.com/wordpress/12060) — the companion to the introduction formula, for ending a paper well.
- [Nikolov — Writing tips for economics research papers](https://docs.iza.org/dp16276.pdf) — an IZA discussion paper collecting practical writing advice.
- [McCloskey — Economical Writing (summary)](https://www.deirdremccloskey.com/docs/pdf/Article_309.pdf) — the key rules from the classic short book on clear economic prose.

</details>

<details class="res-group"><summary>Publishing, refereeing and discussing <span class="res-count">(4)</span></summary>

- [Edmans — Learnings from 1,000 rejections](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4336383) — how to handle rejection and improve the next submission.
- [Harvey — Reflections on editing the Journal of Finance](https://faculty.fuqua.duke.edu/~charvey/Research/Working_Papers/W111_Reflections_on_editing.pdf) — an editor's view of what gets published in finance.
- [Berk, Harvey & Hirshleifer — How to write an effective referee report](https://www.aeaweb.org/articles?id=10.1257/jep.31.1.231) — guidance on writing useful, fair referee reports.
- [Choi — How to give a good paper discussion](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4223908) — how to structure a conference discussion.

</details>

<details class="res-group"><summary>Presentations <span class="res-count">(3)</span></summary>

- [Shapiro — How to give an applied micro talk](https://www.brown.edu/Research/Shapiro/pdfs/applied_micro_slides.pdf) — slides on structuring an empirical seminar talk.
- [Fu — How to make effective slides](https://fuzhiyu.me/blogs/slide_design_guide/slide_deck_design.pdf) — a slide-design guide for academic talks.
- [Goldsmith-Pinkham — Beamer tips](https://paulgp.github.io/beamer_tips.html) — making cleaner slides in LaTeX Beamer.

</details>

<details class="res-group"><summary>Research life and productivity <span class="res-count">(3)</span></summary>

- [Pedersen — How to succeed in academia](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3972340) — candid career advice from a finance professor.
- [Brooks — Your PhD in accounting or finance](https://www.amazon.com/Your-PhD-accounting-finance-Produce-ebook/dp/B09HXS6MY8/) — a guide to doctoral research written for accounting and finance.
- [Newport — Study Hacks blog](http://calnewport.com/blog/) — on focused, deep work in a world of email and meetings.

</details>

<details class="res-group"><summary>Teaching <span class="res-count">(2)</span></summary>

- [EEA Education Committee](https://www.eeassoc.org/committees/education-committee) — the European Economic Association's resources for teaching economics.
- [Gioia — My 10 rules for public speaking](https://tedgioia.substack.com/p/my-10-rules-for-public-speaking) — short, practical advice that also works in the lecture hall.

</details>

<details class="res-group"><summary>Finance news <span class="res-count">(4)</span></summary>

- [Google Finance](https://www.google.com/finance) — stock quotes and market news.
- [Yahoo Finance](https://finance.yahoo.com/) — quotes, financial statements and market news.
- [Bloomberg](https://www.bloomberg.com/europe) — global business and markets news.
- [WSJ](https://www.wsj.com/europe) — The Wall Street Journal's business and financial news.

</details>

<p class="resources-suggest">Know a resource that should be here? Email me at <a href="mailto:smagerakis@upatras.gr">smagerakis@upatras.gr</a>. Several links above are adapted from <a href="https://claesbackman.com/resources.html">Claes Bäckman's resources page</a>.</p>
