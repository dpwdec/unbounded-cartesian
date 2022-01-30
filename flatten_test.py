from main import flatten

def test_flatten():
    result = flatten([[1, 2, 3], [4, 5, 6], [7, [8, 9]]])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]