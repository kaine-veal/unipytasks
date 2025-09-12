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