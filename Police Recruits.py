def police_recruits(events):
    officers = 0
    untreated_crimes = 0
    
    for event in events:
        if event > 0:
            officers += event  
        elif event == -1:
            if officers > 0:
                officers -= 1  
            else:
                untreated_crimes += 1 
    
    return untreated_crimes
 
n = int(raw_input().strip())
events = map(int, raw_input().strip().split())
 
result = police_recruits(events)
 
print(result)
