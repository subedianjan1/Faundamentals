#############Incomplete#########

import pytest

def test_trycatch():
    
    with pytest.raises(Exception) as e:
        assert 1 == 1
    assert str(e.value) == "Invalid email format"
