
f = open("mean-median-mode-frequency.csv",'r')
for line in f:
    if len(line) > 1:
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



        #LIST IS SORTED IN LINE 19 !!!!!!!!!
        print(alist) # thats proof


        print("This is just printing first digit", alist[0])


        indexPos = 0
        Numlist ={}

        while indexPos <= len(alist)-1:
            y = alist.count(alist[indexPos])
            Numlist[alist[indexPos]] = y
           # Numlist.append(int(y))
           # Apearlist.append(alist[indexPos])
        #    print(Numlist)
            print(y, "thats the amount of" , Numlist[alist[indexPos]] )
            indexPos = indexPos +y
       # print("amounts of numbers", Numlist)
       # print("the number", Apearlist)
        print(Numlist)

        maxValue = -1
        keyValue = -99 #can be any value
        for key,value in Numlist.items():
            if value > maxValue:
                maxValue = value
                keyValue = key
        print(keyValue,"occurs",maxValue,"times")
         
        
        print(Numlist) #orginised BUT NOT USEFUL
        
        print(alist)
        newDict = {}
        for apple in alist:
            
            if apple in newDict:
                newDict[apple] = newDict[apple]+1
            else:
                newDict[apple] = 1
        print(newDict)
        dictValues =[]
        
        for v in newDict.values():
            dictValues.append(v)
            print(v)
        print(dictValues)
A = max(newDict)
B = min(newDict)
    print(a , "is the largest")
    print(b , "is the smallest")
    C = max - min
    print("so", a , "minus -" , b ,"is equal to" , c )
            
            

        
        
        

                

         
         
         
         
f.close()


