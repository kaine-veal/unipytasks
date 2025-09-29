from pythontasks.modules.transcribe_dna import transcribe_dna_to_mrna

# Tests a known DNA sequence against expected lowercase mRNA output
def test_transcription():
    dna = "ATCGT"  
    expected = "aucgu" 
    result = transcribe_dna_to_mrna(dna)
    assert result == expected