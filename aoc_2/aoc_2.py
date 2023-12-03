MAX_BLUE = 14
MAX_GREEN = 13
MAX_RED = 12

def count_possible_games(file_name: str) -> int:
  with open(file_name) as f:
    lines = f.readlines()
  return sum([is_possible_game(line) for line in lines])

def count_power_of_games(file_name: str) -> int:
  with open(file_name) as f:
    lines = f.readlines()
  return sum([power_of_game(line) for line in lines])

def power_of_game(line: str) -> int:
  game_dict = parse_line(line)
  if game_dict is not None:
    need_blue = 1
    need_red = 1
    need_green = 1
    for set in game_dict["sets"]:
      if "blue" in set:
        need_blue = max(set["blue"], need_blue)
      if "green" in set:
        need_green = max(set["green"], need_green)
      if "red" in set:
        need_red = max(set["red"], need_red)
    return need_blue * need_green * need_red
  return 0

def is_possible_game(line: str) -> int:
  game_dict = parse_line(line)
  if game_dict is not None:
    for set in game_dict["sets"]:
      if "blue" in set and set["blue"] > MAX_BLUE:
        return 0
      if "green" in set and set["green"] > MAX_GREEN:
        return 0
      if "red" in set and set["red"] > MAX_RED:
        return 0
    return game_dict["game"]
  return 0



def parse_line(line: str):
  if parse_game(line) is not None:
    sets_str = line.split(":")[1].strip()
    seperate_sets = sets_str.split(";")
    sets = []
    for set in seperate_sets:
      set_colors_dict = parse_set_colors(set)
      if set_colors_dict != {}:
        sets.append(set_colors_dict)
    return {"game": parse_game(line), "sets": sets}
  return None

def parse_set_colors(line: str):
  set_colors_dict = {}
  set_colors = line.split(",")
  for set_color in set_colors:
    if set_color.find("blue") > -1:
      set_colors_dict["blue"] = int(set_color.replace("blue", "").strip())
    if set_color.find("red") > -1:
        set_colors_dict["red"] = int(set_color.replace("red", "").strip())
    if set_color.find("green") > -1:
        set_colors_dict["green"] = int(set_color.replace("green", "").strip())
  return set_colors_dict

def parse_game(line: str) -> int:
  split_str = line.split(":")
  if len(split_str) > 1 and split_str[0].startswith("Game "):
    game_str = split_str[0]
    if (game_str[5:].isdigit()):
      return int(game_str[5:])
  return None

def main():
  print("Day 1")
  print(f"Part 1: {count_possible_games('input.txt')}")
  print(f"Part 2: {count_power_of_games('input.txt')}")

if __name__ == "__main__":
  main()
