def nonogram_line_solver(line: str, blocks: list[int]) -> int:
  if line.count('#') == blocks[0] or line.count('?') == blocks[0]:
    return 1

  return 0
# ..?#.?? 2, 1

def expand_all_variations(line: str, blocks, variations, cur_index = 0) -> dict:
  if cur_index == len(line):
    return {"leaf": True}
  else:
    
  if d == 1: return {"leaf": True}
  else: return {"leaf": False, "left": make_tree(d-1), "right": make_tree(d-1)}
  # if cur_index == len(line):
  #   return variations
  # elif line[cur_index] == "?":
  #   cur_line = line[:cur_index] + "#" + line[cur_index+1:].replace("?", ".")
  #   cur_structure_code = get_structure_code(cur_line)
  #   if cur_structure_code == blocks:
  #     variations.append(",".join(cur_structure_code))
  #   next_line = line[:cur_index] + "." + line[cur_index+1:]
  #   return expand_all_variations(next_line, blocks, variations, cur_index+1)
  #   next_line_b = line[:cur_index] + "#" + line[cur_index+1:]
  #   return expand_all_variations(next_line_b, blocks, variations, cur_index+1)
  # else:
  #   return expand_all_variations(line, blocks, variations, cur_index+1)

def get_structure_code(line: str) -> [str]:
  blocks = []
  cur_block_size = 0
  for i in line:
    if i == "#":
      cur_block_size += 1
    elif cur_block_size != 0:
      blocks.append(str(cur_block_size))
      cur_block_size = 0
  if cur_block_size != 0:
    blocks.append(str(cur_block_size))
  return blocks

