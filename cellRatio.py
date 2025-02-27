import scanpy as sc
import sys
import importlib_metadata
import matplotlib.pyplot as plt
import argparse
import pandas as pd
import seaborn as sns

sys.modules['importlib.metadata'] = importlib_metadata

parser = argparse.ArgumentParser()
parser.add_argument('myObject')
args = parser.parse_args()

myObject =  args.myObject

combined_adata = sc.read_h5ad(myObject, backed="r")

cell_type_counts = combined_adata.obs.groupby(['sample', 'celltype']).size().unstack(fill_value=0)

cell_type_percentages = cell_type_counts.div(cell_type_counts.sum(axis=1), axis=0) * 100

df = cell_type_percentages.reset_index()

df_long = df.melt(id_vars=["sample"], var_name="CellType", value_name="Percent")

df_long = df_long.drop_duplicates(subset=['sample', 'CellType'])

df_long = df_long.groupby(['sample', 'CellType'], as_index=False)['Percent'].sum()

custom_order = ["WT_Astro", "KO_Astro", "Dediff-Astro", "Oligos", "Pro-NSC", "NSC", "Neurons"]

df_long['CellType'] = pd.Categorical(df_long['CellType'], categories=custom_order, ordered=True)

unique_cell_types = df_long['CellType'].unique()

colors = sns.color_palette("Set2", len(unique_cell_types))

cell_type_colors = dict(zip(unique_cell_types, colors))

plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid", palette="dark")

df_wide = df_long.pivot(index='sample', columns='CellType', values='Percent').fillna(0)

ax = df_wide.plot(kind='bar', stacked=True, figsize=(10, 6), color=[cell_type_colors[cell] for cell in custom_order])

ax.grid(False)

plt.ylabel('Cell Ratio (%)')
plt.xlabel('Sample')
plt.title('Celltype Ratio')

plt.xticks(rotation=45, ha="right")

plt.legend(title="Cell Type", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

plt.savefig("cell_ratio_stacked_bar_chart.png")









