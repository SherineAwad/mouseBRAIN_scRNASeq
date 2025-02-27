with open(config['SAMPLES']) as fp:
    samples = fp.read().splitlines()

rule all:
         input:
            expand("{all}.h5ad", all= config['ALL']), 
            expand("clustered_{all}.h5ad", all=config['ALL']), 
            #expand("figures/dotplot_{all}_markers.png", all =config['ALL']), 
            expand("reClustered_{all}.h5ad", all =config['ALL']),
 
rule preprocess: 
        input:  
            expand("{sample}_filtered_feature_bc_matrix.h5", sample = samples) 
        output: 
          expand("{all}.h5ad", all= config['ALL']), 
        params: 
          samples = config['SAMPLES'],  
          name = config['ALL']
        shell: 
            """
           python preprocess.py {params.samples}  {params.name}  
            """ 

rule cluster: 
       input:
          expand("{all}.h5ad", all=config['ALL']) 
       output:
          expand("clustered_{all}.h5ad", all=config['ALL'])
       shell:
          """
          python cluster.py {input}
          """

rule plot_markers: 
       input: 
           expand("clustered_{all}.h5ad", all=config['ALL']) 
       params: 
          markers = config['MARKERS']
       output: 
           expand("figures/dotplot_{all}_markers.png", all =config['ALL'])
       shell: 
           """
           python plot_markers.py {input} {params.markers} 
           """ 

rule removeClusters: 
       input:
           expand("clustered_{all}.h5ad", all=config['ALL'])
       params:
           removeClusters = config['removeClusters']
       output:
           expand("reClustered_{all}.h5ad", all =config['ALL'])
       shell:
           """
           python removeClusters.py {input} {params} 
           """
            
          

rule annotate:
       input:
          expand("clustered_{all}.h5ad", all=config['ALL'])
       output:
          expand("annotated_{all}.h5ad", all=config['ALL'])
       shell:
          """
          python annotate.py {input}
          """

      
