# DBfetch

Author: Murat Buyukyoruk

        DBfetch help:

This script is developed to fetch sequences from multifasta file by using a list of accession numbers to fetch. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

Syntax:

        python DBfetch.py -i DB -l demo_sub_list.txt -o out.fasta

DBfetch dependencies:
	Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download
	tqdm                                                refer to https://pypi.org/project/tqdm/

List example:
------------
List file should contain accessions that separated by new line "\n".

	CP000117.1
	CH902601.1
	CP000469.1
	AAVU01000016.1
	ABCQ01000037.1

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		DB              Specify a DB file to process (i.e., /home/shared/amino-acid/bac_arc_db_01022023/bac_arc_db_01022023_prodigal.faa).

	-l/--list		List		Specify a list of accession (Accession only). Each accession should be included in a new line (i.e. generated with Excel spreadsheet). Script works with or without '>' symbol before the accession.

	-o/--output		output file	Specify a output file name that should contain fetched sequences.

Basic Options:
--------------
	-h/--help		HELP		Shows this help text and exits the run.
