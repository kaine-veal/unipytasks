'''
1.5. Write code to transcribe a DNA sequence. So given sequence:
aggagtaagcccttgcaactggaaatacacccattg
the output will be:
aggaguaagcccuugcaacuggaaauacacccauug

Challenge: transcribe the following:
GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAG
GCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGT
TGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGA
TCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAAC
CAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAG
TACGAGATTTGAT
'''



def transcribe_dna_to_mrna(dna_sequence): 
    """
    This function transcribes a DNA sequence into mRNA. Instad of prompting user input,
    it takes a DNA sequence as an argument, so that the function can be reused in other modules.
    """
    
    dna_sequence = "".join(dna_sequence.split()) # Removes any whitespace from the dna sequence
    dna_sequence = dna_sequence.replace('n', '').replace('N', '') # Removes any n or N characters
    dna_sequence = dna_sequence.upper().replace('T', 'U') # Convert everything to uppercase and replace T with U

    return dna_sequence.lower() # Return the final mRNA sequence in lowercase



'''
The method beneath prompts the user to paste a DNA sequence and then transcribes it into mRNA into the terminal.

import sys

def transcribe_dna_to_mrna(dna_sequence): 
    dna_sequence = "".join(dna_sequence.split())  
    dna_sequence = dna_sequence.replace('n', '').replace('N', '')  
    dna_sequence = dna_sequence.replace('T', 'U')
    
    return dna_sequence.lower()

if __name__ == "__main__":
    print("Paste DNA:")
    dna_sequence = sys.stdin.read().strip() # Requires ctrl+Z to end input
    mrna_sequence = transcribe_dna_to_mrna(dna_sequence)
    print(mrna_sequence)
'''