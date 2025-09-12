'''
2.1. Refer back to exercise 1.4, where we printed a DNA string in blocks, with a space between each 
block. Now further develop your code so that it displays a DNA string in the style used in GenBank 
records. 

So given the DNA sequence:
GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC
CTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAA
GAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGG
AACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAA
AGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTT
AGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAA
ACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCA
AAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAA
ACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAAC
CTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTA
TTGCAGTGTGGGAGATCAAG

The output should look as close as possible to:
1 gggagaacca ggtgggattg acagtggtaa atgtgttgac cacgagtaaa aacagggccc
61 ggaagcgggg ctatatagaa gagcgcaaga agaacacata aggagagtta ttttgattgg
121 gcaaatcgct ggcaaaattg gcaaaatttc ttcaatagtt tttgtatcaa atagcgaaaa
181 tatttttttt ctcaaaaagt tttttgactg gttagcgtaa actattttag tttctcattt
241 atgagtttta tgcgagttgg taataaatct cacaaaactc taaggacaaa ctctggcaga
301 aatcctaagg agaaacatta agagtttcgt ggtctctggt ctcgtatcga caaacgaggt
361 cttcggttgt atatgttctc tggcaatcac taagggccgc ccggtgtcat ctgccgcatc
421 acgaagtacc cccgaaccct caggtggtat gtaaacagag tatacaagct caaggacaat
481 tcgtcgatac gaaatactaa ggacataatt gttatctatt tcttttaagt ccgtatttcg
541 cttgttcata atttattggt ataatttcag tattcgcata ctcttcggca aactttctca
601 aatcatctaa tgaatatttt ttagtatttc taaatgacat atataatttg tttggtcctc
661 ctcttacttc ataacctctc aatccttttt tggtgtgtat aggaaaaatg gtagggcgaa

Hint: its a good idea to make your code into a function which has parameters for the block size and 
number of blocks per row, as well as the string to print. Also, see if you can ensure that the bases are 
always in lower case when printed regardless of the input.
'''

dna_sequence = """GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC
CTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAA
GAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGG
AACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAA
AGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTT
AGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAA
ACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCA
AAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAA
ACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAAC
CTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTA
TTGCAGTGTGGGAGATCAAG"""


def genbank_chunk_dna(dna_sequence, block_size=10, blocks_per_row=6): 
    dna_sequence = dna_sequence.replace("\n", "").lower() # Removes newlines from dna_sequence input and ensure the DNA sequence is always in lower case
    line_width = block_size * blocks_per_row # Calculates and defines the total line width
    chunks = [] # Create an empty list for formatted output

    for position in range(0, len(dna_sequence), line_width): # Iterate over the DNA sequence in chunks of line_width
        split = dna_sequence[position:position+line_width] # Takes 60 characters from the current position from the for loop

        blocks = [split[i:i+block_size] for i in range(0, len(split), block_size)] # Splits the 'split' chunk of 60 characters into blocks of 10 characters
        block_str = " ".join(blocks) # Joins the blocks with a space

        line_number = str(position+1).rjust(9) # Right-justifies the line number
        chunks.append(f"{line_number} {block_str}") # Appends the formatted line to the chunks list

    return "\n".join(chunks) # Joins all the formatted lines into a single formatted string