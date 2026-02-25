try:
    n = int(raw_input().strip())
    s = raw_input().strip()
except:
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        sys.exit()
    if len(data) == 1:
        s = data[0]
    else:
        s = data[1]
removals = 0
for i in xrange(1, len(s)):
    if s[i] == s[i-1]:
        removals += 1
 
print removals
