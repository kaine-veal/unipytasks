'''
2.6. Develop a function which gives the GC content of a sequence. This is the number of G plus C 
bases in a sequence as a percentage of the total number of bases in the sequence. 

So for the sequence:
aggagtaagcccttgcaactggaaatacacccattg

the GC content is 47.22%.

Hint: if you have completed 2.5 you can use that function to help achieve this.

Challenge: what is the GC content of:
GAACCCGAAAATCCTTCCTTGCAGGAAACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAA
CTCTGAGGACAAAGCAGCGGATACAACCTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTC
TGAAGATACCGTTAATAAGGCAACTTATTGCAGTGTGGGAGATCAAGAATTGTTACAAATCACCCCTCAA
GGAACCAGGGATGAAATCAGTTTGGATTCTGCAAAAAAGGCTGCTTGTGAATTTTCTGAGACGGATGTAA
'''

from pythontasks.utils.logger import logger

def calculate_gc_content(dna_sequence):

    # Error handling for empty input
    if not dna_sequence:
        logger.warning("Empty DNA sequence")
        return None

    cleaned_sequence = '' # Initiates an empty string to collect valid characters
    for character in dna_sequence: # Iterates over each character in the input sequence
        character = character.upper() # Converts character to uppercase to standardise

        # Error handling for non-ATCG characters and breaks the function if found
        if character not in 'ATCG': 
            logger.error("DNA sequence contained ambiguous characters, not equal to ATCG")
            return None
                  
        cleaned_sequence += character # Appends valid characters to cleaned_sequence
        
    g_count = cleaned_sequence.count('G') # Counts the number of Gs in the cleaned sequence
    c_count = cleaned_sequence.count('C') # Counts the number of Cs in the cleaned sequence
    gc_count = g_count + c_count # Sums the G and C counts

    gc_percentage = (gc_count/len(cleaned_sequence)) *100 # Calculates the GC percentage
    gc_percentage = round(gc_percentage, 2) # Rounds the percentage to 2 decimal places

    # Log the result
    logger.info(f"The GC content of the given DNA sequence: {dna_sequence} is {gc_percentage}%")
    return f"{gc_percentage}%"


result = calculate_gc_content('gatagcgcatcgttactgatgtgtacgacgatcatcgactgagctacgaccacaccac') # Test to check function works