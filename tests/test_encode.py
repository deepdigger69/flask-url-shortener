from app import encode

def test_encode():
    assert encode(0) == '0'
    assert encode(62) == '10'
