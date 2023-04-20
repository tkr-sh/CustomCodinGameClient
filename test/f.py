def test():
    # Test for string
    assert "_ny38EYh".f(isdigit)=="38", "Should be bcd"
    assert "abcDEfEHjajIE".f(isupper)=="DEEHIE", "Should be [1,2,3,4,5]"

    # Test for list
    assert range(15).f(lambda n:n<10)==range(10), "Should be range(10)"
    assert ["2","a", "1e3", "3","4"].f(isdigit)==["2", "3", '4'], "Should be ['2','3','4']"