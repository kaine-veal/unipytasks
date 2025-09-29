'''
2.5. Count single, di-nucleotide and tri-nucleotides in a sequence. 

So for sequence:
aggagtaagcccttgcaactggaaatacacccattg

The output would be something like:
- see exercise sheet

Hint - the above examples only count what is present so there are no counts of zero. For bonus 
points find all possible nucleotide combinations in advance then count those that are present. You 
can also provide warnings about incomplete groups of nucleotides at the end of the sequence, e.g. if 
there are two bases at the end when you are counting tri-nucleotides, and deal with gaps or non-standard bases in the input sequence.

Challenge: find the single, di-nucleotide and tri-nucleotide counts for:
GAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAA
CTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTC
TGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAGAATTGTTACAAATCACCCCTCAA
GGAACCAGGGATGAAATCAGTTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA
'''

from pythontasks.utils.logger import logger


def nucleotide_count(dna_sequence):
    """This function counts mono, di and tri-nucleotides in a DNA sequence"""

    mononucleotide_count = {} # Initiates an empty dictionary to hold mononucleotide counts
    for character in dna_sequence: # Iterates over each character in the input sequence
        if character in mononucleotide_count: # If the base already exists in dict, then increase its count by 1
            mononucleotide_count[character] +=1
        else: 
            mononucleotide_count[character] = 1 # If this base is seen for the first time, add to the dict with a starting count of 1
    for character, count in mononucleotide_count.items(): # Iterates through each key:value pair in the dict and counts how many times each character has appeared
        logger.info(f"The mononucleotide count of the given dna sequence is {character}: {count}") # Logs the result
    
    dinucleotide_count = {} # Initiates an empty dictionary to hold dinonucleotide counts
    for position in range(len(dna_sequence) - 1): # Iterates over each base in the sequence, stopping 1 base before the end as dinucleotides need 2 bases
        dinucleotide = dna_sequence[position:position + 2] # Takes a slice of 2 bases starting at the current position
        if dinucleotide in dinucleotide_count: # If the base already exists in dict, then increase its count by 1
            dinucleotide_count[dinucleotide] += 1
        else:
            dinucleotide_count[dinucleotide] = 1 # If this base is seen for the first time, add to the dict with a starting count of 1
    for dinucleotide, count in dinucleotide_count.items(): # Iterates through each key:value pair in the dict and counts how many times each character has appeared
            logger.info(f"The dinucleotide count of the given dna sequence is {dinucleotide}: {count}") # Logs the result

    # Logger error handling if there are remaining bases at the end of the dna sequence that do not form a dinucleotide
    n = 2
    remainder = len(dna_sequence) % n
    if remainder != 0:
        logger.warning(f"Sequence has {remainder} leftover base(s) that does not form a complete dinucleotide")
    

    trinucleotide_count = {} # Initiates an empty dictionary to hold trinonucleotide counts
    for position in range(len(dna_sequence) - 2): # Iterates over each base in the sequence, stopping 2 bases before the end as trinucleotides need 3 bases
        trinucleotide = dna_sequence[position:position + 3] # Takes a slice of 3 bases starting at the current position
        if trinucleotide in trinucleotide_count: # If the base already exists in dict, then increase its count by 1
            trinucleotide_count[trinucleotide] += 1
        else:
            trinucleotide_count[trinucleotide] = 1 # If this base is seen for the first time, add to the dict with a starting count of 1
    for trinucleotide, count in trinucleotide_count.items(): # Iterates through each key:value pair in the dict and counts how many times each character has appeared
            logger.info(f"The trinucleotide count of the given dna sequence is {trinucleotide}: {count}") # Logs the result

    # Logger error handling if there are remaining bases at the end of the dna sequence that do not form a trinucleotide
    n = 3
    remainder = len(dna_sequence) % n
    if remainder != 0:
        logger.warning(f"Sequence has {remainder} leftover base(s) that does not form a complete trinucleotide")
    
    
    return mononucleotide_count, dinucleotide_count, trinucleotide_count # Returns a tuple of 3 dicts