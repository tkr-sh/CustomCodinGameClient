def test():
    assert "rotate" == "rotate".rotate(0), "rotate"
    assert "erotat" == "rotate".rotate(1), "erotat"
    assert "terota" == "rotate".rotate(2), "terota"
    assert "otater" == "rotate".rotate(-1), "otater"
    assert "tatero" == "rotate".rotate(-2), "tatero"