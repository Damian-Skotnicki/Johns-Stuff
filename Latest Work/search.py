'''
idx = int(input("what are you looking for "))
al = [15,4,41,13,24,14,12,21,4]

def Linears(al,idx):  
    for inside in al:
        if inside == idx:
            return al.index(inside)
    return -1
    
working = Linears(al,idx)
print(working)
'''


idx = int(input("what are you looking for "))
al=[4,1,3,7,8,2,10,5,6,9,22,11,12] #list
al.sort() #sort list
print(al)
low = 0 # gets index first 
high = len(al) #count how long list is
high = high-1 #list is 11 long as shown 
print(low) #prints first
print(high)
mid = (low + high)//2 
print(mid)

boolianval = True
while True:
    mid = (low + high)//2 
    if al[mid] == idx:
        print(mid)
        break
    elif al[mid] > idx:
        high = mid - 1
    elif al[mid] < idx:
        low = mid + 1   
    if low > high:
        print("this number dousnt exist")
        break









