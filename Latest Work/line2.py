
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
        
        
        #print(alist) LIST ITSELF
        
        shmol= min(alist)
        biggg= max(alist)
        
        print("smalles is" , shmol)
        print("biggest is" , biggg)
        Range= biggg - shmol
        print("so", biggg , "minus -" , shmol ,"is equal to" , Range)
        


f.close()


