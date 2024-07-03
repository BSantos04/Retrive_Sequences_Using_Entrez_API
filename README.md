# Retrieve_Sequences_Using_Entrez_API
This repository contains a python script that retrieves sequences from a database using the E-Utilities from NCBI.

This is a work proposed in the Curricular Unit of Analysis of Biological Sequences from the Bioinformatics course.
# Requisities
-Python3

-Biopython (Entrez & SeqIO)
# Installation
## PIP command
### For python3
`sudo apt install python3-pip`
## Biopython
`pip install biopython`
# Tutorial
`python3 script.py database term`
## Script.py
The python script we are going to run.
## Database
The name of the database (nucleotide, protein, genome or gene).
## Term
The term we want to search in the database. Make sure to write it between quotation marks.
## Example
`python3 homework1_asb.py nucleotide "Psammodromus algirus[organism], cytb[gene]"` 
# Credits
https://biopython.org/


