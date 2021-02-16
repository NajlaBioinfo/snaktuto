####
# snaktuto/snaktuto.py
# BY NajlaBioinfo Fev21
###
"""

Automated launch of snakemake workflow

"""


import os 
import yaml

def run_snakemake_wf():
    """ Run WF """
    os.system("snakemake prj_tree mini_report fastqc multiqc clean_all --use-conda --core 2 --latency-wait 15")

def report_generation():
    """ Generate smk report """
    os.system("snakemake prj_tree mini_report fastqc multiqc clean_all --use-conda --core 2 --latency-wait 15 --report report.html")

def graph_generation():
    """ Generate smk graph """
    os.system("snakemake prj_tree mini_report fastqc multiqc clean_all  --rulegraph | dot -Tpdf > dag.pdf")

def clean_up():
    """ Move report and graph to project dir """

    with open(r'configs/configuser.yaml') as file:
        param_list = yaml.load(file, Loader=yaml.FullLoader)
    #print(param_list['projectname'])
    reportpath= param_list['workdir']+"/"+param_list['projectname']+"/Reports/"
    #print (reportpath)
    os.system ("mv report.html " + reportpath)
    os.system ("mv dag.pdf " + reportpath)


def workflow_launch():
    ## Run the wf
    run_snakemake_wf()
    ## Create the report
    report_generation()
    ## Create the graph
    graph_generation()
    # Clean up
    clean_up()


# Func Call
workflow_launch()
