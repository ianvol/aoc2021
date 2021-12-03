#part 1

numflist = []
numdlist = []
numulist = []

with open("input.txt", 'r') as f:
  for line in f:
    if line.startswith("f"):
        lnf = line.split()
        numf = int(lnf[1])
        numflist.append(numf)
    elif line.startswith("d"):
        lnd = line.split()
        numd = int(lnd[1])
        numdlist.append(numd)
    elif line.startswith("u"):
        lnu = line.split()
        numu = int(lnu[1])
        numu = numu * -1
        numulist.append(numu)

forwardsum = sum(numflist)
downsum = sum(numdlist)
upsum = sum(numulist)

verticalsum = upsum + downsum

total = forwardsum * verticalsum
print("Total: ",total)

#part 2

numhlist = []
ho = 0
depth = 0
aim = 0

with open("input.txt", 'r') as f:
  for line in f:
    if line.startswith("f"):
        lnh = line.split()
        ho = int(lnh[1])
        numhlist.append(ho)
        if aim !=0:
            depth += ho * aim
    elif line.startswith("d"):
        lnd = line.split()
        numd = int(lnd[1])
        aim += numd
    elif line.startswith("u"):
        lnu = line.split()
        numu = int(lnu[1])
        numu = numu * -1
        aim += numu

hsum = sum(numhlist)

total = forwardsum * depth

print("Total: ",total)








