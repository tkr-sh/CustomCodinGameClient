def test():
    # 42 = 0b101010
    assert 42[0] == 0, "42 - First"
    assert 42[1] == 1, "42 - Second"
    assert 42[2] == 0, "42 - Third"
    assert 42[3] == 1, "42 - Forth"
    assert 42[4] == 0, "42 - Fifth"
    assert 42[5] == 1, "42 - Six"

    # 31 = 0b11111
    assert 31[0] == 1, "31 - First"
    assert 31[1] == 1, "31 - Second"
    assert 31[2] == 1, "31 - Third"
    assert 31[3] == 1, "31 - Forth"
    assert 31[4] == 1, "31 - Fifth"

