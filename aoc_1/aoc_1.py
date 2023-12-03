def transform_words_to_numbers(string: str) -> list:
  translation_dict_list = [
    ("one", "o1e"),
    ("two", "t2o"),
    ("three", "t3e"),
    ("four", "f4r"),
    ("five", "f5e"),
    ("six", "s6x"),
    ("seven", "s7n"),
    ("eight", "e8t"),
    ("nine", "n9e")]
  for item in translation_dict_list:
    string = string.replace(item[0], item[1])
  return string

def calibration_value_sum(list: [str]) -> int:
  if len(list) == 0 or list[0] == "":
    return None
  integer_list = []
  for x in list:
    # filter string to only include digits
    item = ''.join(filter(str.isdigit, x))
    if len(item) > 0:
      integer_list.append(f"{item[0]}{item[-1]}")
  return sum([int(x) for x in integer_list if x.isdigit()])

def calibration_value_sum_two(list: [str]) -> int:
  return calibration_value_sum([transform_words_to_numbers(item) for item in list])

def input_lines_to_list(file_name):
  with open(file_name) as f:
      lines = f.readlines()
  return [x.strip() for x in lines]

def main():
  print("Day 1")
  print(f"Part 1: {calibration_value_sum(input_lines_to_list('input.txt'))}")
  print(f"Part 2: {calibration_value_sum_two(input_lines_to_list('input.txt'))}")

if __name__ == "__main__":
    main()


