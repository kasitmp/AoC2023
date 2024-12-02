import os
from math import gcd


def follow_instructions(instructions, dict, start="AAA"):
  pointer = dict.get(start)
  steps = 0
  while(True):
    index = steps % len(instructions)
    if (index == 0):
      print(f"Steps: {steps}")
    instruction = instructions[index]
    if instruction == "L":
      pointer_value = pointer[0]
    elif instruction == "R":
      pointer_value = pointer[1]
    steps+=1
    if pointer_value[2] == "Z":
      return steps
    pointer = dict.get(pointer_value)

def follow_complex_instructions(instructions, dict, lookup):
  pointer_array = lookup.get("A")
  steps_list = []

  for pointer in pointer_array:
    steps = follow_instructions(instructions, dict, pointer)
    steps_list.append(steps)
  return least_common_multiple(steps_list)

def set_dict(lines):
  dict = {}
  for line in lines:
    dict[line[0:3]] = (line[7:10], line[12:15])
  return dict

def set_complex_dict(lines):
  dict = {}
  lookup = {"A": []}
  for line in lines:
    key = line[0:3]
    value = (line[7:10], line[12:15])
    dict[key] = value
    lookup_key = key[2]

    if lookup_key == "A":
      lookup[lookup_key].append(key)

  return (dict, lookup)

def least_common_multiple(steps):
  lcm = 1
  for i in steps:
      lcm = lcm*i//gcd(lcm, i)
  return lcm


def main():
  file_name = os.path.join(os.path.dirname(__file__), 'input.txt')
  with open(file_name) as f:
    lines = f.readlines()

  instructions = lines[0].strip()
  dict = set_dict(lines[2:])

  print("Part 1: ", follow_instructions(instructions, dict))

  dict, lookup = set_complex_dict(lines[2:])
  print("Part 2: ", follow_complex_instructions(instructions, dict, lookup))
if __name__ == "__main__":
  main()
