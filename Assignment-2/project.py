#Simple the_BMI calculator using python::

# define a function name convert to feet,inche  ::
def convert():
    print("Input your Informations-")
    h_ft = int(input("Feet: "))
    h_inch = int(input("Inches: "))
    
    h_inch += h_ft * 12
    h_cm = round(h_inch * 2.54, 1)
    print("Your height is : %d cm." % h_cm)

convert()


# define a function name The_BMI::

def the_BMI(height, weight):
    return round((weight /(height/100)**2),2)

# asking for input from the users::

Height = float(input("Enter your height in cm: "))
Weight = float(input("Enter your weight in kg: "))

# print to welcome calculator::

print("Welcome to the the_BMI calculator.")


# print Body Mass Index::

the_BMI = the_BMI(Height, Weight)
print("Your the_BMI is: ", the_BMI)


# using the if-elif-else conditions::

if (the_BMI<18.5):
    print('Oops! You are underweight.')
elif (the_BMI>=18.5) and (the_BMI<25):
    print("Awesome! You are healthy.")
elif (the_BMI>=25) and (the_BMI<30):
    print('Eee! You are overweight')
elif (the_BMI>=30):
    print('Seesh! You are obese.')
else:
    print("Enter Your Vaild Number") 



