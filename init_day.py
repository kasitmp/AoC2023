import os
import requests
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


FOLDER = os.path.dirname(__file__)
AOC_URL = "https://adventofcode.com/2023/day/"

def init_day():
  input_day = int(input("Which Advent of Code day do you want to initialize? (1-25)"))
  folder = os.path.join(FOLDER, f"aoc_{input_day}")
  if os.path.exists(folder):
    print(f"Folder aoc_{input_day} already exists")
    exit(1)
  os.mkdir(folder)
  Path(folder, f"aoc_{input_day}.py").touch()
  Path(folder, f"test_aoc_{input_day}.py").touch()
  Path(folder, "test_input.txt").touch()
  Path(folder, "input.txt").touch()
  Path(folder, "__init__.py").touch()

  url = f"{AOC_URL}{input_day}/input"
  aoc_response = requests.get(url, cookies={"session": os.getenv("SESSION_COOKIE")}, stream=True)
  with open(os.path.join(folder, "input.txt"), 'wb') as f:
    for chunk in aoc_response:
      f.write(chunk)

def main():
  init_day()

if __name__ == "__main__":
  main()


