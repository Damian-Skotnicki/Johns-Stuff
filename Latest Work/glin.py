#runTOTAL = 0

#price1 = 12
#runTOTAL = runTOTAL + price1
#price2 = 24
#runTOTAL = runTOTAL + price2
#price3 = 36
#runTOTAL = runTOTAL + price3
#price4 = 48
#runTOTAL = runTOTAL + price4
#print(runTOTAL)

#fin = open("daffodils.txt")
#print(fin)
#for line in fin:

#    print(line.strip())
#fin.close()
  

#f = open("daffodils.txt")
#print(f)
#for line in f:
#   line = line.strip()
#   if(line.isdigit()):
#    print(line)


#numl = 0
#flin = open("daffodils.txt")
#print(flin)
#for line in flin:
#    print(line)
#    numl = numl + 1
#    print(numl)
    
#flin.close()

#ans = 0
#guml = 0
#glin = open("num_calc_1.txt")
#print(glin)
#for line in glin:
#   line = line.strip()
#	if line.isdigit():
#       print(line)
#    	print(line)
#    	guml = guml + 1

#print(guml)
#print(glin)
# ans = glum / glin
#print(ans)

    
#glin.close()

#Runtotal = 0
#puml = 0
#Answere = 0
#test = 0 
#plin = open("num_calc_2.txt")
#print(plin)
#for line in plin:
#    line = line.strip()
#    if line.isdigit():
#        print(line)
#        Runtotal = Runtotal + int(line)
#        puml = puml + 1
#   
#print(puml) #lines
#print(Runtotal) #add all digits inside

#test = Runtotal / puml
#Answere = puml / Runtotal # lines Divided by num_calc_2. total from txt
#print(Answere) #mean
#print(test)
#plin.close()

# EXERCISE $4
#a = int(input("Random number"))
#b = int(input("Random number"))
#c = int(input("Random number"))
#d = int(input("Random number"))
#e = int(input("Random number"))
#f = int(input("Random number"))
#g = int(input("Random number"))
#h = int(input("Random number"))
#i = int(input("Random number"))
#j = int(input("Random number"))
#k = int(input("Random number"))
#l = int(input("Random number"))
#m = int(input("Random number"))
#n = int(input("Random number"))
#o = int(input("Random number"))
#p = int(input("Random number"))
#q = int(input("Random number"))
#r = int(input("Random number"))
#s = int(input("Random number"))
#t = int(input("Random number"))

#NumAns = 0
#NumAns = a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t
#print(NumAns)
#Mean = 20
#ANSS = NumAns / Mean
#print(ANSS)

aa = input("Random number")
bb = input("Random number")
cc = input("Random number")
dd = input("Random number")
ee = input("Random number")
ff = input("Random number")
gg = input("Random number")
hh = input("Random number")
ii = input("Random number")
jj = input("Random number")

Fil=open("NUMS.txt", 'w')
Fil.write(aa + "\n" + bb +"\n" + cc + "\n" +  ee + "\n" +  ff + "\n" + gg + "\n" +  hh + "\n" + ii + "\n" + jj)
"""
Fil.write(aa)
Fil.write("\n")
Fil.write(bb)
Fil.write("\n")
Fil.write(cc)
Fil.write("\n")
Fil.write(ee)
Fil.write("\n")
Fil.write(ff)
Fil.write("\n")
Fil.write(gg)
Fil.write("\n")
Fil.write(hh)
Fil.write("\n")
Fil.write(ii)
Fil.write("\n")
Fil.write(jj)
"""
Fil.close()



