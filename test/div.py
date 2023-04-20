def test():
    assert 'abcde'/'abc' == "de", "Should be 'de'"
    assert 'abcdefghijkl'/'def' == "abcghijkl", "Should be 'abcghijkl'"
    assert range(97,123).m(chr)*""/'abcxyz' == range(100,120).m(chr)*"", "Should be range(100,120)"