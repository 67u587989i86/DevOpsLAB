
a = [11, 32, 1, 3, 4, 22, 55, 46, 7, 23]


largest = float('-inf')  
second_largest = float('-inf')  

for i in a:
    if i > largest: 
        second_largest = largest  
        largest = i  
    elif i > second_largest and i < largest:
        second_largest = i 


print("Second largest number:", second_largest)
