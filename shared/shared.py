def input_lines_to_list(file_name):
  with open(file_name) as f:
      print(f)
      lines = f.readlines()
  return [x.strip() for x in lines]
