from Task1B import run

def test_Task1B():
    A,B = run()
    """To test the length of the two lists are both correct"""
    assert len(A) == 10
    assert len(B) == 10
