MyFloatValue = 9.82
print(type(MyFloatValue))
print(MyFloatValue)

str_my_number=str(MyFloatValue)
print(type(str_my_number))
print(str_my_number)

MyFloatValue2 = 9.82
print(type(MyFloatValue2))
print(MyFloatValue2)


int_my_number=int(MyFloatValue2)


year = input("Enter the current year")
age = int(input("What age will you be at the end of this year?")) #  Note the int() cast on the input
print("You were born in", year-age)
