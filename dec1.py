with open("dec1input.txt") as file:
  while (line := file.readline().rstrip()):
    print(line)
