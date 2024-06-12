

Name = input ("Name: ")
print ("Enter weight in meters")
Height= float(input("Height:" ))
print ("weight in kilograms")
Weight = float(input("Weight:" )) 

BMI = Weight/Height**2

if BMI < 18.5:
    print(Name,"You are under weight")
elif BMI >=18.5 and BMI <25:
    print(Name,"you are Normal in weight")
elif BMI>=25 and BMI <30:
    print (Name,"Your are over weight")
else: print (Name,"You are Over weight")