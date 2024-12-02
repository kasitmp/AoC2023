import os
from functools import reduce


def get_extrapolated_value(values):
  return get_extrapolated_value_recursive(values, [])

def get_extrapolated_value_recursive(values, last_row_items):
  last_row_items.append(values[-1])
  if set(values) == {0}:
    return sum(last_row_items)
  new_values = []
  for i in range(len(values)):
    if i > 0:
      new_values.append(values[i] - values[i - 1])
  return get_extrapolated_value_recursive(new_values, last_row_items)

def get_left_extrapolated_value(values):
  return get_left_extrapolated_value_recursive(values, [])

def get_left_extrapolated_value_recursive(values, first_row_item):
  first_row_item.append(values[0])
  if set(values) == {0}:
    return reduce(lambda x, y: y - x, first_row_item[::-1])
  new_values = []
  for i in range(len(values)):
    if i > 0:
      new_values.append(values[i] - values[i - 1])
  return get_left_extrapolated_value_recursive(new_values, first_row_item)

def result_sum_helper(lines, left = False):
  extrapolated_values = []
  for line in lines:
    list_of_values = [int(x) for x in line.strip().split(" ")]
    if left:
      extrapolated_values.append(get_left_extrapolated_value(list_of_values))
    else:
      extrapolated_values.append(get_extrapolated_value(list_of_values))
  return sum(extrapolated_values)


def main():
  lines = []
  file_name = os.path.join(os.path.dirname(__file__), "input.txt")
  with open(file_name) as f:
    lines = f.readlines()
  # print(f"Part 1: {result_sum_helper(lines)}")
  print(f"Part 2: {result_sum_helper(lines, True)}")

if __name__ == "__main__":
  main()
