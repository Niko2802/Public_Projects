from Akkerman import akkerman


def test_1():
    assert akkerman(1,1) == 3

def test_2():
    assert akkerman(1,2) == 4

def test_3():
    assert akkerman(1,3) == 5

def test_4():
    assert akkerman(2,1) == 5

def test_5():
    assert akkerman(2,2) == 7

def test_6():
    assert akkerman(2,3) == 9

def test_7():
    assert akkerman(3,5) == 253
