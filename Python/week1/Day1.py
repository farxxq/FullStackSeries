
#---------print statement----------
print("Assalamwalaikum !!!")

#---------input method-------------
haalChaal = input("How are you!?")
print(haalChaal,"Good to hear")
age = int(input("What is ur age?"))
print("Great so ur age is",age)


#----------Variables---------
print("----------Variables---------")
num = 10
name = "Safar"
decimal = 1.0

print ("num:",num,"name:",name,"decimal:",decimal)


#--------Data types ---------------
print("--------Data types ---------------")
## 1. Numbers - 
    # Integer (int) = 1,2,3,4,5
    # Float (float) = 1.0,2,3.6
    # complex  = imaginary value(not available at the moment but might get in future)

print("1. Numbers")
Type1 = 12
Type2 = 1.2
Type3 = 12j
print("Type1:",type(Type1))
print("Type2:",type(Type2))
print("Type3:",type(Type3))

## 2. Boolean -
    # True
    # False.
print("2. Boolean")
Type4 = True
Type5 = False
print("Type4:",type(Type4))
print("Type5:",type(Type5))

## 3. String -
    # "" (Double quotes)
    # '' (Single quotes)

print("3. String")
Type6 = "Safar"
print("Type6:", type(Type6))

#---------Type Casting/Type Conversion-------------
print("--------Type Casting/Type Conversion-------------")
# 1. int()
print("1. Int conversion:")

casting1 = "12" #Is in string
print("Casting1 type:",type(casting1))
#Converting to int
casting1 = int(casting1)
print("Casting1 type after conversion:",type(casting1))
print("Addition of converted Casting1:",casting1 + 1)

# 2. float()
print("2. Float conversion:")

casting2 = "12.3" #Is in string
print("Casting2 type:",type(casting2))
#Converting to float
casting2 = float(casting2)
print("Casting2 type after conversion:",type(casting2))
print("Addition of converted Casting2:",casting2 + 0.1)

# 3. str()
print("3. String conversion:")

casting3 = 12.3 #Is in float
print("Casting3 type:",type(casting3))
#Converting to string
casting3 = str(casting3)
print("Casting3 type after conversion:",type(casting3))
print("Addition of converted Casting3:",casting3 + " bday")

# 4. bool()
print("4. Boolean conversion:")

casting4 = "" #Is an empty string
casting5 = "Safar" #Is an empty string
print("Casting4 type:",type(casting4)) #false due to empty
print("Casting5 type:",type(casting5)) #true as it has some value
#Converting to float
casting4 = bool(casting4)
casting5 = bool(casting5)
print("Casting4 type after conversion:",type(casting4))
print("Addition of converted Casting4:",casting4)
print("Casting5 type after conversion:",type(casting5))
print("Addition of converted Casting5:",casting5)