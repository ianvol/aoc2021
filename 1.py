##part 1
highestcount = 0
highestcount = int(highestcount)

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

lines = [int(i) for i in lines]

for x in range(1, len(lines)):
    if lines[x] > lines[x-1]:
        highestcount += 1

print(highestcount)

##part 2

highestsum = 0
highestsum = int(highestsum)

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

lines = [int(i) for i in lines]

for x in range(2, len(lines)):
    if sum(lines[x-2:x+1]) < sum(lines[x-1:x+2]):
        highestsum += 1

print(highestsum)
