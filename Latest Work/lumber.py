# THIS IS THE MEAN FROM THE FIRST LINE IN THE FILE

f = open("mean-median-mode-frequency.csv",'r')
line=f.readline()
line=line.strip()
line= line.split(",")
alist = []
#print(line)
RunningTotal= 0

for item in line:
    alist.append(int(item))
for item in alist:
    RunningTotal = RunningTotal + item
print("Mean is", RunningTotal / len(line))

print(line)

alist.sort()
meanie = len(alist)%2
lenght = len(alist)
print("odd = 1 / even = 0  AND THIS IS", meanie)
print("this has", lenght , "digits" )
half = len(alist)//2
print("half of", lenght, "is" , half )
meeen = alist[half]
print("THE MEDIAN IS" , meeen)

'''
m0 = alist.count(0)
print("their is", m0 , "0's")
m1 = alist.count(1)
print("their is", m1 , "1's")
m2 = alist.count(2)
print("their is", m2 , "2's")
m3 = alist.count(3)
print("their is", m3 , "3's")
m4 = alist.count(4)
print("their is", m4 , "4's")
m5 = alist.count(5)
print("their is", m5 , "5's")
m6 = alist.count(6)
print("their is", m6 , "6's")
m7 = alist.count(7)
print("their is", m7 , "7's")
m8 = alist.count(8)
print("their is", m8 , "8's")
m9 = alist.count(9)
print("their is", m9 , "9's")
'''

#LIST IS SORTED IN LINE 19 !!!!!!!!!
print(alist) # thats proof


print("This is just printing first digit", alist[0])

#this calculates the amounts of one digit
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


Answere = max(Numlist)
print(Answere)
numb = Numlist.index(Answere)
print(numb )


print(Apearlist[numb] , "apears" , Answere , "times")



f.close()

