import os


def get_card_points(card, pow_rule = True):
  winning_numbers = card.split("|")[0].split(":")[1].split()
  drawn_numbers = card.split("|")[1].split()
  points = len(set(winning_numbers).intersection(set(drawn_numbers)))
  if points > 1 and pow_rule:
    return pow(2, (points - 1))
  else:
    return points

def get_scratchcard_pile(cards):
  pile = list(range(len(cards)))
  for index, card_id in enumerate(pile):
    points = get_card_points(cards[card_id], False)
    if points > 0:
      for i in range(points):
        pile.insert(index+1, card_id + i + 1)
  return pile


def calculate_points_for_file(file):
  with open(file) as f:
    return sum([get_card_points(line) for line in f.readlines()])

def calculate_scratchcard_pile_for_file(file):
  with open(file) as f:
    return len(get_scratchcard_pile([line for line in f.readlines()]))

def main():
  file = os.path.join(os.path.dirname(__file__), "input.txt")
  print("Day 4")
  print(f"Part 1: {calculate_points_for_file(file)}")
  print(f"Part 2: {calculate_scratchcard_pile_for_file(file)}")

if __name__ == "__main__":
  main()
