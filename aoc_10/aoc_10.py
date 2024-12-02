import copy
import os


class Node:
  def __init__(self, value, coords: (int, int), prev=None):
    self.value = value
    self.coords = coords
    self.prev = prev
    if self.value == "S":
      self.loop_position = 0
    elif self.prev is not None:
      self.loop_position = self.prev.loop_position + 1
    else:
      self.loop_position = -1

  def __eq__(self, other):
    if isinstance(other, Node):
      return self.coords == other.coords and self.value == other.value
    return False


class MapService:
  def __init__(self, map: list[list[str]], start_coords: (int, int)):
    self.map = map
    self.start_node = Node("S", start_coords)

  def _get_value_for_coords(self, coords: (int, int)) -> str:
    return self.map[coords[0]][coords[1]]

  def _get_next_node_for_start(self) -> Node:
    node = self.start_node
    max_x_index = len(self.map) - 1
    max_y_index = len(self.map[0]) - 1
    if node.coords == (0, 0):
      return Node(self._get_value_for_coords((0, 1)), (0, 1), prev=node)
    if node.coords == (0, max_y_index):
      return Node(
        self._get_value_for_coords((1, max_y_index)),
        (1, max_y_index),
        prev=node,
      )
    if node.coords == (max_x_index, 0):
      return Node(
        self._get_value_for_coords((max_x_index - 1, 0)),
        (max_x_index - 1, 0),
        prev=node,
      )
    if node.coords == (max_x_index, max_y_index):
      return Node(
        self._get_value_for_coords((max_x_index - 1, max_y_index)),
        (max_x_index - 1, max_y_index),
        prev=node,
      )

    if self.map[node.coords[0] - 1][node.coords[1]] in ["7", "|", "F"]:
      return Node(
        self._get_value_for_coords((node.coords[0] - 1, node.coords[1])),
        (node.coords[0] - 1, node.coords[1]),
        prev=node,
      )
    if self.map[node.coords[0]][node.coords[1] + 1] in ["J", "-", "7"]:
      return Node(
        self._get_value_for_coords((node.coords[0], node.coords[1] + 1)),
        (node.coords[0], node.coords[1] + 1),
        prev=node,
      )
    if self.map[node.coords[0] + 1][node.coords[1]] in ["J", "|", "L"]:
      return Node(
        self._get_value_for_coords((node.coords[0] + 1, node.coords[1])),
        (node.coords[0] + 1, node.coords[1]),
        prev=node,
      )
    if self.map[node.coords[0]][node.coords[1] - 1] in ["L", "-", "F"]:
      return Node(
        self._get_value_for_coords((node.coords[0], node.coords[1] - 1)),
        (node.coords[0], node.coords[1] - 1),
        prev=node,
      )

  def _get_next_node_for_l(self, node: Node) -> Node:
    if node.prev.coords[1] == node.coords[1] + 1:
      return Node(
        self._get_value_for_coords((node.coords[0] - 1, node.coords[1])),
        (node.coords[0] - 1, node.coords[1]),
        prev=node,
      )
    if node.prev.coords[0] == node.coords[0] - 1:
      return Node(
        self._get_value_for_coords((node.coords[0], node.coords[1] + 1)),
        (node.coords[0], node.coords[1] + 1),
        prev=node,
      )

  def _get_next_node_for_pipe(self, node: Node) -> Node:
    if node.prev.coords[0] == node.coords[0] - 1:
      return Node(
        self._get_value_for_coords((node.coords[0] + 1, node.coords[1])),
        (node.coords[0] + 1, node.coords[1]),
        prev=node,
      )
    if node.prev.coords[0] == node.coords[0] + 1:
      return Node(
        self._get_value_for_coords((node.coords[0] - 1, node.coords[1])),
        (node.coords[0] - 1, node.coords[1]),
        prev=node,
      )

  def _get_next_node_for_dash(self, node: Node) -> Node:
    if node.prev.coords[1] == node.coords[1] - 1:
      return Node(
        self._get_value_for_coords((node.coords[0], node.coords[1] + 1)),
        (node.coords[0], node.coords[1] + 1),
        prev=node,
      )
    if node.prev.coords[1] == node.coords[1] + 1:
      return Node(
        self._get_value_for_coords((node.coords[0], node.coords[1] - 1)),
        (node.coords[0], node.coords[1] - 1),
        prev=node,
      )

  def _get_next_node_for_f(self, node: Node) -> Node:
    if node.prev.coords[0] == node.coords[0] + 1:
      return Node(
        self._get_value_for_coords((node.coords[0], node.coords[1] + 1)),
        (node.coords[0], node.coords[1] + 1),
        prev=node,
      )
    if node.prev.coords[1] == node.coords[1] + 1:
      return Node(
        self._get_value_for_coords((node.coords[0] + 1, node.coords[1])),
        (node.coords[0] + 1, node.coords[1]),
        prev=node,
      )

  def _get_next_node_for_seven(self, node: Node) -> Node:
    if node.prev.coords[1] == node.coords[1] - 1:
      return Node(
        self._get_value_for_coords((node.coords[0] + 1, node.coords[1])),
        (node.coords[0] + 1, node.coords[1]),
        prev=node,
      )
    if node.prev.coords[0] == node.coords[0] + 1:
      return Node(
        self._get_value_for_coords((node.coords[0], node.coords[1] - 1)),
        (node.coords[0], node.coords[1] - 1),
        prev=node,
      )

  def _get_next_node_for_j(self, node: Node) -> Node:
    if node.prev.coords[0] == node.coords[0] - 1:
      return Node(
        self._get_value_for_coords((node.coords[0], node.coords[1] - 1)),
        (node.coords[0], node.coords[1] - 1),
        prev=node,
      )
    if node.prev.coords[1] == node.coords[1] - 1:
      return Node(
        self._get_value_for_coords((node.coords[0] - 1, node.coords[1])),
        (node.coords[0] - 1, node.coords[1]),
        prev=node,
      )

  def _get_next_node_for_node(self, node: Node) -> Node:
    if node.value == "S":
      return self._get_next_node_for_start()
    if node.value == "|":
      return self._get_next_node_for_pipe(node)
    if node.value == "-":
      return self._get_next_node_for_dash(node)
    if node.value == "F":
      return self._get_next_node_for_f(node)
    if node.value == "7":
      return self._get_next_node_for_seven(node)
    if node.value == "L":
      return self._get_next_node_for_l(node)
    if node.value == "J":
      return self._get_next_node_for_j(node)

  def _get_loop_distance(self) -> int:
    current_node = self.start_node
    next_node = self._get_next_node_for_node(current_node)
    while next_node.value != "S":
      current_node = next_node
      next_node = self._get_next_node_for_node(current_node)
    return current_node.loop_position + 1

  def get_most_distant_corner_distance(self) -> int:
    return int(self._get_loop_distance() / 2)

  @staticmethod
  def from_file(filename: str):
    with open(filename) as f:
      start_coords = None
      map = []
      for index, line in enumerate(f.readlines()):
        if start_coords is None and "S" in line:
          start_coords = (index, line.index("S"))
        map.append(list(line.strip()))
    return MapService(map, start_coords)


class EnhancedMapService(MapService):
  def __init__(self, map: list[list[str]], start_coords: (int, int)):
    super().__init__(map, start_coords)
    self.enhanced_map = copy.deepcopy(map)
    self._generate_enhanced_map()

  def _generate_enhanced_map(self):
    current_node = self.start_node
    self.enhanced_map[current_node.coords[0]][
      current_node.coords[1]
    ] = current_node
    next_node = self._get_next_node_for_node(current_node)
    while next_node.value != "S":
      current_node = next_node
      self.enhanced_map[current_node.coords[0]][
        current_node.coords[1]
      ] = current_node
      next_node = self._get_next_node_for_node(current_node)

  def _get_s_value(self):
    top = None
    right = None
    bottom = None
    left = None

    if self.start_node.coords[0] - 1 >= 0:
      top = self._get_value_for_coords(
        (self.start_node.coords[0] - 1, self.start_node.coords[1])
      )
    if self.start_node.coords[1] + 1 < len(self.enhanced_map[0]):
      right = self._get_value_for_coords(
        (self.start_node.coords[0], self.start_node.coords[1] + 1)
      )
    if self.start_node.coords[0] + 1 < len(self.enhanced_map):
      bottom = self._get_value_for_coords(
        (self.start_node.coords[0] + 1, self.start_node.coords[1])
      )
    if self.start_node.coords[1] - 1 >= 0:
      left = self._get_value_for_coords(
        (self.start_node.coords[0], self.start_node.coords[1] - 1)
      )

    if top is not None and top in ["|", "F", "7"]:
      if right is not None and right in ["-", "F", "J"]:
        return "L"
      if left is not None and left in ["-", "L", "F"]:
        return "J"
      if bottom is not None and bottom in ["|", "L", "J"]:
        return "|"
    if right is not None and right in ["-", "J", "7"]:
      if bottom is not None and bottom in ["|", "L", "J"]:
        return "F"
      if left is not None and left in ["-", "L", "F"]:
        return "-"
    if (
      bottom is not None
      and bottom in ["|", "L", "J"]
      and left is not None
      and left in ["-", "L", "F"]
    ):
      return "7"

  def get_bounded_elements_count(self) -> int:
    bounded_elements_count = 0
    s_value = self._get_s_value()
    for row in self.enhanced_map:
      is_in = False
      last_angle = None
      for element in row:
        if isinstance(element, Node):
          if (
            element.value == "|"
            or element.value == "S"
            and self._get_s_value() == "|"
          ):
            is_in = not is_in
          if last_angle is None and element.value in ["L", "J", "7", "F"]:
            last_angle = element.value
          if (
            last_angle == "L"
            and (
              element.value == "7" or element.value == "S" and s_value == "7"
            )
            or last_angle == "F"
            and (
              element.value == "J" or element.value == "S" and s_value == "J"
            )
          ):
            is_in = not is_in
            last_angle = None

          if (
            last_angle == "L"
            and (
              element.value == "J" or element.value == "S" and s_value == "J"
            )
            or last_angle == "F"
            and (
              element.value == "7" or element.value == "S" and s_value == "7"
            )
          ):
            last_angle = None
        else:
          if is_in:
            bounded_elements_count += 1
    return bounded_elements_count

  @staticmethod
  def from_file(filename: str):
    with open(filename) as f:
      start_coords = None
      map = []
      for index, line in enumerate(f.readlines()):
        if start_coords is None and "S" in line:
          start_coords = (index, line.index("S"))
        map.append(list(line.strip()))
    return EnhancedMapService(map, start_coords)


def main():
  file_name = os.path.join(os.path.dirname(__file__), "input.txt")
  # loop = MapService.from_file(file_name)
  # print(f"Part 1: {loop.get_most_distant_corner_distance()}")
  enhanced_loop = EnhancedMapService.from_file(file_name)
  print(f"Part 2: {enhanced_loop.get_bounded_elements_count()}")


if __name__ == "__main__":
  main()
