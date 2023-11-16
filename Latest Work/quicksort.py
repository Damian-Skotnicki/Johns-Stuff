#mainlist = [88,13,25,11,18,46,12,22,82]
mainlist = [88,46,25,11,18,12,22]
pivot = int(mainlist[-1])
print(pivot)

left_list = [] #left
middle_list = [] #middle
right_list = [] #right

for elements in mainlist:
    
    if pivot > elements:
        left_list.append(elements)
        print(left_list)
        
    elif pivot == elements:
        middle_list.append(elements)
        print(middle_list)
        
    elif pivot < elements:
        right_list.append(elements)
        print(right_list)
        
    else:
        print("AHHHH AHHHHH SOMETHINGS ON FIRE PLEASE HELP ME!!!!!!!!!! AHHHH")#this is how i feel





          
