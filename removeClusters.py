import scanpy as sc
import sys
import importlib_metadata
import matplotlib.pyplot as plt
import argparse

sys.modules['importlib.metadata'] = importlib_metadata

parser = argparse.ArgumentParser()
parser.add_argument('myObject')
parser.add_argument('clustersFile')
args = parser.parse_args()

myObject =  args.myObject
clustersFile = args.clustersFile

parts = myObject.split("_")  
newObject = "reClustered_" + parts[1]

clusters_to_remove = []

with open(clustersFile, 'r') as f:
    clusters_to_remove = [line.strip() for line in f]


combined_adata = sc.read(myObject)

subset = combined_adata[~combined_adata.obs['leiden'].isin(clusters_to_remove)]

sc.pl.umap(subset, color=["leiden"], save= "_removedClusters.png",legend_loc="on data")

sc.tl.leiden(subset,  n_iterations=2)
sc.pl.umap(subset, color=["leiden"], save= "_reClsuteredclusters.png",legend_loc="on data")

subset.obs_names_make_unique()
subset.write(newObject,compression="gzip")
