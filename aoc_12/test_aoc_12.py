from aoc_12.aoc_12 import (
  expand_all_variations,
  get_structure_code,
  nonogram_line_solver,
)


def test_block():
  assert nonogram_line_solver("#", ["1"]) == 1

def test_question_mark():
  assert nonogram_line_solver("?", ["1"]) == 1

def test_blanks_question_marks_hashtags():
  assert nonogram_line_solver("..?#.#", ["2", "1"]) == 1

def test_blanks_question_marks_hashtags_2():
  assert nonogram_line_solver("..?#.??", ["2", "1"]) == 2

def test_expand_simple_case_block():
  assert expand_all_variations("#") == ['1']

def test_expand_simple_question_mark():
  assert expand_all_variations("?", ["1"], []) == ['1']

def test_expand_complex_case():
  assert expand_all_variations("..?#.??", ["2", "1"], []) == ['2,1', '2,1']

def test_get_structure_code_block():
  assert get_structure_code("#") == ["1"]

def test_get_structure_multi_block():
  assert get_structure_code("##..##..#") == ["2","2","1"]

