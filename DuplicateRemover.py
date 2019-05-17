name = 'dwa512'
file = name+'.mtx'
fileS = name+'-sorted.txt'
fileD = name+'-com.txt'
ok = True

with open(fileS) as fs:
    for lineS in fs:
        ts = tuple()
        ts = (int(lineS.split(" ")[0]), int(lineS.split(" ")[1]), lineS)
        with open(fileD, 'r+') as fd:
            lines = fd.readlines()
            for lineD in lines:
                td = tuple()
                td = (int(lineD.split(" ")[0]), int(lineD.split(" ")[1]), lineD)

                if (ts[0] == td[1] and ts[1] == td[0]):
                    ok = False
                    break
                else:
                    ok = True
            else:
                if ok:
                    fd.write(lineS)
