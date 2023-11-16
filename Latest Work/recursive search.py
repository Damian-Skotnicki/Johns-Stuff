#Recursive Search
idx = int(input("what are you looking for "))
al = [15,4,41,13,24,14,12,21,4]

'''
def Linears(al,idx):  
    for inside in al:
        if inside == idx:
            return al.index(inside)
    return -1
    
working = Linears(al,idx)
print(working)
'''


def linears(al,idx):
        if al == []:
            return -1
        elif al[0] == idx:
#             return al.index(0)
            return al[0]
        else:
            return linears(al[1:len(al)],idx)
print(linears(al,idx))
             
        
