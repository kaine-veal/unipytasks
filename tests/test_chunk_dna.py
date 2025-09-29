from pythontasks.modules.chunk_dna import chunk_dna

# Tests a known input of 20 bases and ensures it is split into 2 blocks of 10
def test_basic_chunking():
    dna = "ATCGATCGATCGATCGATCG"
    expected = "ATCGATCGAT CGATCGATCG"  
    result = chunk_dna(dna, block_size=10)
    assert result == expected