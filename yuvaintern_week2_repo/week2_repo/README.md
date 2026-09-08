# Week 2 — Exploratory Data Analysis & Visualization

Task submitted for the **YuvaIntern Virtual Data Science with Python Trainee** internship (Week 2).

## Objective
Perform exploratory data analysis (EDA) and visualization on a public dataset using Pandas,
Matplotlib, and Seaborn, extracting meaningful insights beyond basic summary statistics.

## Dataset
Continues from [Week 1](../yuvaintern-week1-data-cleaning) — the cleaned **Palmer Archipelago
(Antarctica) Penguin Data** (342 records, 3 species, 3 islands).

## Repo structure
```
├── Week2_EDA_Report.docx        # Full report: analysis, code, visuals, interpretation
├── data/
│   └── penguins_cleaned.csv     # Cleaned dataset (input, from Week 1)
├── scripts/
│   ├── 01_summary_stats.py      # Descriptive statistics, groupby summaries, correlations
│   └── 02_visualizations.py     # All 9 figures (distributions, correlation, pairplot, etc.)
└── figures/                     # All generated chart images
```

## Key finding
The headline insight in this analysis is a **Simpson's Paradox**: culmen (bill) depth appears
*negatively* correlated with body mass when all species are pooled (r = -0.47), but within every
individual species the relationship is clearly *positive* (r = 0.58–0.72). This is because species
acts as a confounding variable — Gentoo penguins are both the heaviest species and have
proportionally shallower bills, which reverses the correlation's sign when species are mixed
together. See Section 4.3 of the report for the full breakdown and visualization.

Other findings include: flipper length as the strongest, most consistent predictor of body mass
(r = 0.87), near-perfect species/island confounding, and consistent sexual dimorphism in body
mass across all three species.

## How to run
```bash
pip install pandas numpy matplotlib seaborn
cd scripts
python 01_summary_stats.py
python 02_visualizations.py
```

## Full report
See [`Week2_EDA_Report.docx`](./Week2_EDA_Report.docx) for the complete write-up.
