# f = open('demofile.txt')
# print(f.read())

# f = open("demofile.txt")
# print(f.read())

# with open("demofile.txt") as f:
#   print(f.read())

# f = open("demofile.txt")
# print(f.readline())
# print(f.readline())
# f.close()

with open("demofile.txt") as f:
  for x in f:
    print(x)