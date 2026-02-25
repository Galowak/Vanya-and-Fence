import sys
data = sys.stdin.read().strip().split()
if not data:
    print(0)
else:
    n = int(data[0])
    mags = data[1:1+n]
    if n == 0:
        print(0)
    else:
        groups = 1
        for i in range(1, n):
            if mags[i] != mags[i-1]:
                groups += 1
        print(groups)
