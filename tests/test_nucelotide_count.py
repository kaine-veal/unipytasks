from pythontasks.modules.nucleotide_count import nucleotide_count

# Tests known input against expected mononucleotide counts
def test_mononucleotide_count():
    dna = "ATCGAT"
    mono, di, tri = nucleotide_count(dna)
    assert mono == {"A": 2, "T": 2, "C": 1, "G": 1}

# Tests known input against expected dinucleotide counts
def test_dinucleotide_count():
    dna = "ATAT"
    mono, di, tri = nucleotide_count(dna)
    assert di == {"AT": 2, "TA": 1}

# Tests known input against expected trinucleotide counts
def test_trinucleotide_count():
    dna = "ATGATG"
    mono, di, tri = nucleotide_count(dna)
    assert tri == {"ATG": 2, "TGA": 1, "GAT": 1}