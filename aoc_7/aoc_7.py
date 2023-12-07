import os


class Card:
  def __init__(self, name: str, with_jokers: bool = False):
    self.name = name
    self.with_jokers = with_jokers
    self.value = self._calculate_value()

  def _calculate_value(self):
    if self.name.isnumeric():
      return int(self.name)
    switcher = {
      "A": 14,
      "J": 11,
      "Q": 12,
      "K": 13,
      "T": 10
    }
    if self.with_jokers:
      switcher["J"] = 1
    return switcher.get(self.name)

  def __repr__(self):
    return f"{self.name} ({self.value})"

  def __eq__(self, other):
    return self.value == other.value

  def __hash__(self):
    return hash(self.value)

class Hand:
  def __init__(self, cards: [Card], bid: int, with_jokers: bool = False):
    self.cards = cards
    self.hand_type = HandType(cards, with_jokers=with_jokers)
    self.bid = bid

  def __repr__(self):
    return f"{self.cards}"

class HandType:
  def __init__(self, cards: [Card], with_jokers: bool = False):
    self.cards = cards
    self.with_jokers = with_jokers
    self.value = self._calculate_value()

  def _calculate_value(self):
    counted_card_dict = {}
    for card in self.cards:
      counted_card_dict[card.name] = counted_card_dict.get(card.name, 0) + 1
    ordered_counted_card_dict = dict(sorted(counted_card_dict.items(), key=lambda item: item[1], reverse=True))

    if self.with_jokers and 0 < ordered_counted_card_dict.get("J", 0) < 5:
      joker_count = ordered_counted_card_dict.pop("J")
      init_dict = list(ordered_counted_card_dict.keys())[0]
      ordered_counted_card_dict[init_dict] = ordered_counted_card_dict.get(init_dict, 0) + joker_count

    if list(ordered_counted_card_dict.values())[0] == 5:
      return 7
    if list(ordered_counted_card_dict.values())[0] == 4:
      return 6
    if list(ordered_counted_card_dict.values())[0] == 3 and list(ordered_counted_card_dict.values())[1] == 2:
      return 5
    if list(ordered_counted_card_dict.values())[0] == 3:
      return 4
    if list(ordered_counted_card_dict.values())[0] == 2 and list(ordered_counted_card_dict.values())[1] == 2:
      return 3
    if list(ordered_counted_card_dict.values())[0] == 2:
      return 2

    return 1

class Game:
  def __init__(self, hands: [Hand]):
    self.hands = hands
    self.hands.sort(key=lambda hand: (
      hand.hand_type.value,
      hand.cards[0].value,
      hand.cards[1].value,
      hand.cards[2].value,
      hand.cards[3].value,
      hand.cards[4].value), reverse=True)

  def total_winnings(self):
    total = 0
    length = len(self.hands)
    for i in range(length):
      total += self.hands[i].bid * (length - i)
    return total

def setup_part_one(lines: list):
  hands = []
  for line in lines:
    raw_cards, bid = line.strip().split()
    cards = [Card(card) for card in list(raw_cards)]
    hands.append(Hand(cards, int(bid)))
  game = Game(hands)
  return game

def setup_part_two(lines: list):
  hands = []
  for line in lines:
    raw_cards, bid = line.strip().split()
    cards = [Card(card, True) for card in list(raw_cards)]
    hands.append(Hand(cards, int(bid), True))
  game = Game(hands)
  return game


def main():
  file_name = os.path.join(os.path.dirname(__file__), "input.txt")
  with open(file_name) as f:
    lines = f.readlines()

  game_one = setup_part_one(lines)
  game_two = setup_part_two(lines)
  print(f"Part 1: {game_one.total_winnings()}")
  print(f"Part 2: {game_two.total_winnings()}")

if __name__ == "__main__":
  main()
