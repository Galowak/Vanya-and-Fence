n = int(raw_input().strip())
 
cards = map(int, raw_input().strip().split())
 
sereja_score = 0
dima_score = 0
 
left = 0
right = n - 1
turn = 0  
 
while left <= right:
    if cards[left] > cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1
    
    if turn == 0: 
        sereja_score += chosen_card
    else: 
        dima_score += chosen_card
    
    turn = 1 - turn
 
print sereja_score, dima_score
