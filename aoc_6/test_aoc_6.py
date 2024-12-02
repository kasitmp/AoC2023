from aoc_6.aoc_6 import parse_input, race_options


class TestRaceOptions:
  def test_example(self):
    assert race_options(7, 9) == 4

  def test_example_two(self):
    assert race_options(15, 40) == 8

  def test_example_three(self):
    assert race_options(30, 200) == 9

class TestParseInput:
  def test_example(self):
    assert parse_input(["Time:      7  15   30","Distance:  9  40  200"]) == [(7, 9), (15, 40), (30, 200)]

