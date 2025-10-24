from pythontasks.modules.genbank_chunk_dna import genbank_chunk_dna

def test_basic_formatting():
    input_seq = "ATGCGTACGTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG"
    expected = (
        "        1 atgcgtacgt cgatcgatcg atcgatcgat cgatcgatcg atcgatcgat cgatcgatcg"
    )
    assert genbank_chunk_dna(input_seq) == expected

def test_line_wrapping():
    # 120 bases should produce two lines (default line_width = 60)
    input_seq = "A" * 120
    output = genbank_chunk_dna(input_seq)
    lines = output.split("\n")
    assert len(lines) == 2
    assert lines[0].startswith("        1")
    assert lines[1].startswith("       61")