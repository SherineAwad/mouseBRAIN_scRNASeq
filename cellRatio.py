import scanpy as sc
import sys
import importlib_metadata
import matplotlib.pyplot as plt
import argparse

sys.modules['importlib.metadata'] = importlib_metadata

parser = argparse.ArgumentParser()
parser.add_argument('myObject')
args = parser.parse_args()

myObject =  args.myObject

combined_adata = sc.read_h5ad(myObject, backed="r")

# Step 1: Count the total number of cells for each cell type
cell_type_counts = combined_adata.obs['celltype'].value_counts()

# Step 2: Count the number of cells per cell type and cluster
cluster_and_celltype_counts = combined_adata.obs.groupby(['celltype', 'leiden']).size()

# Step 3: Reshape the counts to a DataFrame (clusters as columns)
cluster_and_celltype_counts_unstacked = cluster_and_celltype_counts.unstack(fill_value=0)

# Step 4: Calculate the proportion of cells in each cluster for each cell type
# We will divide the counts for each cluster by the total number of cells in that cell type
cell_type_proportions = cluster_and_celltype_counts_unstacked.div(cell_type_counts, axis=0)

# Step 5: Print the result
print("Cluster Proportions per Cell Type:")
print(cell_type_proportions)





 


