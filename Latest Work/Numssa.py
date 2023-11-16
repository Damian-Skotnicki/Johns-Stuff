
TestUPPER = "amazing pie"
print(TestUPPER)
ANS1 = TestUPPER.upper()    
print(ANS1)

print()
print()

Testlower = "FLYING CHEESE"
print(Testlower)
ANS2 = Testlower.lower()    
print(ANS2)

print()
print()

Counttester = "Bumfuzzle, Fartlek, Everywhen, Erf, Hullaballoo, Meldrop, Obelus, Sozzled, Bumbershoot, Titter, Supercalifragilisticexpialidocious"
print(Counttester)
CounterOfe = Counttester.count("e")
CounterOfE = Counttester.count("E")
print(CounterOfe + CounterOfE )

print()
print()

LetterFinder = "What song was or do you want to be the your first dance at your wedding, What song would make the best theme music for you, What is the most irrational superstition you have, What is the most unbelievable-yet-true excuse you have ever had for being late"
print(LetterFinder)
Finder = LetterFinder.find("x")
print(Finder)

print()
print()

WordReplacer = "Pxper bxgs hxve been lxrgely replxced by plxstic bxgs"
print(WordReplacer)
Replacer = WordReplacer.replace("x","a")
print(Replacer)

#///
print()
print()

islowertester = "I Love"
print(islowertester)
Lowertester = islowertester.islower()


print("test")
for Words in islowertester:
    if Words.isalpha():
        Words = Words.islower()
        print(Words)

#///
        
#/// is
        .
print()
print()

isHIGERtester = "Sign In"
print(isHIGERtester)
Highertester = isHIGERtester.islower()


print()
for Wordss in isHIGERtester:
    if Wordss.isalpha():
        Wordss = Wordss.isupper()
        print(Wordss)

#///
                
#/// is digit / is alnum
print()
print()

isDIGITtester = "O 0O 0 0O"
print(isDIGITtester)
Digittester = isDIGITtester.islower()


print()
for Wordsss in isDIGITtester:
    if Wordsss.isalnum():
        Wordsss = Wordsss.isdigit()
        print(Wordsss)

#///

