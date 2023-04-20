def test():
    assert 'abc'.sum == 294, "Should be 294"
    assert '123'.sum == 150, "Should be 150"
    assert 'XYZ'.sum == 267, "Should be 267"
    assert '!@#'.sum == 132, "Should be 132"
    assert ' '.sum == 32, "Should be 32"
    assert ''.sum == 0, "Should be 0"
    assert sum(range(128).m(lambda c:chr(c))*"") ==  sum(range(128)), "Should be equal"
    assert sum(range(99999).m(lambda c:chr(c))*"") ==  sum(range(99999)), "Should be equal"
