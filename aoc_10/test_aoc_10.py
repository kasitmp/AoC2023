import os
import shutil

from aoc_10.aoc_10 import EnhancedMapService, MapService, Node


class TestMap:
  TEST_DATA = os.path.join(os.path.dirname(__file__), "test_data")

  def test_from_file(self):
    with open(os.path.join(self.TEST_DATA, "fixture.txt"), "w") as f:
      f.write(
        """.S-7.
.|.|.
.L-J."""
      )
    loop = MapService.from_file(os.path.join(self.TEST_DATA, "fixture.txt"))
    assert loop.map == [
      [".", "S", "-", "7", "."],
      [".", "|", ".", "|", "."],
      [".", "L", "-", "J", "."],
    ]
    os.remove(os.path.join(self.TEST_DATA, "fixture.txt"))

  def test_find_start(self):
    with open(os.path.join(self.TEST_DATA, "fixture.txt"), "w") as f:
      f.write(
        """.S-7.
.|.|.
.L-J."""
        )
    map = MapService.from_file(os.path.join(self.TEST_DATA, "fixture.txt"))
    assert map.start_node.coords == (0, 1)

  def test_get_next_node_for_s_top_left(self):
    map = MapService([["S", "7"], ["L", "J"]], (0, 0))
    assert map._get_next_node_for_node(map.start_node) == Node(
      "7", (0, 1), prev=map.start_node
    )

  def test_get_next_node_for_s_top_right(self):
    map = MapService([["7", "S"], ["L", "J"]], (0, 1))
    assert map._get_next_node_for_node(map.start_node) == Node(
      "J", (1, 1), prev=map.start_node
    )

  def test_get_next_node_for_s_bottom_left(self):
    map = MapService([["F", "7"], ["S", "J"]], (1, 0))
    assert map._get_next_node_for_node(map.start_node) == Node(
      "F", (0, 0), prev=map.start_node
    )

  def test_get_next_node_for_s_bottom_right(self):
    map = MapService([["F", "7"], ["L", "S"]], (1, 1))
    assert map._get_next_node_for_node(map.start_node) == Node(
      "7", (0, 1), prev=map.start_node
    )

  def test_get_next_node_for_s_top_right_bigger(self):
    map = MapService([["F", "-", "S"], ["L", "-", "J"]], (0, 2))
    assert map._get_next_node_for_node(map.start_node) == Node(
      "J", (1, 2), prev=map.start_node
    )

  def test_get_next_node_for_s_bottom_left_bigger(self):
    map = MapService([["F", "-", "J"], ["|", ".", "|"], ["S", "-", "J"]], (2, 0))
    assert map._get_next_node_for_node(map.start_node) == Node(
      "|", (1, 0), prev=map.start_node
    )

  def test_get_next_node_for_s_bottom_right_bigger(self):
    map = MapService([["F", "-", "J"], ["|", ".", "|"], ["L", "-", "S"]], (2, 2))
    assert map._get_next_node_for_node(map.start_node) == Node(
      "|", (1, 2), prev=map.start_node
    )

  def test_get_next_node_for_s_center(self):
    map = MapService([["F", "F", "7"], ["|", "S", "J"], ["L", "-", "J"]], (1, 1))
    assert map._get_next_node_for_node(map.start_node) == Node(
      "F", (0, 1), prev=map.start_node
    )

  def test_get_next_node_for_pipe_from_bottom(self):
    map = MapService([["F"], ["|"], ["S"]], (2, 0))
    pipe_node = Node("|", (1, 0), prev=map.start_node)
    assert map._get_next_node_for_node(pipe_node) == Node(
      "F", (0, 0), prev=pipe_node
    )

  def test_get_next_node_for_pipe_from_top(self):
    map = MapService([["S"], ["|"], ["L"]], (0, 0))
    pipe_node = Node("|", (1, 0), prev=map.start_node)
    assert map._get_next_node_for_node(pipe_node) == Node(
      "L", (2, 0), prev=pipe_node
    )

  def test_get_next_node_for_dash_from_left(self):
    map = MapService([["S", "-", "7"]], (0, 0))
    dash_node = Node("-", (0, 1), prev=map.start_node)
    assert map._get_next_node_for_node(dash_node) == Node(
      "7", (0, 2), prev=dash_node
    )

  def test_get_next_node_for_dash_from_right(self):
    map = MapService([["F", "-", "S"]], (0, 2))
    dash_node = Node("-", (0, 1), prev=map.start_node)
    assert map._get_next_node_for_node(dash_node) == Node(
      "F", (0, 0), prev=dash_node
    )

  def test_get_next_node_for_f_from_bottom(self):
    map = MapService([["F", "7"], ["S", "|"]], (1, 0))
    f_node = Node("F", (0, 0), prev=map.start_node)
    assert map._get_next_node_for_node(f_node) == Node("7", (0, 1), prev=f_node)

  def test_get_next_node_for_f_from_top(self):
    map = MapService([["F", "7"], ["|", "S"], ["L", "J"]], (1, 1))
    prev_node = Node("7", (0, 1), prev=map.start_node)
    f_node = Node("F", (0, 0), prev=prev_node)
    assert map._get_next_node_for_node(f_node) == Node("|", (1, 0), prev=f_node)

  def test_get_next_node_for_7_from_left(self):
    map = MapService([["S", "7"], ["L", "J"]], (0, 0))
    seven_node = Node("7", (0, 1), prev=map.start_node)
    assert map._get_next_node_for_node(seven_node) == Node(
    "J", (1, 1), prev=seven_node
    )

  def test_get_next_node_for_7_from_bottom(self):
    map = MapService([["F", "7"], ["L", "S"]], (1, 1))
    seven_node = Node("7", (0, 1), prev=map.start_node)
    assert map._get_next_node_for_node(seven_node) == Node(
      "F", (0, 0), prev=seven_node
    )

  def test_get_next_node_for_l_from_right(self):
    map = MapService([["F", "7"], ["L", "S"]], (1, 1))
    l_node = Node("L", (1, 0), prev=map.start_node)
    assert map._get_next_node_for_node(l_node) == Node("F", (0, 0), prev=l_node)

  def test_get_next_node_for_l_from_top(self):
    map = MapService([["F", "S", "."], ["|", "L", "7"]], (0, 1))
    l_node = Node("L", (1, 1), prev=map.start_node)
    assert map._get_next_node_for_node(l_node) == Node("7", (1, 2), prev=l_node)

  def test_get_next_node_for_j_from_top(self):
    map = MapService([["F", "S"], ["L", "J"]], (0, 1))
    j_node = Node("J", (1, 1), prev=map.start_node)
    assert map._get_next_node_for_node(j_node) == Node("L", (1, 0), prev=j_node)

  def test_get_next_node_for_j_from_left(self):
    map = MapService([["F", "7"], ["S", "J"]], (1, 0))
    j_node = Node("J", (1, 1), prev=map.start_node)
    assert map._get_next_node_for_node(j_node) == Node("7", (0, 1), prev=j_node)

  def test_get_loop_distance_easy(self):
    map = MapService([["S", "7"], ["L", "J"]], (0, 0))
    assert map._get_loop_distance() == 4

  def test_get_loop_distance_three_col(self):
    map = MapService([["S", "-", "7"], ["L", "-", "J"]], (0, 0))
    assert map._get_loop_distance() == 6

  def test_get_most_distant_corner_distance(self):
    map = MapService([["S", "-", "7"], ["L", "-", "J"]], (0, 0))
    assert map.get_most_distant_corner_distance() == 3

  def setup_method(self):
    if os.path.exists(self.TEST_DATA):
      shutil.rmtree(self.TEST_DATA)
    os.mkdir(self.TEST_DATA)

  def teardown_method(self):
    if os.path.exists(self.TEST_DATA):
      shutil.rmtree(self.TEST_DATA)


class TestEnhancedMap:
  def test_constructor_generates_enhanced_map(self):
    enhanced_map = EnhancedMapService(
        [["S", "-", "7"], ["|", ".", "|"], ["L", "-", "J"]], (0, 0)
    )
    assert enhanced_map.enhanced_map == [
      [Node("S", (0, 0)), Node("-", (0, 1)), Node("7", (0, 2))],
      [Node("|", (1, 0)), ".", Node("|", (1, 2))],
      [Node("L", (2, 0)), Node("-", (2, 1)), Node("J", (2, 2))],
    ]

  def test_constructor_generates_enhanced_map_with_different_position(self):
    enhanced_map = EnhancedMapService([["F", "7"], ["L", "S"]], (1, 1))
    assert enhanced_map.enhanced_map == [
      [Node("F", (0, 0)), Node("7", (0, 1))],
      [Node("L", (1, 0)), Node("S", (1, 1))],
    ]

  def test_get_bounded_elements_count(self):
    enhanced_map = EnhancedMapService(
      [
        ["7", "F", "-", "7", "|"],
        ["J", "|", ".", "S", "L"],
        ["=", "L", "-", "J", "."],
      ],
        (1, 3),
    )
    assert enhanced_map.get_bounded_elements_count() == 1

  def test_get_s_value_f(self):
    enhanced_map = EnhancedMapService([["S", "7"], ["L", "J"]], (0, 0))
    assert enhanced_map._get_s_value() == "F"

  def test_get_s_value_seven(self):
    enhanced_map = EnhancedMapService([["F", "S"], ["L", "J"]], (0, 1))
    assert enhanced_map._get_s_value() == "7"

  def test_get_s_value_l(self):
    enhanced_map = EnhancedMapService([["F", "7"], ["S", "J"]], (1, 0))
    assert enhanced_map._get_s_value() == "L"

  def test_get_s_value_j(self):
    enhanced_map = EnhancedMapService([["F", "7"], ["L", "S"]], (1, 1))
    assert enhanced_map._get_s_value() == "J"

  def test_get_s_value_dash(self):
    enhanced_map = EnhancedMapService([["F", "S", "7"], ["L", "-", "J"]], (0, 1))
    assert enhanced_map._get_s_value() == "-"

  def test_get_s_value_pipe(self):
    enhanced_map = EnhancedMapService([["F", "7"], ["S", "|"], ["L", "J"]], (1, 0))
    assert enhanced_map._get_s_value() == "|"
