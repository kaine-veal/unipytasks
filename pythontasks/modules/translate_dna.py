'''
2.2. Write a function to translate a DNA sequence into an amino acid sequence (dont use imported 
modules to do this for now). You can find the standard genetic code table here 
https://www.genscript.com/tools/codon-table and elsewhere. Hint: one way is to create a dictionary 
to hold a translation table. Use single letter amino-acid codes, and assume coding starts from the 
first base only.
So given a sequence:
aggagtaagcccttgcaactggaaatacacccattg
The output should look like:
RSKPLQLEIHPL
For bonus points, deal with any errors in the DNA string, e.g. incomplete codons at the end of the 
sequence, gaps or incorrect bases in the sequence. For now dont consider ambiguity base codes like N.

Challenge: now translate the following sequence:
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCC
CATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGA
AACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAA
'''

from pythontasks.utils.logger import logger

def translate_dna_to_AAseq(dna_sequence):
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    # Strips whitespace and only includes characters ATCG. Ensures all uppercase and filters to only allow ATCG
    dna_sequence = "".join(character for character in dna_sequence.upper() if character in "ATCG") 
    
    protein = "" # Define an empty list which will accumulate one letter amino acids
    for position in range(0, len(dna_sequence), 3): # Iterate over filtered DNA in steps of 3 to read each codon
        codon = dna_sequence[position:position + 3] # Slices out a 3-base codon
        if len(codon) < 3: # If a partial codon is reached at the end of the DNA string, stop and print remainder
            logger.debug(f"Remaining codon incomplete: {codon}")
            break

        # Translate codon to corresponding amino acid
        amino_acid = codon_table.get(codon, "X")

        # If a stop codon is hit, end translation and dont include '*'
        if amino_acid == "*":
            logger.debug(f"Stop codon reached at position {position}: {codon}")
            protein += "*"
            continue 

        protein += amino_acid # Append the translated amino acid to the growing protein string

    return protein # Returns and stores the result so calling code can use it



'''
The method beneath prompts the user to paste a DNA sequence, which can be multiline (sys), 
and translates it into corresponding protein sequence

import sys

def translate_dna_to_AAseq(dna_sequence):
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    dna_sequence = "".join(character for character in dna_sequence.upper() if character in "ATCG") # Strips whitespace and only includes characters ATCG
    
    protein = ""
    for position in range(0, len(dna_sequence), 3):
        codon = dna_sequence[position:position + 3]
        if len(codon) < 3:
            print(f"Remaining codon incomplete: {codon}")
            break

        amino_acid = codon_table(codon)

        if amino_acid == "*":
            print(f"Stop codon reached at position {position}: {codon}")
            break

        protein += amino_acid

    print(f"Protein sequence: \n{protein}")

    return "".join(protein)            


if __name__ == "__main__":
    print("Paste DNA:")
    dna_sequence = sys.stdin.read() # Requires ctrl+Z to end input
    protein = translate_dna_to_AAseq(dna_sequence)
'''