a, b = map(int, raw_input().split())
years = 0
while a <= b:
    a *= 3
    b *= 2
    years += 1
print years
