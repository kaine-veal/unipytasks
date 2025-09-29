from pythontasks.modules.framed_translation import six_frame_translation

# Tests for six_frame_translation function

# Tests a known sequence against expected output
# ATG translates to "M" in frame 1 of the forward strand whereas 
# CAT translates to "H" when reverse complemented in reverse frame 1
def test_small_known_sequence():
    dna = "ATG"
    expected = "Forward\n1 M\nReverse\n1 H"
    result = six_frame_translation(dna)
    assert result == expected 

# Tests for a sequence that is too short
def test_too_short_sequence():
    dna = "AT"  
    result = six_frame_translation(dna)
    assert result == "Forward\nReverse"