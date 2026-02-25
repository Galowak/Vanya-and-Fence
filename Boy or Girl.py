s = raw_input().strip()
distinct_characters = set(s)
if len(distinct_characters) % 2 == 1:
    print "IGNORE HIM!"
else:
    print "CHAT WITH HER!"
