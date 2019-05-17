bands = list()
name = 'dwa512'
file = name+'.mtx'
with open(file) as fin:
    for line in fin:
        t = tuple()
        t = (int(line.split(" ")[0]), int(line.split(" ")[1]), line)
        bands.append(t)


sorted_by_first = sorted(bands, key=lambda tup: tup[0])
with open(name+'-sorted.txt', 'w') as outfile:
    for s in sorted_by_first:
        if s[0] != s[1]:
            outfile.write(str(s[0]-1)+" "+str(s[1]-1)+"\n")
