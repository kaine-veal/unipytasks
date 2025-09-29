from pythontasks.modules.GC_content import calculate_gc_content

# Tests a known DNA sequence against expected GC % output
def test_valid_sequence():
    dna = "ATGC"  
    result = calculate_gc_content(dna)
    assert result == "50.0%"

# Test to ensure that AT returns 0%
def test_all_at():
    dna = "ATATAT"  
    result = calculate_gc_content(dna)
    assert result == "0.0%"
