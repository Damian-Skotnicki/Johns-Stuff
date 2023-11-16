'''
if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
'''
''' # 7, 13, 14, 16, 19 , 1, 9, 16, 18, 19 , 3, 4, 8, 10, 17 ,4, 7, 8, 11, 17
firstl = [1,9,10,18,2,1,2,15,17,1,7,9,13,17,1,2,15,17,18]

#x=0

def sumfinder(f):
    if len(f) == 0:
        return 0 
    else:
        return f[0]+sumfinder(f[1:])
working = sumfinder(firstl)
print(working)
'''
'''
secondl = int(input("Multiply out " ))
#y=0

def multipliere(s):
    if s ==1:
        return 1
    else:
        return s * multipliere(s-1)
working = multipliere(secondl)
print(working)
'''

'''
imput = int(input("how long u want the fibonacci system to go "))

def fibonacci(n):  
    if n == 1:
     return 0
    elif n <= 3:
       return 1
    else:
       return(fibonacci(n-1) + fibonacci(n-2))

#for i in range(imput):
#   print(fibonacci(i))


print(fibonacci(imput))

'''

'''
imput = int(input("Enter A very large number eg 1234 "))

def weirdsum(permm):
    #print(permm)
    if permm == 0:
        return 0   
    else:
        return permm % 10 + weirdsum(permm//10)
ans = weirdsum(imput)
print(ans)
  
'''





    