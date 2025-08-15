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

def dna_complement(dna_sequence):
   '''This function returns a complemented DNA sequence. Instad of prompting user input,
      it takes a DNA sequence as an argument, so that the function can be reused in other modules.'''
   dna_sequence = "".join(character for character in dna_sequence.upper() if character in "ATCG")
   dna_sequence = dna_sequence.replace('G', 'c').replace('C', 'g')
   dna_sequence = dna_sequence.replace('A', 't').replace('T', 'a')    
   dna_sequence = dna_sequence.upper()
   return "\n".join(textwrap.wrap(dna_sequence, 60))  # Wrap the output to 60 characters per line

def reverse_dna(dna_sequence):
   '''This function reverses a DNA sequence. Instad of prompting user input,
      it takes a DNA sequence as an argument, so that the function can be reused in other modules.'''
   dna_sequence = "".join(dna_sequence.split())  # Remove any whitespace
   reverse_dna = dna_sequence[::-1]
   return "\n".join(textwrap.wrap(reverse_dna, 60))  # Wrap the output to 60 characters per line

def reverse_complement_dna(dna_sequence):
   '''This function complements and reverses a DNA sequence. Instad of prompting user input,
      it takes a DNA sequence as an argument, so that the function can be reused in other modules.'''
   dna_sequence = "".join(character for character in dna_sequence.upper() if character in "ATCG")
   dna_sequence = dna_sequence.replace('G', 'c').replace('C', 'g')
   dna_sequence = dna_sequence.replace('A', 't').replace('T', 'a')   
   dna_sequence = dna_sequence.upper()
   reverse_complement_dna = dna_sequence[::-1]
   return "\n".join(textwrap.wrap(reverse_complement_dna, 60))

   
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