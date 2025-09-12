'''
1.4. Given a string representing a DNA sequence, print it in blocks, i.e. with gaps every so many bases.
So given sequence: 
aggagtaagcccttgcaactggaaatacacccattg
an output with a block size of 3 should look like:
agg agt aag ccc ttg caa ctg gaa ata cac cca ttg

Challenge: output the following sequence with a block size of 10:
GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAG
GAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCT
TCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTC
TGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTG
AAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAG
GAGCCTACAAGAAAGTACGAGATTTGA
'''


def chunk_dna(dna_sequence, block_size=10):
    chunks = [] # Creates an empty list for chunk_dna to be stored 
    for character_split in range(0, len(dna_sequence), block_size): # Iterate over the DNA sequence in chunks of 10
        split = dna_sequence[character_split:character_split+block_size] # Takes 10 characters from the current position from the for loop
        chunks.append(split) # Appends the split chunk of 10 characters to the chunks list

    return " ".join(chunks) # Returns the list as a single string, with chunks separated by spaces
