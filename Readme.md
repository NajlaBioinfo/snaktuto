# SNAKTUTO
>>> A repository for trying some snakemake tutorials and tricks.

## Authors
>>> Najlabioinfo


# Usage

## Install
>>> Make sure that you are in conda environment with snakemake installed

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

snakemake --use-conda --cores $N

### 3. using $N cores or run it in a cluster environment via

snakemake --use-conda --cluster qsub --jobs 100

### 4. or

snakemake --use-conda --drmaa --jobs 100

# References
* https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html
* https://www.youtube.com/watch?v=hPrXcUUp70Y
