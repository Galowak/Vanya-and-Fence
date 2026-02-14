n, h = map(int, raw_input().split())
heights = list(map(int, raw_input().split()))
 total_width = 0
 for a in heights:
    if a <= h:
        total_width += 1
    else:
        total_width += 2
 print(total_width)
 
