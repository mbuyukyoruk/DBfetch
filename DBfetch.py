import sys
import argparse
import os
import subprocess
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except :
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python DBfetch.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

Author: Murat Buyukyoruk

        DBfetch help:

This script is developed to fetch sequences from multifasta file by using a list of accession numbers to fetch. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

Syntax:

        python DBfetch.py -i DB -l demo_sub_list.txt -o out.fasta

DBfetch dependencies:
	Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download
	tqdm                                                refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		DB              Specify a DB file to process (i.e., /home/shared/amino-acid/bac_arc_db_01022023/bac_arc_db_01022023_prodigal.faa).

	-l/--list		List			Specify a list of accession (Accession only). Each accession should be included in a new line (i.e. generated with Excel spreadsheet). Script works with or without '>' symbol before the accession.

	-o/--output		output file	    Specify a output file name that should contain fetched sequences.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a DB file to process.\n')
parser.add_argument('-l', '--list', required=False, type=str, dest='list', default=None,
                    help='Specify a list of accession numbers to fetch.\n')
parser.add_argument('-o', '--output', required=True, dest='out',
                    help='Specify a output fasta file name.\n')

results = parser.parse_args()
filename = results.filename
list = results.list
out = results.out

os.system('> ' + out)

print(
    "Locating index file! An index file will be generated if the fasta file is provided for the first time to generate DB.")

index = filename + '.index'
record_dict = SeqIO.index_db(index, filename, 'fasta')

proc = subprocess.Popen("wc -l < " + list, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

if list != None:
    f = open(out, 'a')
    sys.stdout = f
    with tqdm.tqdm(range(length + 1)) as pbar:
        pbar.set_description('Reading...')
        with open(list, 'r') as file:
            for line in file:
                pbar.update()
                acc = line.split()[0].split("\n")[0]
                found = record_dict[acc]
                print(found.format("fasta"))
