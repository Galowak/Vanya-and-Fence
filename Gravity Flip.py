n = int(raw_input().strip())
a = map(int, raw_input().strip().split())
a.sort()
print ' '.join(map(str, a))
