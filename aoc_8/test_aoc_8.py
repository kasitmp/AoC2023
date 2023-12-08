from aoc_8.aoc_8 import follow_complex_instructions, follow_instructions, least_common_multiple, set_complex_dict, set_dict


class TestSetDict:
  def test_three_similar_letters(self):
    assert set_dict(["AAA = (BBB, CCC)"]) == {"AAA": ("BBB", "CCC")}

  def test_three_different_letters(self):
    assert set_dict(["FLG = (PCR, CTD)"]) == {"FLG": ("PCR", "CTD")}

  def test_multi_line(self):
    assert set_dict(["AAA = (BBB, CCC)", "DDD = (EEE, FFF)"]) == {"AAA": ("BBB", "CCC"), "DDD": ("EEE", "FFF")}

class TestFollowInstructions:
  def test_single_instruction(self):
    assert follow_instructions("R", {"AAA": ("BBB", "ZZZ")}) == 1

  def test_two_step_instructions(self):
    assert follow_instructions("LR", {"AAA": ("BBB", "CCC"), "BBB": ("DDD", "ZZZ")}) == 2

  def test_two_step_single_instruction(self):
    assert follow_instructions("L", {"AAA": ("BBB", "CCC"), "BBB": ("ZZZ", "DDD")}) == 2

  def test_single_z_version(self):
    assert follow_instructions("R", {"AAA": ("BBB", "XXZ")}) == 1

  def test_different_start(self):
    assert follow_instructions("R", {"11A": ("BBB", "ZZZ")}, "11A") == 1


class TestComplexDict:
  def test_single_ending_on_a(self):
    assert set_complex_dict(["AAA = (BBB, CCC)"]) == ({"AAA": ("BBB", "CCC")}, {"A": ["AAA"]})

  def test_two_ending_on_a(self):
    assert set_complex_dict(["AAA = (BBB, CCC)", "DDA = (EEE, FFF)"]) == ({"AAA": ("BBB", "CCC"), "DDA": ("EEE", "FFF")}, {"A": ["AAA", "DDA"]})

class TestComplexFollowInstructions:
  def test_single_step(self):
    assert follow_complex_instructions("R", {"AAA": ("BBB", "ZZZ")}, {"A": ["AAA"]}) == 1

  def test_single_step_complex(self):
    assert follow_complex_instructions("L", {"AAA": ("ZZZ", "BBB"), "BBA": ("BBZ", "CCC")}, {"A": ["AAA", "BBA"]}) == 1

  def test_two_step_complex(self):
    assert follow_complex_instructions("LR", {
      "11A": ("11B", "XXX"),
      "22A": ("22B", "XXX"),
      "11B": ("XXX", "11Z"),
      "22B": ("XXX", "22Z")}, {"A": ["11A", "22A"], "B": ["11B", "22B"]}) == 2

class TestLeastCommonDenominator:
  def test_easy_parameters(self):
    assert least_common_multiple([2, 3]) == 6

  def test_hard_parameters(self):
    assert least_common_multiple([2, 3, 4]) == 12



