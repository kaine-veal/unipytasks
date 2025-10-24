'''
2.4. Combine translation and reverse complement functions to generate a six frame translation of a 
DNA sequence. This means you should translate three forward reading frames starting at the first, 
second and third base of the first codon of the forward sequence, and three reverse reading frames 
starting at the first, second and third base of the first codon of the reverse complement of the 
sequence. 

So given a sequence:
aggagtaagcccttgcaactggaaatacacccattg

The output should be something like:

Forward
1 RSKPLQLEIHPL
2 GVSPCNWKYTH
3 E*ALATGNTPI
Reverse
1 QWVYFQLQGLTP
2 NGCISSCKGLL
3 MGVFPVARAYS

Challenge: print the six-frame translation of:
GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCT
TCACCC
'''


from pythontasks.modules.translate_dna import translate_dna_to_AAseq
from pythontasks.modules.reverse_complement import reverse_complement_dna   

def six_frame_translation(dna_sequence):
    """
    Generates the six-frame translation from 5'-3' and reverse complement from 3'-5'
    """

    translations = {"Forward": [], "Reverse": []}

    # Forward strand translation
    for frame_start in [0, 1, 2]: # Frames start at position 0,1,2
        frame_sequence = dna_sequence[frame_start:] # Shifts the starting point of translation
        if len(frame_sequence) >= 3: # Only translate if at lease one codon
            protein = translate_dna_to_AAseq(frame_sequence) # Calls the translate function on each frame_sequence
            translations["Forward"].append(protein) # Appends the resulting protein to the forward list in the translations dictionary

    # Reverse strand translation
    reverse_sequence = reverse_complement_dna(dna_sequence) # Starts by calling the reverse complement function on the input dna sequence 
    for frame_start in [0, 1, 2]: # Frames again start at position 0,1,2 as dna is now reverse complemented
        frame_sequence = reverse_sequence[frame_start:] # Shifts the starting point of translation
        if len(frame_sequence) >= 3: # Only translate if at lease one codon
            protein = translate_dna_to_AAseq(frame_sequence) # Now calls the translate function on reverse complemented sequence
            translations["Reverse"].append(protein) # Appends the resulting protein to the reverse list in the translations dictionary

    # Format the output
    formatted_output = [] # Initiate an empty list to collect lines of text

    formatted_output.append("Forward") # Add the section header for the forward strand translation
    for frame_number, protein_sequence in enumerate(translations["Forward"], start=1): # Loop through each protein sequence in the forward frames with its frame number
        formatted_output.append(f"{frame_number} {protein_sequence}") # Format the frame number and protein sequence into one string

    formatted_output.append("Reverse") # Add the section header for the reverse strand translation
    for frame_number, protein_sequence in enumerate(translations["Reverse"], start=1): # Loop through each protein sequence in the forward frames with its frame number
        formatted_output.append(f"{frame_number} {protein_sequence}") # Format the frame number and protein sequence into one string

    return "\n".join(formatted_output) # # combine all entries in the list into one string, placing each entry on its own line