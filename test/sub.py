def test():
    # Test for string
    assert "abc"-1, "Should be ab"
    assert "abcde"-2, "Should be abc"

    # Test for list
    assert [1,2,3]-1, "Should be 1, 2"
    assert [1,2,3,4,5]-2, "Should be 1, 2, 3"