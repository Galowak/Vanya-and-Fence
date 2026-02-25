def convert_word(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = len(s) - upper_count  
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()
s = raw_input().strip()  
result = convert_word(s)
print(result)
