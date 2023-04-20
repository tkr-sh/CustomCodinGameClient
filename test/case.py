def test():
    # Camel to snake
    assert "helloWorld".camel_to_snake=="hello_world", "Failed camel to Snake."
    assert "helloWorldIsBack".camel_to_snake=="hello_world_is_back", "Failed camel to Snake."

    # Snake to camel
    assert "hello_world_is_back".snake_to_camel=="helloWorldIsBack", "Failed Snake to camel."