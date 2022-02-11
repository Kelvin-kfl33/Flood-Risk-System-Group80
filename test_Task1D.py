from Task1D import run

def test_Task1D():
    a,b,c,d = run()
    """To check the length of each list output"""
    assert len(a) == 10
    assert len(b) == 24
    assert len(c) == 7 
    assert len(d) == 54