import os
from dataclasses import dataclass


@dataclass
class Number:
  row: int
  columnstart: int
  columnend: int
  value: str
  is_tile: bool = False

@dataclass
class Symbol:
  row: int
  column: int
  symbol: str

@dataclass
class Gear:
  attached_numbers: int = 0
  ratio: int = 0

def check_is_tile(array, number: Number):
  return search_symbols_around_number_function(
    array, number, lambda x: x != "." and not x.isdigit()) != []

def search_symbols_around_number_function(array, number, detector_function):
  symbols = []
  for row in range(number.row - 1, number.row + 2):
    if row >= 0 and row < len(array):
      for column in range(number.columnstart - 1, number.columnend + 2):
        if (column >= 0
            and column < len(array[number.row])
            and detector_function(array[row][column])):
              symbols.append(Symbol(row, column, array[row][column]))
  return symbols

def parse_for_tile_numbers(array):
  numbers = []
  tmp_number = None
  for row_index, row in enumerate(array):
    for column, value in enumerate(row):
      if value.isdigit():
        if tmp_number is None:
          tmp_number = Number(row_index, column, column, value)
        else:
          tmp_number.columnend = column
          tmp_number.value += value
      else:
        if tmp_number is not None:
          tmp_number.is_tile = check_is_tile(array, tmp_number)
          numbers.append(tmp_number)
          tmp_number = None
    if tmp_number is not None:
      tmp_number.is_tile = check_is_tile(array, tmp_number)
      numbers.append(tmp_number)
      tmp_number = None
  return numbers

def sum_up_tiles(numbers):
  return sum([int(number.value) for number in numbers if number.is_tile])

# Too lazy to TDD this one, sorry karma
def calculate_gears(array, numbers):
  gears = [[0 for x in range(len(array))] for y in range(len(array[0]))]
  for tile in [number for number in numbers if number.is_tile]:
    gear_symbols = search_symbols_around_number_function(
      array, tile, lambda x: x == "*")
    for gear_symbol in gear_symbols:
      if gears[gear_symbol.row][gear_symbol.column] == 0:
        gears[gear_symbol.row][gear_symbol.column] = Gear(1, int(tile.value))
      else:
        gears[gear_symbol.row][gear_symbol.column].attached_numbers += 1
        gears[gear_symbol.row][gear_symbol.column].ratio *= int(tile.value)
  flat_gear_list = [j for sub in gears for j in sub]
  return sum(
    gear.ratio for gear in flat_gear_list if gear != 0 and gear.attached_numbers >= 2)

def load_into_2d_array(file_name):
  with open(file_name) as f:
    return [list(line.strip()) for line in f.readlines()]

def main():
  input_array = load_into_2d_array(os.path.join(os.path.dirname(__file__), "input.txt"))
  print("Day 3")
  print(
    f"Part 1: {sum_up_tiles(parse_for_tile_numbers(input_array))}")
  print(
    f"Part 2: {calculate_gears(input_array, parse_for_tile_numbers(input_array))}")

if __name__ == "__main__":
  main()
