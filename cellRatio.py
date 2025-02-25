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


cluster_counts = combined_adata.obs['leiden'].value_counts()

total_cells = combined_adata.n_obs

cluster_ratios = cluster_counts / total_cells

print(cluster_ratios)

 


