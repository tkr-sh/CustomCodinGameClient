def test():
    # Test for string
    assert "_ny38EYhds".cnt(lambda c:ord(c)<100)==5, "Should be 5"
    assert "afdqfqfdqdfqfdbcdef".cnt(lambda c: c in "abc")==3, "Should be 3"
    assert "aaabcad".cnt("a")==4, "Should be 4"
