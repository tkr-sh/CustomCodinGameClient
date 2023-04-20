def test():
    assert "abcd".n_split(2) == ["ab", "cd"], "ab, cd"
    assert "abc".n_split(2) == ["ab", "c"], "ab, c"
    assert "abc".n_split(5) == ["abc"], "abc"
    assert "abc".n_split(-1) == [], "Empty array when negative"
    assert "abc".n_split(1) == ["a", "b", "c"], "a, b, c"
    assert ((65@91).m(chr)*"").n_split(2)[-1] == "YZ", "Last two char"