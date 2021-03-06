import os
from Bio import SeqIO
import subprocess
from pathlib import Path




# home would contain something like "/Users/jame"
home = str(Path.home())

path = home + "/Desktop/MiniProject/Results/"

#figured this out with Dr. Putonti on how to avoid the hardcode


sra_number = "SRR8185310"
print ("Currently downloading: " + sra_number)
prefetch = "prefetch " + sra_number
print ("The command used was: " + prefetch)
subprocess.call(prefetch, shell=True)


print ("Generating fastq for: " + sra_number)


#non hard coded 

fastQFile= home

fastq_dump = "fastq-dump --outdir path --gzip --skip-technical  --readids --read-filter pass --dumpbase --split-3 /Users/sabrinalutfiyeva/Desktop/MiniProject/SRAdata/sra/" + sra_number + ".sra"
print ("The command used was: " + fastq_dump)
subprocess.call(fastq_dump, shell=True)
#got this off of internet


#had to hardcode this bc of SPADES and how it was downloaded
getAssembly = "/Users/sabrinalutfiyeva/Downloads/SPAdes-3.15.4-Darwin/bin/spades.py	-k	55,77,99,127	-t	2	--only-assembler	-s/Users/sabrinalutfiyeva/Desktop/MiniProject/SRAdata/SRR8185310_pass.fastq.gz	-o	/Users/sabrinalutfiyeva/Desktop/MiniProject/SRAdata/SRA_assembly"
subprocess.call(getAssembly, shell =True)

#write SPAdes command to log file
#w+ python command to create new file and read or write to it if not already existing


logFile = open(path + "miniproject.log", "w+")
logFile.write("The spades command is " + getAssembly)


#calculate # of contigs with length 

contigList1000= []


with open("path + contigs.fasta/") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        if len(record.seq) > 1000:
            contigList1000.append(record)

#write the # out to log file , from here on out, only consider the contigs > 1000 bp in length
logFile.write("There are %i contigs > 1000 in the assembly" % getAssembly)
SeqIO.write(contigList1000, path + "1000contigs.fasta","fasta")

#4. calculate length of assembly (total number of bp in all the contigs> 1000 bp in length) and write this out to log files

num= 0
file1000contigs = SeqIO.parse("/Users/sabrinalutfiyeva/Desktop/MiniProject/Results/1000contigs.fasta","fasta")
for x in file1000contigs:
    num = num + len(x)
countlength = ("There are " + str(num) + " bp in the assembly.")
    

#5 i used prokka

prokka1='prokka --force --outdir ' + path + 'Prokka_Output/ --genus Escherichia --locustag ECOL long_sequences.fasta'
logFile.write("Prokka command is " + prokka1)

subprocess.call('prokka --force --outdir ' + path + 'Prokka_Output/ --genus Escherichia --locustag ECOL long_sequences.fasta')
