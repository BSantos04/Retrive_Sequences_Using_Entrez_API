import argparse
from Bio import Entrez, SeqIO

def parse_arguments():
    """
    Before starting retrieving the sequences, first we need to parse the command line arguments to prevent any future misuse from the user.
    
    For that, we use the method argparse.ArgumentParser() to contain the argument specifications. 
    
    After that, we need to specify the arguments we want to attach to the parser.
    
    In that case, we want to attach the database and the term.
    
    If there is a missing argument, the terminal will display a message with the required missing argument(s) and exit the program.
    
    If there is any extra argument, the terminal will display the unrecognized arguments and close the program.
    
    Returns the database and term arguments from the command line using argparse.Namespace.
    """
    parser=argparse.ArgumentParser()  
    parser.add_argument("database", help="\nDatabase missing (nucleotide, genome, protein or gene).")
    parser.add_argument("term", help="\nSearching term missing (Ex.:'Psammodromus algirus[organism], cytb[gene]').") 
    return parser.parse_args().database, parser.parse_args().term
    
        
def search(database,term):
    """
    Takes two arguments: database name & searching term.
    
    Uses Bio.Entrez method .esearch() in order to search the desired term in the choosen database.
    
    Bio.Entrez method .read() will then parse the XML file from .esearch() into a python dictionary or list containing the primary IDs from the search.
    
    From this dictionary we will only need the Web Environment and the Query Key.
    
    It's also good practice to always close the file in order to prevent memory leaks.
    
    It's also good practice enter an email to use the API.
    """
    Entrez.email = "bcmpswork@gmail.com"
    handle=Entrez.esearch(db=database, term=term, usehistory="y")
    record=Entrez.read(handle)
    handle.close()
    return record["WebEnv"], record["QueryKey"]


def fetch(database,webenv,querykey):
    """
    Takes three arguments: database name, Web Environment and Query Key provided by the Entrez "history".
    
    The method .efetch() will retrieve the records from the search results/record. 
    
    SeqIO.parse() will take the results from efetch and parse them in FASTA, returning a SeqRecord iterator.
    
    And then, we print the object(s) as a string.
    
    Just like the previous fuction, we close the file.
    """
    results=Entrez.efetch(db=database, rettype="fasta", retmode="text", webenv=webenv, query_key=querykey)
    for sequences in SeqIO.parse(results,"fasta"):
        print(sequences.format("fasta"))
    results.close()
    
    
def main():
    """
    The main function where the entire process happens.
    """
    database, term = parse_arguments()
    webenv, querykey = search(database,term)
    fetch(database,webenv,querykey)


if __name__=="__main__":
    """
    We are just ensuring the code is only executed when the script is run as a standalone program.
    """
    main()

