sentence = input("Enter a sentence: ")
chars = {}
vowls = "aeiouAEIOU"
constants = "bcdfghjklmnpqrstvwxyzBCDFGHIJKLMNPQRSTVWXYZ"
for char in sentence:
    #chars[char] = chars.get(char, 0) + 1
    if char in vowls:
        chars[char] = chars.get(char, 0) + 1
    elif char in constants:
        chars[char] = chars.get(char, 0) + 1
    #print(char)
        
'''
    if char in chars:
        chars[char] = chars[char] +1
    else:
        chars[char] = 1
'''
    
    
print(chars)



