import os
import shutil

import pytest

import init_day

TEST_FOLDER = os.path.join(os.path.dirname(__file__), "test_folder")
class TestInitDay:
  def test_folder_creation(self, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    init_day.init_day()
    assert os.path.exists(os.path.join(TEST_FOLDER, "aoc_5"))

  def test_handle_existing_folder(self, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    init_day.init_day()
    with pytest.raises(SystemExit) as sys_exit:
      init_day.init_day()
    assert sys_exit.value.code == 1

  def test_base_file_creation(self, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 6)
    init_day.init_day()
    assert os.path.exists(os.path.join(TEST_FOLDER, "aoc_6", "aoc_6.py"))

  def test_base_test_file_creation(self, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    init_day.init_day()
    assert os.path.exists(os.path.join(TEST_FOLDER, "aoc_5", "test_aoc_5.py"))

  def test_input_file_creation(self, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    init_day.init_day()
    assert os.path.exists(os.path.join(TEST_FOLDER, "aoc_5", "input.txt"))

  def test_init_file_creation(self, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    init_day.init_day()
    assert os.path.exists(os.path.join(TEST_FOLDER, "aoc_5", "__init__.py"))

  @pytest.mark.skip(reason="Have to continue later")
  def test_input_file_population(self, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    init_day.init_day()
    with open(os.path.join(TEST_FOLDER, "aoc_5", "input.txt")) as f:
      assert f.read() == "mock_input"

  def test_test_input_file_creation(self, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    init_day.init_day()
    assert os.path.exists(os.path.join(TEST_FOLDER, "aoc_5", "test_input.txt"))

    #TODO: Test session outdated
    #TODO: Input validation (1-25)
    #TODO: Input validation (day <= today)


  def setup_method(self):
    if os.path.exists(TEST_FOLDER):
      shutil.rmtree(TEST_FOLDER)
    os.mkdir(TEST_FOLDER)
    init_day.FOLDER = TEST_FOLDER

  def teardown_method(self):
    if os.path.exists(TEST_FOLDER):
      shutil.rmtree(TEST_FOLDER)
