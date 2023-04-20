def test():
    assert "abc".rotate_ord(1) == "bcd", "bcd"
    assert "ABC".rotate_ord(1) == "BCD", "BCD"
    assert "abc".rotate_ord(-1) == "zab", "zab"
    assert "ABC".rotate_ord(-1) == "ZAB", "ZAB"
    assert "UPAnddown".rotate_ord(16) == "KFQdttemd", "UP and down translate of 16"