from aoc_4.aoc_4 import get_card_points, get_scratchcard_pile


class TestGetCardPoints:
  def test_card_has_one_winning_number(self):
    assert get_card_points("Card 1: 40 | 40") == 1

  def test_card_has_no_winning_number(self):
    assert get_card_points("Card 1: 40 | 41") == 0

  def test_card_has_two_winning_numbers(self):
    assert get_card_points("Card 1: 39 40 | 39 40") == 2

  def test_card_has_subset_of_winning_numbers(self):
    assert get_card_points("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == 8

class TestGetScratchcardPile:
  def test_card_has_one_winning_number(self):
    assert get_scratchcard_pile(["Card 1: 40 | 40", "Card 2: 40 | 39"]) == [0, 1, 1]
