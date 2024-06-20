def calculate_bmi(user_weight, user_height_cm):
    user_height_m = user_height_cm / 100
    bmi_value = user_weight / (user_height_m ** 2)
    return bmi_value

def determine_bmi_category(bmi_value, user_name):
    if bmi_value < 18.5:
        return f"{user_name}, you are underweight."
    elif bmi_value <= 24.9:
        return f"{user_name}, your weight is normal."
    elif bmi_value < 29.9:
        return f"{user_name}, you are overweight."
    elif bmi_value < 34.9:
        return f"{user_name}, you are obese."
    elif bmi_value < 39.9:
        return f"{user_name}, you are severely obese."
    else:
        return f"{user_name}, you are morbidly obese."


user_name = input("Enter your name: ")
user_weight = float(input("Enter your weight in kgs: "))
user_height_cm = float(input("Enter your height in cms: "))

if user_weight > 0 and user_height_cm > 0:
    bmi_value = calculate_bmi(user_weight, user_height_cm)
    print(f"Your BMI is: {bmi_value:.2f}")
    print(determine_bmi_category(bmi_value, user_name))
else:
    print("Invalid input, please enter positive numbers for weight and height.")