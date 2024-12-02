import os

import pytest

from aoc_2.aoc_2 import (
  MAX_BLUE,
  MAX_GREEN,
  MAX_RED,
  count_possible_games,
  count_power_of_games,
  is_possible_game,
  parse_game,
  parse_line,
  power_of_game,
)

TEMP_FIXTURE_FOLDER = os.path.join(os.path.dirname(__file__), "temp_fixtures")
DEFAULT_FILE_NAME = f"{TEMP_FIXTURE_FOLDER}/test.txt"

class TestCountPossibleGames:
  def test_with_empty_list(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [""])
    assert count_possible_games(DEFAULT_FILE_NAME) == 0

  def test_with_single_allowed_item_list(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, ["Game 1: 1 blue"])
    assert count_possible_games(DEFAULT_FILE_NAME) == 1

  def test_with_single_not_allowed_item_list(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [f"Game 1: {MAX_BLUE + 1} blue"])
    assert count_possible_games(DEFAULT_FILE_NAME) == 0

  def test_with_single_allowed_item_list_and_single_sets(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, ["Game 1: 1 blue, 1 red, 1 green"])
    assert count_possible_games(DEFAULT_FILE_NAME) == 1

  def test_with_not_allowed_item_list_and_single_sets(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [
      f"Game 1: 1 blue, {MAX_RED + 1} red, 1 green"])
    assert count_possible_games(DEFAULT_FILE_NAME) == 0

  def test_with_not_allowed_item_list_green_and_single_sets(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [
      f"Game 1: 1 blue, 5 red, {MAX_GREEN + 1} green"])
    assert count_possible_games(DEFAULT_FILE_NAME) == 0

  def test_with_single_noe_allowed_item_list_and_multiple_sets(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [
      f"Game 1: 1 blue, 1 red, 1 green; {MAX_GREEN + 1} green"])
    assert count_possible_games(DEFAULT_FILE_NAME) == 0

  def test_with_multiple_games(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [
      "Game 1: 1 blue, 1 red, 1 green",
      "Game 2: 1 blue, 1 red, 1 green",
      "Game 3: 1 blue, 1 red, 1 green",
    ])
    assert count_possible_games(DEFAULT_FILE_NAME) == 6

  def test_with_instruction_example(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [
      "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
      "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ])
    assert count_possible_games(DEFAULT_FILE_NAME) == 8

  @pytest.fixture(scope='function', autouse=True)
  def clean_fixture_files(self):
    yield
    # Will be executed after the last test
    for file in os.listdir(TEMP_FIXTURE_FOLDER):
      os.remove(os.path.join(TEMP_FIXTURE_FOLDER, file))

  def create_file_from_list(self, file_name, list):
    with open(file_name, "w") as f:
      for item in list:
        f.write("%s\n" % item)

class TestCountPowerOfGames:
  def test_count_power_of_games_with_empty_list(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [""])
    assert count_power_of_games(DEFAULT_FILE_NAME) == 0

  def test_count_power_of_games_with_single_item_list(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, ["Game 1: 2 blue"])
    assert count_power_of_games(DEFAULT_FILE_NAME) == 2

  def test_count_power_of_games_with_full_item_set(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, ["Game 1: 2 blue, 3 red, 4 green"])
    assert count_power_of_games(DEFAULT_FILE_NAME) == 24

  def test_count_power_of_games_with_multiple_sets(self):
    self.create_file_from_list(DEFAULT_FILE_NAME,
      ["Game 1: 2 blue, 3 red, 4 green; 1 blue, 3 red, 6 green"])
    assert count_power_of_games(DEFAULT_FILE_NAME) == 36

  def test_count_power_of_games_with_instruction_example(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, [
      "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
      "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ])
    assert count_power_of_games(DEFAULT_FILE_NAME) == 2286

  @pytest.fixture(scope='function', autouse=True)
  def clean_fixture_files(self):
    yield
    # Will be executed after the last test
    for file in os.listdir(TEMP_FIXTURE_FOLDER):
      os.remove(os.path.join(TEMP_FIXTURE_FOLDER, file))

  def create_file_from_list(self, file_name, list):
    with open(file_name, "w") as f:
      for item in list:
        f.write("%s\n" % item)

class TestPowerOfGame:
  def test_power_of_game_with_empty_list(self):
    assert power_of_game("") == 0

  def test_power_of_game_with_single_item_list(self):
    assert power_of_game("Game 1: 2 blue") == 2

  def test_power_of_game_with_full_item_set(self):
    assert power_of_game("Game 1: 2 blue, 3 red, 4 green") == 24

  def test_power_of_game_with_multiple_sets(self):
    assert power_of_game("Game 1: 2 blue, 3 red, 4 green; 1 blue, 3 red, 6 green") == 36

class TestIsPossibleGame:
  def test_is_possible_game_with_empty_list(self):
    assert is_possible_game("") == 0

  def test_is_possible_game_with_single_allowed_item_list(self):
    assert is_possible_game("Game 1: 1 blue") == 1

  def test_is_possible_game_with_single_not_allowed_item_list(self):
    assert is_possible_game(f"Game 1: {MAX_BLUE + 1} blue") == 0

  def test_is_possible_game_with_single_allowed_item_list_and_single_sets(self):
    assert is_possible_game("Game 1: 1 blue, 1 red, 1 green") == 1

  def test_is_possible_game_with_not_allowed_item_list_and_single_sets(self):
    assert is_possible_game(f"Game 1: 1 blue, {MAX_RED + 1} red, 1 green") == 0

  def test_is_possible_game_with_not_allowed_item_list_green_and_single_sets(self):
    assert is_possible_game(f"Game 1: 1 blue, 5 red, {MAX_GREEN + 1} green") == 0

  def test_is_possible_game_with_single_noe_allowed_item_list_and_multiple_sets(self):
    assert is_possible_game(
      f"Game 1: 1 blue, 1 red, 1 green; {MAX_GREEN + 1} green") == 0

  def test_is_possible_game_to_return_game_id(self):
    assert is_possible_game("Game 2: 1 blue, 1 red, 1 green") == 2

class TestParseLine:
  def test_parse_line_with_empty_set(self):
    assert parse_line("Game 1:") == {
      "game": 1,
      "sets": [
      ]
    }

  def test_actual_game_number_is_taken(self):
    assert parse_line("Game 2:") == {
      "game": 2,
      "sets": [
      ]
    }

  def test_with_broken_string(self):
    assert parse_line("Game 1") is None

  def test_parse_line_with_single_set_and_one_color(self):
    assert parse_line("Game 2: 1 blue") == {
      "game": 2,
      "sets": [
        {
          "blue": 1
        }
      ]
    }

  def test_parse_line_with_single_set_and_all_colors(self):
    assert parse_line("Game 2: 1 blue, 2 red, 4 green") == {
      "game": 2,
      "sets": [
        {
          "blue": 1,
          "red": 2,
          "green": 4
        }
      ]
    }

  def test_parse_line_with_multiple_sets_and_one_color(self):
    assert parse_line("Game 2: 1 blue, 2 red; 3 green") == {
      "game": 2,
      "sets": [
        {
          "blue": 1,
          "red": 2
        },
        {
          "green": 3
        }
      ]
    }

class TestParseGame:
  def test_parse_game_with_minimal_valid_string(self):
    assert parse_game("Game 1:") == 1

  def test_parse_game_with_valid_string(self):
    assert parse_game("Game 2: 1 blue") == 2

  def test_parse_game_without_colon(self):
    assert parse_game("Game 1") is None

  def test_parse_game_with_broken_string(self):
    assert parse_game("Gae 1:") is None

  def test_parse_game_without_digit(self):
    assert parse_game("Game a:") is None
