def test():
    # Test for string
    assert "abc".rm("a"), "Should be bc"
    assert "abcde".rm(["d","e","f"]), "Should be abc"

    # Test for list
    assert [1,2,3].rm(1), "Should be 2, 3"
    assert [1,2,3,4,5].rm([4,5,6]), "Should be 1, 2, 3"