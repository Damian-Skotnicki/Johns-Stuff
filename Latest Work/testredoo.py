#test redoo
#cardNum= 8123123412341234
# 7200828282828210
#print(cardNum)
#print(conv_str)
#print(listversion)
asd = "1234"
print(asd[0:2])
#ads = asd + 1
#asd += 1
def cardcheck():
    tries = 2   
    cardNum= input("Welcome to CardCheck. Enter your card number:")
    listversion = list(cardNum)
    
    while tries != 0:
        if len(listversion) == 16:
            break 
        else:
            cardNum= input("This is incorrect, please try again:")
            tries -= 1
            
    exp = input("Enter the card expiry date e.g. 11/26 should be entered as 1126:")
    combined = 0
    for el in exp:
        combined += int(el)
        
        #print(combined)
    # a =  combined * (( int(listversion[0]) *10 ) + int(listversion[1]) ) #this is what im trying to get
    cvv = combined * int(cardNum[0:2]) - int(cardNum[9])
    
    
    

    
    
    firstd = int(listversion[0])
    
    if firstd == 8 : 
        print("This is a WinCard")
    elif firstd == 7 :
        print("This is a ZincCard")
        
    print("CVV number:",  cvv )
    

        
cardcheck()
