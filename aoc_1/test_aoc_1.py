from aoc_1.aoc_1 import (
  calibration_value_sum,
  calibration_value_sum_two,
  transform_words_to_numbers,
)


def test_calibration_value_sum_with_empty_list():
  assert calibration_value_sum([]) is None

def test_calibration_value_sum_with_empty_string():
  assert calibration_value_sum([""]) is None

def test_calibration_value_sum_with_single_item_list_zero():
  assert calibration_value_sum(["0"]) == 0

def test_calibration_value_sum_with_single_item_list_five():
  assert calibration_value_sum(["5"]) == 55

def test_calibration_value_sum_with_two_item_list():
  assert calibration_value_sum(["2", "5"]) == 77

def test_calibration_value_sum_with_one_item_list_with_non_digit():
  assert calibration_value_sum(["a"]) == 0

def test_calibration_value_sum_with_one_item_list_with_digit_and_non_digit():
  assert calibration_value_sum(["a1"]) == 11

def test_calibration_value_sum_with_one_item_list_with_digits_and_non_digit():
  assert calibration_value_sum(["1a1"]) == 11

def test_calibration_value_sum_with_one_item_list_with_digit_and_non_digits():
  assert calibration_value_sum(["a1a"]) == 11

def test_calibration_value_sum_with_one_item_list_with_digits_and_non_digits():
  assert calibration_value_sum(["a1b2c3d4e5f"]) == 15

def test_transform_words_to_numbers_with_empty_list():
  assert transform_words_to_numbers("") == ""

def test_transform_words_to_numbers_with_non_digit_words():
  assert transform_words_to_numbers("bla") == "bla"

def test_transform_words_to_numbers_with_digit_word_one():
  assert transform_words_to_numbers("one") == "o1e"

def test_transform_words_to_numbers_with_digit_words_all():
  assert transform_words_to_numbers(
    "onetwothreefourfivesixseveneightnine") == "o1et2ot3ef4rf5es6xs7ne8tn9e"

def test_word_overlap_prefix():
  assert transform_words_to_numbers("eightwothree") == "e8t2ot3e"

def test_calibration_value_sum_two_with_empty_list():
  assert calibration_value_sum_two([]) is None

def test_calibration_value_sum_two_with_official_test_data():
  assert calibration_value_sum_two([
    "two1nine",
  "eightwothree",
  "abcone2threexyz",
  "xtwone3four",
  "4nineeightseven2",
  "zoneight234",
  "7pqrstsixteen"
  ]) == 281

def test_calibration_value_sum_with_official_test_data():
  assert calibration_value_sum([
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"]) == 142

