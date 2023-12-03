import os.path

import pytest

from shared.shared import input_lines_to_list

TEMP_FIXTURE_FOLDER = os.path.join(os.path.dirname(__file__), "temp_fixtures")

class TestFileHandlingFunctions:
  def test_input_line_to_list(self):
    self.create_file_from_list(f"{TEMP_FIXTURE_FOLDER}/test1.txt", ["1abc2"])
    assert input_lines_to_list(f"{TEMP_FIXTURE_FOLDER}/test1.txt") == ["1abc2"]

  def test_input_line_to_list_with_multiple_lines(self):
    self.create_file_from_list(f"{TEMP_FIXTURE_FOLDER}/test2.txt", ["1abc2", "3def4"])
    assert input_lines_to_list(f"{TEMP_FIXTURE_FOLDER}/test2.txt") == ["1abc2", "3def4"]

  @pytest.fixture(scope='session', autouse=True)
  def clean_fixture_files(self):
    yield
    # Will be executed after the last test
    for file in os.listdir(TEMP_FIXTURE_FOLDER):
      os.remove(os.path.join(TEMP_FIXTURE_FOLDER, file))

  def create_file_from_list(self, file_name, list):
    with open(file_name, "w") as f:
      for item in list:
        f.write("%s\n" % item)
