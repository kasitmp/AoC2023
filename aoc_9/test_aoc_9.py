from aoc_9.aoc_9 import (
  get_extrapolated_value,
  get_left_extrapolated_value,
  result_sum_helper,
)


class TestGetExtrapolatedValue:
  def test_minimal_example(self):
    assert get_extrapolated_value([1, 1]) == 1
  def test_regular_example(self):
    assert get_extrapolated_value([0, 3, 6, 9, 12, 15]) == 18

class TestGetLeftExtrapolatedValue:
  def test_minimal_example(self):
    assert get_left_extrapolated_value([1, 1]) == 1
  def test_regular_example(self):
    assert get_left_extrapolated_value([10, 13, 16, 21, 30, 45]) == 5

class TestResultSumHelper:
  def test_single_row_example(self):
    assert result_sum_helper(["2 2"]) == 2
  def test_multi_row_example(self):
    assert result_sum_helper(["0 3 6 9 12 15", "2 2"]) == 20
  def test_multi_row_example_left(self):
    assert result_sum_helper(["10 13 16 21 30 45", "2 2"], True) == 7
  def test_special_example_left(self):
    assert result_sum_helper(["1 3 6 10 15 21"], True) == 0
