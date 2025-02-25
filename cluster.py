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
parts = myObject.split(".")  
newObject = "clustered_" + myObject

combined_adata = sc.read(myObject)
figure_name = parts[0] + ".png"

sc.pp.normalize_total(combined_adata, target_sum=1e4)
sc.pp.log1p(combined_adata)
sc.pp.highly_variable_genes(combined_adata)
sc.pp.scale(combined_adata)
sc.tl.pca(combined_adata, svd_solver='arpack',n_comps=20) 
sc.pp.neighbors(combined_adata,  random_state=0)
sc.tl.umap(combined_adata)
sc.pl.umap(combined_adata, color='sample', size=2, save=figure_name)

sc.tl.leiden(combined_adata,  n_iterations=2)
figure_name = parts[0] + "clusters.png"
sc.pl.umap(combined_adata, color=["leiden"], save= figure_name,legend_loc="on data")


combined_adata.obs_names_make_unique()

combined_adata.write(newObject,compression="gzip")
