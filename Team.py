n = int(raw_input())
 
 
total_implemented = 0
 
 
for i in range(n):
   
    sure_list = map(int, raw_input().split())
    
 
    if sum(sure_list) >= 2:
        total_implemented += 1
 
 
print total_implemented
