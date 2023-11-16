'''
alist=[1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print("This is just printing first digit", alist[0])
indexPos = 0
Numlist =[]
Apearlist =[] 

while indexPos <= len(alist)-1:
    y = alist.count(alist[indexPos])
    Numlist.append(int(y))
    Apearlist.append(alist[indexPos])
#    print(Numlist)
    print(y, "thats the amount of" , alist[indexPos] )
    indexPos = indexPos +y
print("amounts of numbers", Numlist)
print("the number", Apearlist)

#choose from numlist which number is the largest
#from the second list we to figure out what number it was
#eg. if 16 is the largest it shows that 1 is the most common

#if u sorted numlist 16 would be the last one in the list
#but if u do so then u might not know what number it related to 

Answere = max(Numlist)
print(Answere)
numb = Numlist.index(Answere)
print(numb )

print(Apearlist[numb] , "apears" , Answere , "times")
'''