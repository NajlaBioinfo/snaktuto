#Example of rules
rule fastqc_pre:
    input:
        "fastq/{name}_{primer}.fastq"
    output:
        html="qc/fastqc/pre/{name, [0-9]{1,2}}_{primer, .+[F-R]}_fastqc.html",
        zip="qc/fastqc/pre/{name,[0-9]{1,2}}_{primer, .+[F-R]}_fastqc.zip"
    wrapper:
        "0.35.1/bio/fastqc"


rule multiqc:
    input:
        expand(["qc/fastqc/pre/{sample}_{primer}_fastqc.zip",
                "qc/fastqc/post/{sample}_{primer}_fastqc.zip"],
               sample=samples.name, primer=["27F", "1492R"])
    output:
        "qc/multiqc.html"
    log:
        "log/multiqc.log"
    params: "--dirs"
    wrapper:
        "0.35.1/bio/multiqc"