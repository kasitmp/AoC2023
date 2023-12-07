from aoc_7.aoc_7 import Card, Game, Hand, HandType


class TestCard:
  def test_numeric_value(self):
    card = Card("2")
    assert card.value == 2

  def test_ace_value(self):
    card = Card("A")
    assert card.value == 14

  def test_jack_value(self):
    card = Card("J")
    assert card.value == 11

  def test_joker_value(self):
    card = Card("J", True)
    assert card.value == 1

  def test_queen_value(self):
    card = Card("Q")
    assert card.value == 12

  def test_king_value(self):
    card = Card("K")
    assert card.value == 13

  def test_ten_value(self):
    card = Card("T")
    assert card.value == 10

  def test_repr(self):
    card = Card("T")
    assert repr(card) == "T (10)"

class TestHandType:
  def test_high_card(self):
    cards = [Card("2"), Card("3"), Card("4"), Card("5"), Card("6")]
    hand_type = HandType(cards)
    assert hand_type.value == 1

  def test_five_of_a_kind(self):
    cards = [Card("2"), Card("2"), Card("2"), Card("2"), Card("2")]
    hand_type = HandType(cards)
    assert hand_type.value == 7

  def test_four_of_a_kind(self):
    cards = [Card("3"), Card("2"), Card("2"), Card("2"), Card("2")]
    hand_type = HandType(cards)
    assert hand_type.value == 6

  def test_full_house(self):
    cards = [Card("2"), Card("2"), Card("2"), Card("3"), Card("3")]
    hand_type = HandType(cards)
    assert hand_type.value == 5

  def test_three_of_a_kind(self):
    cards = [Card("2"), Card("2"), Card("2"), Card("3"), Card("4")]
    hand_type = HandType(cards)
    assert hand_type.value == 4

  def test_two_pair(self):
    cards = [Card("2"), Card("2"), Card("3"), Card("3"), Card("4")]
    hand_type = HandType(cards)
    assert hand_type.value == 3

  def test_pair(self):
    cards = [Card("2"), Card("2"), Card("3"), Card("4"), Card("5")]
    hand_type = HandType(cards)
    assert hand_type.value == 2

  def test_joker_upgrades_high_card_to_pair(self):
    cards = [Card("2"), Card("3"), Card("4"), Card("5"), Card("J", True)]
    hand_type = HandType(cards, True)
    assert hand_type.value == 2

  def test_joker_upgrades_pair_to_three_of_a_kind(self):
    cards = [Card("2"), Card("2"), Card("4"), Card("5"), Card("J", True)]
    hand_type = HandType(cards, True)
    assert hand_type.value == 4

  def test_joker_upgrades_two_pair_to_full_house(self):
    cards = [Card("2"), Card("2"), Card("3"), Card("3"), Card("J", True)]
    hand_type = HandType(cards, True)
    assert hand_type.value == 5

  def test_joker_upgrades_three_of_a_kind_to_four_of_a_kind(self):
    cards = [Card("2"), Card("2"), Card("2"), Card("3"), Card("J", True)]
    hand_type = HandType(cards, True)
    assert hand_type.value == 6

  def test_joker_upgrades_full_house_to_five_of_a_kind(self):
    cards = [Card("2"), Card("2"), Card("2"), Card("J"), Card("J", True)]
    hand_type = HandType(cards, True)
    assert hand_type.value == 7

  def test_joker_upgrades_four_of_a_kind_to_five_of_a_kind(self):
    cards = [Card("2"), Card("2"), Card("2"), Card("2"), Card("J", True)]
    hand_type = HandType(cards, True)
    assert hand_type.value == 7

  def test_all_joker_upgrades_to_five_of_a_kind(self):
    cards = [Card("J", True), Card("J", True), Card("J", True), Card("J", True), Card("J", True)]
    hand_type = HandType(cards, True)
    assert hand_type.value == 7

class TestGame:
  def test_order_by_hand_type(self):
    cards1 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("A")]
    hand1 = Hand(cards1, 1)
    cards2 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("5")]
    hand2 = Hand(cards2, 2)
    game = Game([hand2, hand1])
    assert game.hands == [hand1, hand2]

  def test_order_by_hand_card_value_first_difference(self):
    cards1 = [Card("K"), Card("A"), Card("A"), Card("A"), Card("K")]
    hand1 = Hand(cards1, 1)
    cards2 = [Card("A"), Card("K"), Card("K"), Card("A"), Card("K")]
    hand2 = Hand(cards2, 2)
    game = Game([hand1, hand2])
    assert game.hands == [hand2, hand1]

  def test_order_by_hand_card_value_second_difference(self):
    cards1 = [Card("A"), Card("A"), Card("A"), Card("K"), Card("K")]
    hand1 = Hand(cards1, 1)
    cards2 = [Card("A"), Card("K"), Card("K"), Card("A"), Card("K")]
    hand2 = Hand(cards2, 2)
    game = Game([hand2, hand1])
    assert game.hands == [hand1, hand2]

  def test_order_by_hand_card_value_third_difference(self):
    cards1 = [Card("A"), Card("A"), Card("A"), Card("K"), Card("K")]
    hand1 = Hand(cards1, 1)
    cards2 = [Card("A"), Card("A"), Card("K"), Card("A"), Card("K")]
    hand2 = Hand(cards2, 2)
    game = Game([hand2, hand1])
    assert game.hands == [hand1, hand2]

  def test_order_by_hand_card_value_fourth_difference(self):
    cards1 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("K")]
    hand1 = Hand(cards1, 1)
    cards2 = [Card("A"), Card("A"), Card("A"), Card("K"), Card("A")]
    hand2 = Hand(cards2, 2)
    game = Game([hand2, hand1])
    assert game.hands == [hand1, hand2]

  def test_order_by_hand_card_value_fifth_difference(self):
    cards1 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("K")]
    hand1 = Hand(cards1, 1)
    cards2 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("Q")]
    hand2 = Hand(cards2, 2)
    game = Game([hand2, hand1])
    assert game.hands == [hand1, hand2]

  def test_order_stays_when_exactly_same_hand(self):
    cards1 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("K")]
    hand1 = Hand(cards1, 1)
    cards2 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("K")]
    hand2 = Hand(cards2, 2)
    game = Game([hand2, hand1])
    assert game.hands[0].bid == 2
    assert game.hands[1].bid == 1

  def test_total_winnings(self):
    cards1 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("K")]
    hand1 = Hand(cards1, 5)
    cards2 = [Card("A"), Card("A"), Card("A"), Card("A"), Card("Q")]
    hand2 = Hand(cards2, 10)
    game = Game([hand2, hand1])
    assert game.total_winnings() == 20

