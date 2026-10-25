import os
import csv

# Weight Lose
def weight_lose(TDEE, weight_lose_calories):
    return  TDEE - weight_lose_calories 

# Weight Gain
def weight_gain(TDEE, weight_gain_calories):
    return TDEE + weight_gain_calories 

# Execution starts from here
if __name__ == "__main__":
    # Get details
    name = input("Name:")
    age = int(input("Age:"))
    weight = float(input("Weight kg's:"))
    height = float(input("Height inche's:"))
    height *= 2.54

    # Estimation of BMR and TDEE
    BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    print(f"\nYour body need {BMR} calories for bodily functions")
    print("\n1. Sedentary (little to no exercise)\n2. Lightly Active (light exercise 1–3 days/week)\n3. Moderately Active (moderate exercise 3–5 days/week)\n4. Very Active (hard exercise 6–7 days/week)")
    activity_level = int(input("\nChoose activity level:"))
    if activity_level == 1:
        TDEE = BMR * 1.2
    elif activity_level == 2:
        TDEE = BMR * 1.375
    elif activity_level == 3:
        TDEE = BMR * 1.55
    elif activity_level == 4:
        TDEE = BMR * 1.725
    else:
        print("Choosen Wrong Option!!!")

    # Choose for weight gain, weight lose and balanced 
    mode = int(input("\n1. To Lose Weight\n2. To Gain Weight\n3.To Maintain Weight\n\nChoice:"))
    if mode == 1:
        weight_lose_calories = int(input("\nChoose 300 t0 500 Calorie deficit(Calories from body fat):"))
        calories_weight = weight_lose_calories
        calories = weight_lose(TDEE, weight_lose_calories)
        mode = "Weight Lose"
        print(f"In take of Calories to lose weight:{calories}")
    elif mode == 2:
        weight_gain_calories = int(input("Extra calories to in take 100 to 500:"))
        calories_weight = weight_gain_calories
        calories = weight_gain(TDEE, weight_gain_calories)
        mode = "Weight Gain"
        print(f"In take of Calories to gain weight:{calories}")
    elif mode == 3:
        calories = TDEE
        mode = "Maintain Weight"
        calories_weight = calories
        print(f"To maintain Weight:{calories}")
    else:
        print("Choosen Wrong Option!!!")

file_path = f"user_data/{name}.csv"
data = [[name, age, weight, height, mode, calories_weight, calories]]
if os.path.exists(file_path):
    with open(file_path, "a", newline="") as file:
        write = csv.writer(file)
        write.writerow(data)
else:
    data = [["Name", "Age", "Weight", "Height", "Mode", "calories_weight", "Calories"],
            [name, age, weight, height, mode, calories_weight, calories]]
    with open(file_path, "x", newline="") as file:
        write = csv.writer(file)
        for line in data:
            write.writerow(line)