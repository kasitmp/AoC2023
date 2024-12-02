import os
from math import prod


def race_options(time: int, distance: int):
  options = 0
  for i in range(time):
    if (time - i) * i > distance:
      options += 1
  return options

def parse_input(lines: list):
  times = lines[0].split(":")[1].split()
  distances = lines[1].split(":")[1].split()
  return [(int(times[i]), int(distances[i])) for i in range(len(times))]

def get_options_for_part_one(lines: list):
  parsed_input = parse_input(lines)
  options = []
  for tuple in parsed_input:
    options.append(race_options(tuple[0], tuple[1]))
  return prod(options)

def get_options_for_part_two(lines: list):
  time = int(lines[0].split(":")[1].replace(" ", ""))
  distance = int(lines[1].split(":")[1].replace(" ", ""))
  return race_options(time, distance)

def main():
  file_name = os.path.join(os.path.dirname(__file__), "input.txt")
  with open(file_name) as f:
    lines = f.readlines()

  print("Day 6")
  print(f"Part 1: {get_options_for_part_one(lines)}")
  print(f"Part 2: {get_options_for_part_two(lines)}")

if __name__ == "__main__":
  main()
