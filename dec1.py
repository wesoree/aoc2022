with open("dec1input.txt") as input_data:
  elflist = []
  for line in input_data:
    elflist.append(sum(line))
  a = max(elflist)
  print(a)