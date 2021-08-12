#改变GeMoMa的输出，使其适合EVM的输入
#Change the output of GeMoMa to suit the input of EVM 
#运行：python convert_gemoma_to_evm_gff3.py final_annotation.gff > protein_alignments.gff3
#run script: python convert_gemoma_to_evm_gff3.py final_annotation.gff > protein_alignments.gff3
#edit by tankaiwen

import sys,os,re
with open (sys.argv[1],'r') as f:
	for line in f:
		line=line.strip()
		if line.startswith("#"): 
			continue
		type=line.split("\t")[2]
		attr=line.split("\t")[8]
		newline="\t".join(line.split("\t")[0:8])
		if type=="mRNA" :
			ID=re.search(r'ID=(.*?);',attr).group(1)
			target=re.search(r'ref-gene=(.*?);',attr).group(1)
			print ('{}\tID={};Target={}'.format(newline,ID,target))
		elif type=="CDS":
			print ('{}\tID={};Target={}'.format(newline,ID,target))
		else:
			continue
