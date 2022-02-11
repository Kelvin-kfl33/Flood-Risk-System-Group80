from Task1E import run

def test_Task1D():
    x,N = run()
    """Test to make sure that the number of stations in any river are less than or equal to the maximum number of stations, i.e. 54"""
    assert x[N][1] <= 54