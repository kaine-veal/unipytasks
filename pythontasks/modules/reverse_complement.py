'''
2.3. Write a function which generates the reverse complement of a sequence. Bonus points for 
dealing with gaps or incorrect base letters. So given a sequence:
aggagtaagcccttgcaactggaaatacacccattg
the output should look like:
caatgggtgtatttccagttgcaagggcttactcct

Challenge: output the reverse complement of:
GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAG
GCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGT
TGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGA
TCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAAC
CAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAG
TACGAGATTTGAT
'''

import textwrap
from pythontasks.utils.logger import logger


def dna_complement(dna_sequence):
   '''This function returns a complemented DNA sequence. Instad of prompting user input,
      it takes a DNA sequence as an argument, so that the function can be reused in other modules.'''
   
   dna_sequence = "".join(character for character in dna_sequence.upper() if character in "ATCG") # Strips whitespace and only includes characters ATCG and ensures all uppercase
   logger.debug("dna_complement: raw sequence=%s", dna_sequence) # DEBUG will show raw sequence before any transformation
   logger.info("dna_complement: input length %d", len(dna_sequence)) # INFO will display the input length of dna_sequence
   if not dna_sequence:
      logger.warning("dna_complement: received empty or invalid sequence") # WARNING will display if sequence ends up empty after initial formatting
   
   # DNA complement rules. Once complemented, change case to lower to avoid overwriting.
   dna_sequence = dna_sequence.replace('G', 'c').replace('C', 'g') 
   dna_sequence = dna_sequence.replace('A', 't').replace('T', 'a')    
   dna_sequence = dna_sequence.upper() # Change all complemented lowercase DNA bases back to uppercase

   logger.debug("dna_complement: output (first 20bp)=%s", dna_sequence[:20]) # DEBUG will log only the first 20 bases of the output for quick inspection
   return "\n".join(textwrap.wrap(dna_sequence, 60))  # Wrap the output to 60 characters per line



def reverse_dna(dna_sequence):
   '''This function reverses a DNA sequence. Instad of prompting user input,
      it takes a DNA sequence as an argument, so that the function can be reused in other modules.'''
   dna_sequence = "".join(character for character in dna_sequence.upper() if character in "ATCG") # Strips whitespace and only includes characters ATCG and ensures all uppercase
   logger.info("reverse_dna: stripped whitespace, length=%d", len(dna_sequence)) # INFO will display the length of the dna_sequence after whitespace removal
   
   # WARNING logger statement to show if and what characters were dropped after whitespace removal and character 'clean-up'
   cleaned = "".join(ch for ch in dna_sequence.upper() if ch in "ATCG")
   if len(cleaned) != len(dna_sequence):
      logger.warning("reverse_dna: removed %d invalid characters", len(dna_sequence)-len(cleaned))
   dna_sequence = cleaned

   reverse_dna = dna_sequence[::-1] # Reverses the DNA string
   return "\n".join(textwrap.wrap(reverse_dna, 60))  # Wrap the output to 60 characters per line

  
def reverse_complement_dna(dna_sequence):
    '''This function returns a reverse complement DNA sequence by utilising the 2 above functions 'dna_complement' and 'reverse_dna' '''

    # First complement (already cleans + uppercases)
    complemented = dna_complement(dna_sequence).replace("\n", "") # Removes line breaks as dna_complement wraps at 60 characters
    reverse_complemented = reverse_dna(complemented).replace("\n", "") # Again removes line breaks as reverse_dna also wraps at 60 characters

    logger.info("reverse_complement_dna: output length=%d", len(reverse_complemented)) # INFO will display how long the final output length is
    if not reverse_complemented:
        logger.error("reverse_complement_dna: failed to compute reverse complement") # ERROR will display if the result is empty. (e.g. bad input, or if 'cleaning' removed everything)

    return "\n".join(textwrap.wrap(reverse_complemented, 60)) # Wrap the reverse complemented string back into 60-character lines for readability




   
'''
The method beneath prompts the user to paste a DNA sequence which then returns a complemented DNA
sequence and the subsequent reverse complemented sequence.

import sys
import textwrap

def dna_complement(dna_sequence):
   dna_sequence = "".join(character for character in dna_sequence.upper() if character in "ATCG")
   dna_sequence = dna_sequence.replace('G', 'c').replace('C', 'g')
   dna_sequence = dna_sequence.replace('A', 't').replace('T', 'a')    
   dna_sequence = dna_sequence.upper()
   return "\n".join(textwrap.wrap(dna_sequence, 60))  # Wrap the output to 60 characters per line

def reverse_dna(dna_sequence):
   dna_sequence = "".join(dna_sequence.split())  # Remove any whitespace
   reverse_dna = dna_sequence[::-1]
   return "\n".join(textwrap.wrap(reverse_dna, 60))  # Wrap the output to 60 characters per line

if __name__ == "__main__":
    print("Paste DNA:")
    dna_sequence = sys.stdin.read().strip()  # Requires ctrl+Z to end input

    complemented_dna_sequence = dna_complement(dna_sequence)
    reversed_dna_sequence = reverse_dna(complemented_dna_sequence)
    
    print("\nComplemented DNA:")
    print(complemented_dna_sequence)
    print("\nReversed DNA:")
    print(reversed_dna_sequence)
'''