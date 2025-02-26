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

cell_type_counts = combined_adata.obs['celltype'].value_counts()

total_cells = cell_type_counts.sum()

cell_type_ratios = cell_type_counts / total_cells

print(cell_type_ratios)



