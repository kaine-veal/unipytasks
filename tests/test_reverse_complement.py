from pythontasks.modules.reverse_complement import (dna_complement, reverse_dna, reverse_complement_dna)

# dna_complement function testing

# Test that each base gets correctly complemented
def test_dna_complement_basic():
    assert dna_complement("ATCG") == "TAGC"

# Test that lowercase input still works correctly
def test_dna_complement_lowercase():
    assert dna_complement("atcg") == "TAGC"

# Test that an empty string returns an empty string
def test_dna_complement_empty():
    assert dna_complement("") == ""


# reverse_dna function testing

# Test a simple reverse
def test_reverse_dna_basic():
    assert reverse_dna("ATCG") == "GCTA"


# reverse_complement_dna function testing

# Test reverse complement on a simple sequence
def test_reverse_complement():
    assert reverse_complement_dna("ATCG") == "CGAT"