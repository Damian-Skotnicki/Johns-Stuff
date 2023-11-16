cardNum= input("Welcome to CardCheck. Enter your card number:")

check = int(cardNum[0])


length = len(cardNum)





randomv = False

if length == 16:

    exdate = input("Enter the card expiry date e.g. 11/26 should be entered as 1125: ")

    def afun(chec):
        f = int(exdate[0])
        s = int(exdate[1])
        t = int(exdate[2])
        l = int(exdate[-1])
        step1 = f + s + t + l
        step2 = step1 * cardNum[0:1]
        print(cardNum[0:1])
        print(step1)
        print(step2)

    if check == 7:
            print("This is a zincCard")
            
    elif check == 8:
            print("This is a WinCard")
else: 
    for sc in range(2):
        
        cardNum= input("This is incorrect,please try again: ")
        check = int(cardNum[0])
        
        if len(cardNum) == 16:
            
            if check == 7:
                exdate = input("Enter the card expiry date e.g. 11/26 should be entered as 1125: ")
                print("this is correct")
                print("This is a zincCard")
                a = afun(chec)
                break
            elif check == 8:
                print("this is correct")
                print("This is a WinCard")
                a = afun(chec)
                break


    #line
            

    
        
    
    
    






    






    

