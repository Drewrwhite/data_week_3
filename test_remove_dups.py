import pytest
from main import remove_dups

def test_empty_arg():
    with pytest.raises(Exception) as e:
        remove_dups()

@pytest.mark.parametrize("list1, expected_result", [
([1, 3, 5], [1, 3, 5]), 
([3, 9, 9], [3, 9]), 
(["x", "y", "z"], ["x", "y", "z"]), 
(["x", "y", "y"], ["x", "y"]),
([], []),
("hello", ["h", "e", "l", "o"]),
(None, "Empty"),

])
def test_remove_dups(list1, expected_result):
  assert remove_dups(list1) == expected_result
