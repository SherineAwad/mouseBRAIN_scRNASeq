# Mouse Brain scRNA-seq Analysis

This project contains single-cell RNA sequencing (scRNA-seq) data from mouse brain cortex and striatum regions. The data were processed and analyzed using **Scanpy**, enabling identification and visualization of distinct cell populations across these brain areas.

The analysis includes data normalization, clustering, cell type annotation, and dimensionality reduction (UMAP), providing insights into the cellular composition and heterogeneity of the mouse brain cortex and striatum.

The raw and processed data files can be accessed from the following Google Drive folder:  
[Mouse Brain scRNA-seq Data](https://drive.google.com/drive/folders/17IKV6byo92fhSuGRBpa9Kp4H65W4go9S?usp=sharing)

## Running the Pipeline

To run the analysis pipeline, use Snakemake with the appropriate configuration file for your dataset:

```bash
snakemake -jN -p --configfile config_cortex.tsv

Or

```bash
snakemake -jN -p --configfile config_striatum.tsv

where N is the number of CPU cores (threads) you want to allocate to Snakemake for parallel execution. For example, -j4 uses 4 cores. 
