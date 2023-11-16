
# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z,
# D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z,A, B, C,

#dwkorqh frppxqlwb froodjh

#part 3 ans 26

#WHAT DO YOU GET WHEN YOU CROSS A SNOWMAN WITH A"banana phone" VAMPIRE FROSTBITE






'''
#STOLEN CODE
def encypt_func(txt, s):  
    result = ""  
# transverse the plain txt  
    for i in range(len(txt)):  
        char = txt[i]  
        # encypt_func uppercase characters in plain txt  
  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        # encypt_func lowercase characters in plain txt  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  
# check the above function  
txt = input("Random txt ")  
s = 22  
  
print("Plain txt : " + "" + txt)  
print("Shift pattern : " + str(s))  
print("Cipher: " + encypt_func(txt, s))  


'''



#LCAPalphabet = "abcdefghijklmnopqrstuvwxyz"
#HCAPalphabet = "ABCDEGHIJKLMNOPQRSTUVWXYZ"
#LCcaesar = "defghijklmnopqrstuvwxyzabc"
#hCcaesar = "DEGHIJKLMNOPQRSTUVWXYZABC"


alphabet = "defghijklmnopqrstuvwxyzABCDEGHIJKLMNOPQRSTUVWXYZabc"
key=23

txt = input("Random txt ")
for var in txt:
    if var in alphabet:
        position_of_current_letter = alphabet.index(var)
        position_of_encode_letter = position_of_current_letter + key
        print(alphabet[position_of_encode_letter])
      
         

