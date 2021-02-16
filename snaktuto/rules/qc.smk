config: "configs/configuser.yaml"
rule fastqc:
	priority: 7

	message: "Step3: Launch FASTQC."

	params:
		qcfolder=config["workdir"]+"/"+config["projectname"]+"/"+"qc/fastqc"
	input:
        	fastq=expand(config["datadir"]+"/{sample}.fastq", sample=SAMPLES)
	output:
        	#html=expand(QCPATH+"/{sample}.html",sample=SAMPLES),
        	zip=expand(QCPATH+"/{sample}_fastqc.zip",sample=SAMPLES)
	
	log: expand("logs/fastqc/{sample}.log",sample=SAMPLES)
    	threads: 2
	
	conda: 
		"../envs/fastqc.yaml"
	#wrapper:
	#	"master/bio/fastqc"
	
	shell:
		r""" 
		fastqc --version
		mkdir -p {params.qcfolder}
		fastqc -t {threads} {input.fastq} -o {params.qcfolder}
		sleep 15
		"""

rule multiqc:
	priority: 6
	input:
        	expand(QCPATH+"/{sample}_fastqc.zip",sample=SAMPLES)
	#output:
        #	"qc/fastqc/multiqc_report.html"
	conda: 
		"../envs/fastqc.yaml"
	log:
		"logs/multiqc.log"
	params:
		qcf=QCPATH
	#wrapper:
	#	"master/bio/multiqc"
	shell:
		r"""
		cd {params.qcf}
		multiqc .
		mkdir ../multiqc
		cd ../multiqc
		mv ../fastqc/multiqc_* .
		"""	
