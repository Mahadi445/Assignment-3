#=============Create BMI Calculator Project In Python===================#

#===========calculate Inche and Feet convert to centimeters===========#
Inch_per_feet = 12
cm_per_inch = 2.54
feet = int(input("Enter Your Height Number of feets:"))
inch = int(input("Enter Your Height Number Of Inches:"))
Height_cm = (feet*Inch_per_feet+inch)*cm_per_inch
print("Here Your Centimeters Number:",Height_cm)
print("============================================")


#============user Input Height and weight===============#
Height =float(input("Enter Your Height in Centimeters:"))
Weight =int(input("Enter Your Weight in KG:"))


#==========Set Formula Height And weight=======#
Height = Height/100
BMI = Weight/float((Height*Height))
print("Here Your Body Mass Index :",BMI)


#=============conditon apply For BMI===========#
if (BMI<18.5):
    print('Your Health is Underweight')
elif (BMI>=18.5) and (BMI<25):
    print("Your Health is Normal")
elif (BMI>=25) and (BMI<30):
    print('Your Health is Overweight')
elif (BMI>=30):
    print('Your Health is Obesity')
else:
    print("Enter Your Vaild Number")    
                 




