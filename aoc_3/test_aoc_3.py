
import os

import pytest

from aoc_3.aoc_3 import (
  Number,
  check_is_tile,
  load_into_2d_array,
  parse_for_tile_numbers,
  sum_up_tiles,
)

TEMP_FIXTURE_FOLDER = os.path.join(os.path.dirname(__file__), "temp_fixtures")
DEFAULT_FILE_NAME = f"{TEMP_FIXTURE_FOLDER}/test.txt"

class TestSumUpTiles:
  def test_with_empty_list(self):
    assert sum_up_tiles([]) == 0

  def test_with_one_tile(self):
    assert sum_up_tiles([Number(0, 0, 0, "1", True)]) == 1

  def test_with_no_tile(self):
    assert sum_up_tiles([Number(0, 0, 0, "1", False)]) == 0


class TestCheckIsTile:
  def test_symbol_in_front(self):
    assert check_is_tile([[".", "$", "1", "2", "3"]], Number(0, 2, 4, "123")) is True

  def test_no_symbol_around(self):
    assert check_is_tile([["1", "2", "3"]], Number(0, 0, 2, "123")) is False

  def test_no_symbol_around_but_space(self):
    assert check_is_tile([[".", "1", "2", "3", "."]], Number(0, 1, 3, "123")) is False

  def test_symbol_top_left(self):
    assert check_is_tile([["$", ".", ".", "."],
                          [".", "2", "3", "."]], Number(1, 1, 2, "23")) is True

  def test_symbol_top_right(self):
    assert check_is_tile([[".", ".", ".", "$"],
                          [".", "2", "3", "."]], Number(1, 1, 2, "23")) is True

  def test_symbol_bottom_left(self):
    assert check_is_tile([[".", "2", "3", "."],
                          ["$", ".", ".", "."]], Number(0, 1, 2, "23")) is True

  def test_symbol_bottom_right(self):
    assert check_is_tile([[".", "2", "3", "."],
                          [".", ".", ".", "$"]], Number(0, 1, 2, "23")) is True

  def test_symbol_top(self):
    assert check_is_tile([[".", ".", "$", "."],
                          [".", "2", "3", "."]], Number(1, 1, 2, "23")) is True

  def test_symbol_bottom(self):
    assert check_is_tile([[".", "2", "3", "."],
                          [".", "$", ".", "."]], Number(0, 1, 2, "23")) is True

  def test_symbol_behind(self):
    assert check_is_tile([[".", "2", "3", "$"]], Number(0, 1, 3, "23")) is True

class TestParseForTileNumber:
  def test_number_full_row(self):
    assert parse_for_tile_numbers([["1","2"]]) == [Number(0, 0, 1, "12")]

  def test_row_start_with_number(self):
    assert parse_for_tile_numbers([["3","2", "."]]) == [Number(0, 0, 1, "32")]

  def test_row_end_with_number(self):
    assert parse_for_tile_numbers([[".", "4","4"]]) == [Number(0, 1, 2, "44")]

  def test_row_with_multiple_numbers(self):
    assert parse_for_tile_numbers([["2","5",".", "9","9"]]) == [
      Number(0, 0, 1, "25"),
      Number(0, 3, 4, "99")]

  def test_multiple_rows(self):
    assert parse_for_tile_numbers([["2","5",".", "9","9"], ["1","2","3","4","5"]]) == [
      Number(0, 0, 1, "25"),
      Number(0, 3, 4, "99"),
      Number(1, 0, 4, "12345")]

class TestLoadInto2DArray:
  def with_multiline(self):
    self.create_file_from_list(DEFAULT_FILE_NAME, ["..123", "$456."])
    assert load_into_2d_array(DEFAULT_FILE_NAME) == [
      [".", ".", "1", "2", "3"],
      ["$", "4", "5", "6", "."]]

  def test_end_to_end(self):
    file = os.path.join(os.path.dirname(__file__), "demo_input.txt")
    parse_for_tile_numbers(load_into_2d_array(file))
    pass

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
