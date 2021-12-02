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

fsum = sum(numflist)
dsum = sum(numdlist)
usum = sum(numulist)

verticalsum = usum + dsum

totalsum = fsum * verticalsum
print("Total sum: ",totalsum)

        



