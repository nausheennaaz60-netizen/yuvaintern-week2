import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.rcParams['figure.dpi'] = 120
PALETTE = {'Adelie penguin (Pygoscelis adeliae)': '#4C956C',
           'Chinstrap penguin (Pygoscelis antarctica)': '#E07A5F',
           'Gentoo penguin (Pygoscelis papua)': '#3D5A80'}

df = pd.read_csv('penguins_cleaned.csv')
numeric_cols = ['Culmen Length (mm)', 'Culmen Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)']

# ---------- FIG 1: Species distribution ----------
plt.figure(figsize=(6,4))
order = df['Species'].value_counts().index
ax = sns.countplot(data=df, y='Species', order=order, palette=PALETTE)
ax.set_title('Number of Observations per Species', fontsize=12, fontweight='bold')
ax.set_xlabel('Count')
ax.set_ylabel('')
plt.tight_layout()
plt.savefig('fig1_species_count.png')
plt.close()

# ---------- FIG 2: Univariate distributions ----------
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
for ax, col in zip(axes.flat, numeric_cols):
    sns.histplot(data=df, x=col, hue='Species', kde=True, ax=ax,
                 palette=PALETTE, legend=(col==numeric_cols[0]), alpha=0.6)
    ax.set_title(col, fontsize=10, fontweight='bold')
fig.suptitle('Distribution of Physical Measurements by Species', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('fig2_distributions.png')
plt.close()

# ---------- FIG 3: Correlation heatmap (pooled) ----------
plt.figure(figsize=(6,5))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, vmin=-1, vmax=1,
            square=True, fmt='.2f', cbar_kws={'label': 'Correlation'})
plt.title('Correlation Matrix — All Species Pooled', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('fig3_correlation_pooled.png')
plt.close()

# ---------- FIG 4: The Simpson's Paradox scatter (key insight) ----------
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
sns.regplot(data=df, x='Body Mass (g)', y='Culmen Depth (mm)', ax=axes[0],
            scatter_kws={'alpha':0.4, 'color':'gray'}, line_kws={'color':'black'})
axes[0].set_title('Pooled: Body Mass vs Culmen Depth\n(appears negative, r = -0.47)', fontsize=10, fontweight='bold')

sns.scatterplot(data=df, x='Body Mass (g)', y='Culmen Depth (mm)', hue='Species',
                 palette=PALETTE, ax=axes[1], alpha=0.7)
for sp, g in df.groupby('Species'):
    sns.regplot(data=g, x='Body Mass (g)', y='Culmen Depth (mm)', ax=axes[1],
                scatter=False, color=PALETTE[sp], ci=None)
axes[1].set_title('Split by Species: same variables\n(each species shows positive r = 0.58-0.72)', fontsize=10, fontweight='bold')
axes[1].legend(fontsize=7, loc='upper left')
plt.tight_layout()
plt.savefig('fig4_simpsons_paradox.png')
plt.close()

# ---------- FIG 5: Flipper length vs Body mass (strongest correlation) ----------
plt.figure(figsize=(7,5.5))
sns.scatterplot(data=df, x='Flipper Length (mm)', y='Body Mass (g)', hue='Species',
                 style='Sex', palette=PALETTE, s=70, alpha=0.75)
plt.title('Flipper Length vs Body Mass (r = 0.87)', fontsize=12, fontweight='bold')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8)
plt.tight_layout()
plt.savefig('fig5_flipper_vs_mass.png')
plt.close()

# ---------- FIG 6: Culmen length vs depth (species separation) ----------
plt.figure(figsize=(7,5.5))
sns.scatterplot(data=df, x='Culmen Length (mm)', y='Culmen Depth (mm)', hue='Species',
                 palette=PALETTE, s=70, alpha=0.75)
plt.title('Culmen Length vs Depth — Clear Species Clustering', fontsize=12, fontweight='bold')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Culmen Depth (mm)')
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig('fig6_culmen_scatter.png')
plt.close()

# ---------- FIG 7: Species x Island distribution ----------
plt.figure(figsize=(7,4.5))
ct = pd.crosstab(df['Island'], df['Species'])
ct.plot(kind='bar', stacked=True, color=[PALETTE[c] for c in ct.columns], ax=plt.gca())
plt.title('Species Distribution Across Islands', fontsize=12, fontweight='bold')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(fontsize=7, title='Species', bbox_to_anchor=(1.02,1), loc='upper left')
plt.tight_layout()
plt.savefig('fig7_species_by_island.png')
plt.close()

# ---------- FIG 8: Body mass by species & sex ----------
plt.figure(figsize=(8,5))
sub = df[df['Sex'] != 'Unknown']
sns.boxplot(data=sub, x='Species', y='Body Mass (g)', hue='Sex', palette='Set2')
plt.title('Body Mass by Species and Sex', fontsize=12, fontweight='bold')
plt.xticks(rotation=15, ha='right', fontsize=8)
plt.tight_layout()
plt.savefig('fig8_mass_by_species_sex.png')
plt.close()

# ---------- FIG 9: Pairplot ----------
g = sns.pairplot(df, vars=numeric_cols, hue='Species', palette=PALETTE,
                  plot_kws={'alpha':0.6, 's':30}, diag_kind='kde', height=2.0)
g.fig.suptitle('Pairwise Relationships Between Measurements', y=1.02, fontsize=13, fontweight='bold')
g.savefig('fig9_pairplot.png')
plt.close()

print("All figures generated.")
