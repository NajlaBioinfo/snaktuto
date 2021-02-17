# SNAKTUTO
>>> A repository for trying some snakemake tutorials and tricks.

## Authors
>>> Najlabioinfo


# Usage

## Install
>>> Make sure that you are in conda environment with snakemake installed
- Ref[1]
- You can use snakemake docker image : 
 ** https://hub.docker.com/r/najlabioinfo/basicsmk
```bash
docker pull najlabioinfo/basicsmk
```

>>> Make sure that you are in the right place(outside of your workdir):
- git clone https://github.com/NajlaBioinfo/snaktuto.git
- cd snaktuto/snaktuto/

>>> You can run it within 2 ways
- python snaktuto.py
or
- Step by step : Ref[Execute]


## Configure
>>> You must configure your configs/configuser.yaml file:
>>> * [project-name] : change your project name.
>>> * [username] : change your username.
>>> * [data-input] : change your path to able data access.
>>> * [workdir] : make sure that your output dir is accessible and have enough space.

## Execute

### 1. Test your configuration by performing a dry-run via

snakemake --use-conda -n

### 2. Execute the workflow locally via

snakemake prj_tree mini_report fastqc multiqc clean_all --use-conda --core 2 --latency-wait 10

### 3. using $N cores or run it in a cluster environment via

snakemake --use-conda --cluster qsub --jobs 100

### 4. or

snakemake --use-conda --drmaa --jobs 100


# References
* https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html
* https://snakemake.readthedocs.io/en/stable/tutorial/short.html
* https://www.youtube.com/watch?v=hPrXcUUp70Y
* [data source] : https://github.com/snakemake/snakemake-tutorial-data/archive/v5.4.5.tar.gz
* [-wrappers-]: https://github.com/snakemake/snakemake-wrappers


