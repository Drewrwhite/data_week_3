import pytest
from main import remove_dups

def test_empty_arg():
  """ Test for empty arguments and passes over as empty

  """
  with pytest.raises(Exception) as e:
      assert remove_dups() == "Empty"

# test multiple arguments in one test checks for duplicates, different data types and no argument
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
  """ tests remove_dups by comparing with expected result

  Args:
      list1 (list): list argument
      expected_result (list): list with duplicates removed
  """
  assert (remove_dups(list1)) == expected_result