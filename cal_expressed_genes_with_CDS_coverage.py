# coding: utf-8
# python version: >= 3
# 根据bedtools coverage的结果文件，统计reads覆盖cds的比例,自动输出xxx_cds_coverage.txt文件
# According to the result file of bedtools coverage, count the proportion of reads covering cds, and automatically output the xxx_cds_coverage.txt file 
# 运行脚本: python script.py xxx.depth.txt 
# Run the script: python script.py xxx.depth.txt 
# edit by tankaiwen 2021.06.09

import sys

# 读取输入文件
# Read input file 
depth_file=sys.argv[1]

name = depth_file.split('.')
geneID_coverage_dict = {}
geneID_cds_dict = {}
geneID_gene_length_dict = {}

with open(depth_file,'r') as depth:
    for i in depth:
        
        line_depth = i.strip().split('\t')
        geneID=line_depth[3]
        cds_length=float(line_depth[5])
        gene_length=float(line_depth[6])
        
        if int(line_depth[4]) >= 5:

            if geneID in geneID_cds_dict:
                geneID_cds_dict[geneID] = int(geneID_cds_dict[geneID]) + cds_length
            else:
                geneID_cds_dict.setdefault(geneID,cds_length)
            if geneID in geneID_gene_length_dict:
                geneID_gene_length_dict[geneID] = int(geneID_gene_length_dict[geneID]) + gene_length
            else:
                geneID_gene_length_dict.setdefault(geneID,gene_length)
        else:
            if geneID in geneID_cds_dict:
                continue
            else:
                geneID_cds_dict.setdefault(geneID,0)
            if geneID in geneID_gene_length_dict:
                geneID_gene_length_dict[geneID] = int(geneID_gene_length_dict[geneID]) + gene_length
            else:
                geneID_gene_length_dict.setdefault(geneID,gene_length)

# 开始计算覆盖比例
# Start calculating coverage ratio 
geneID_coverage_dict = {k : v/geneID_gene_length_dict[k] for k, v in geneID_cds_dict.items() if k in geneID_gene_length_dict}
# 将结果写进输出文件
# Write the results into the output file 
output = open(name[0]+'_cds_coverage.txt','w')
for i,j in geneID_coverage_dict.items() :
    print(i,j,file=output,sep='\t')
output.close()

