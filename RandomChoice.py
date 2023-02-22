import random

choice = input("Enter Chore, Activity, or Meal: ")

Meals = ['Sausage and Rice', 'Fish and Rice', 'Chicken and Rice']
Chores = ['Fishtank', 'Vaccum', 'Kitchen']
Activities = ['Puzzle', 'Movie', 'Games']

Meal_Choice = random.choice(Meals)
Chores_Choice = random.choice(Chores)
Activities_Choice = random.choice(Activities)

if choice == 'Chore':

    print("Your chore is " + Chores_Choice)

elif choice == 'Activity':

    print("Your activity is " + Activities_Choice)

elif choice == 'Meal':

    print("Your meal is " + Meal_Choice)

else:
    print("Invalid Choice")