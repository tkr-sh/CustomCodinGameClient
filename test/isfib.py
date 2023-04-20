def test():
    # Normal fibonacci
    assert (0).isfib(), "0 Is a fibonacci number"
    assert (1).isfib(), "1 Is a fibonacci number"
    assert (2).isfib(), "2 Is a fibonacci number"
    assert (3).isfib(), "3 Is a fibonacci number"
    assert not (4).isfib(), "4 Is not a fibonacci number"
    assert (5).isfib(), "5 Is a fibonacci number"
    assert not (6).isfib(), "6    Is not a fibonacci number"

    # Weird fibonacci
    assert (0).isfib(0,2), "0 Is a Fibonacci number with a=0 and b=2"
    assert not (1).isfib(0,2), "1 Is not a Fibonacci number with a=0 and b=2"
    assert (2).isfib(0,2), "2 Is a Fibonacci number with a=0 and b=2"
    assert not (3).isfib(0,2), "3 Is not a Fibonacci number with a=0 and b=2"
    assert (4).isfib(0,2), "4 Is a Fibonacci number with a=0 and b=2"

    # Yet another fibonacci
    assert not (0).isfib(3,1), "0 Is NOT a Fibonacci number with a=3 and b=1"
    assert (1).isfib(3,1), "1 Is a Fibonacci number with a=3 and b=1"
    assert not (2).isfib(3,1), "2 Is NOT a Fibonacci number with a=3 and b=1"
    assert (3).isfib(3,1), "3 Is a Fibonacci number with a=3 and b=1"
    assert (4).isfib(3,1), "4 Is a Fibonacci number with a=3 and b=1"
    assert (5).isfib(3,1), "5 Is a Fibonacci number with a=3 and b=1"
