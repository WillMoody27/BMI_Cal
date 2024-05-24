"""
William Hellems-Moody
- Python Review

Simple BMI Calculator (Python)

NOTE: 
BMI Scale
Under 18.5    Underweight    Minimal
18.5 - 24.9   Normal Weight  Minimal
25 - 29.9     Overweight     Increased
30 - 34.9     Obese          High
35 - 39.9     Severely Obese Very High
40 and over   Morbidly Obese Extremely High
"""

"""
@Params:
- weight (lbs.)
- height (in.)

BMI = (weight x 703) / (height x height)
"""

def bmi_calc(name, BMI_result): 
    if BMI_result > 0:
        if BMI_result < 18.5:
            print(name + ", you are underweight.")
        elif BMI_result <= 24.9:
            print(name + ", you are normal weight.")
        elif BMI_result < 29.9:
            print(name + ", you are overweight.")
        elif BMI_result < 34.9:
            print(name + ", you are obese.")
        elif BMI_result < 39.9:
            print(name + ", you are severely obese.")
        else:
            print(name + ", you are morbidly obese.")
    else:
        print("Enter valid input")


while True:
    calculate = input('Would you like to calculate your BMI (yes/no): ').strip().lower()
    if calculate in ['yes', 'y']: 
        name = input('Enter your name: ')
        weight = int(input("Enter your weight in pounds: "))
        height = int(input("Enter your height in inches: "))
        BMI = (weight * 703) / (height * height) # Formula to calculate BMI.
        print(f"Your BMI is {round(BMI, 2)}") # Round the BMI to 2 decimals.
        bmi_calc(name, BMI)
    elif calculate in ['no', 'n']:
        print('Thank you!')
        break
    else:
        print("Please enter 'yes' or 'no'.")
