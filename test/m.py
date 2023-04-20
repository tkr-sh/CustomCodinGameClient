def test():
    # Test for string
    assert "abc".m(lambda c:chr(ord(c)+1))=="bcd", "Should be bcd"
    assert "abcde".m(lambda c:ord(c)&31)==[1,2,3,4,5], "Should be [1,2,3,4,5]"

    # Test for list
    assert [1,2,3].m(lambda n:n+1)==[2,3,4], "Should be [2,3,4]"
    assert ["2","3","4"].m(int)==[2,3,4], "Should be [2,3,4]"