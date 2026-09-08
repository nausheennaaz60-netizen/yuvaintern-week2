import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 150)

df = pd.read_csv('penguins_cleaned.csv')

print("=== BASIC INFO ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n=== DESCRIPTIVE STATISTICS (numeric) ===")
print(df[['Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)']].describe().round(2))

print("\n=== SPECIES COUNTS ===")
print(df['Species'].value_counts())

print("\n=== ISLAND x SPECIES CROSSTAB ===")
print(pd.crosstab(df['Island'], df['Species']))

print("\n=== MEAN MEASUREMENTS BY SPECIES ===")
print(df.groupby('Species')[['Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)']].mean().round(1))

print("\n=== MEAN BODY MASS BY SPECIES & SEX ===")
print(df[df['Sex']!='Unknown'].groupby(['Species','Sex'])['Body Mass (g)'].mean().round(1))

print("\n=== CORRELATION MATRIX ===")
print(df[['Culmen Length (mm)','Culmen Depth (mm)','Flipper Length (mm)','Body Mass (g)']].corr().round(2))
