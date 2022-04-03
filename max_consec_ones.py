a = int(input())
b = int(input())
x = a ^ b
y = a * b
z = a + b
binx = [int(i) for i in bin(x).replace('0b', '')]
biny = [int(i) for i in bin(y).replace('0b', '')]
binz = [int(i) for i in bin(z).replace('0b', '')]

def consec1s(x):
    count=0
    res = 0
    for i in range(len(x)):
        if x[i] == 0:
            count = 0
        else:
            count += 1
            res = max(res, count)
    return res
c = [consec1s(binx), consec1s(biny), consec1s(binz)]
ziplist = list(zip(c, [x, y, z]))
maxc = c.count(max(c))
if maxc > 1:
    ziplist = [i for i in ziplist if i[0] == max(c)]
    ziplist = sorted(ziplist, key=lambda x: x[1])
    print(ziplist[0][1])
else:
    print(ziplist[0][1])
