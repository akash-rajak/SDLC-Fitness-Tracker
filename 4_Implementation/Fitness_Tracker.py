
'''

Fitness Tracker:
Here we will be calculating 5 points on Fitness of a person:
    i.) Work Out : it is calculated on the basis of Yoga, Cardio and Meditation
    ii.) BMI (Body Mass Index) : person's weight in kilograms divided by the square of height in meters.
    iii.) Water Intake : measure of water intake basically includes drinking water, water in beverages, and water that is part of food.
    iv.) BMR (Basal Metabolic Rate) : measures the amount of energy (in calories) — that our body needs to stay alive and function properly.
    v.) Approximately Calorie Burnt : It is calculated on the basis of BMR value and the amount of exercise done per week

'''


## i.) function defined to calcuate the work out
def getTime(type):
    did_ = input('Did you do ' + type + '? (yes/no): ')
    if did_.lower() == 'no':
        return 0
    else:
        time = float(input('Enter how long you did ' + type + '? (mins): '))
        return time

def workout():
    print('\nCalculating Work Out :')
    totalTime = [0, 0, 0]
    types = ['yoga', 'cardio', 'meditation']

    for type in types:
        time = getTime(type)
        if type == 'yoga':
            totalTime[0] += time
        elif type == 'cardio':
            totalTime[1] += time
        else:
            totalTime[2] += time

    if sum(totalTime) >= 3 * 20 * 1:
        print('Your fitness score is 5.0 on scale of 5.0')
    elif sum(totalTime) >= 3 * 20 * 1 * 0.8:
        print('Your fitness score is 4.0 on scale of 5.0')
    elif sum(totalTime) >= 3 * 20 * 1 * 0.6:
        print('Your fitness score is 3.0 on scale of 5.0')
    elif sum(totalTime) >= 3 * 20 * 1 * 0.4:
        print('Your fitness score is 2.0 on scale of 5.0')
    else:
        print('Your fitness score is 1.0 on scale of 5.0')


## ii.) function defined to Calculate BMI(Body Mass Index)
def BMI():
    print('\nCalculating BMI(Body Mass Index) :')
    the_height = float(input("Enter the height in cm : "))
    the_weight = float(input("Enter the weight in kg : "))
    the_BMI = the_weight / (the_height / 100) ** 2
    if the_BMI < 18.5:
        print("Your Body Mass Index is", the_BMI)
        print('Status : Underweight')
    if the_BMI >= 18.5 and the_BMI < 25:
        print("Your Body Mass Index is", the_BMI)
        print("Status : Normal")
    if the_BMI >= 25 and the_BMI < 30:
        print("Your Body Mass Index is", the_BMI)
        print('Status : Overweight')
    if the_BMI >= 30:
        print("Your Body Mass Index is", the_BMI)
        print('Status : Obesity')


## iii.) function defined to Calculate Water Intake
def waterIntake():
    print('\nCalculating Water Intake : ')
    the_weight = float(input("Enter the weight in kg : "))
    age = int(input("Enter the age : "))
    the_weight = the_weight * 2.20462
    if (age < 30):
        water_intake = the_weight * 40
    elif (age >= 30 and age < 55):
        water_intake = the_weight * 35
    elif (age >= 55):
        water_intake = the_weight * 30

    water_intake = water_intake / 28.3
    water_intake = water_intake * 0.0295735
    print('The water required for you will be : ', water_intake)


## iv.) function defined to Calculate BMR(Basal Metabolic Rate)
def BMR():
    print('\nCalculating BMR(Basal Metabolic Rate) :')
    the_height = float(input("Enter the height in cm : "))
    the_weight = float(input("Enter the weight in kg : "))
    age = int(input("Enter the age : "))
    gender = input('Enter gender (M/F) : ')
    if (gender == 'M'):
        bMR = 66 + (6.2 * the_weight) + (12.7 * the_height) - (6.76 * age)
    else:
        bMR = 655.1 + (4.35 * the_weight) + (4.7 * the_height) - (4.7 * age)
    print('BMR calculated is: ', bMR)
    return bMR


## v.) function defined to calculate the approx amount of calorie burnt
def approxCalorieBurnt():
    print('\nCalculating Approc Calorie Burnt : ')
    value = BMR()
    print('1.little to no exercise')
    print('2.light exercise 1–3 days a week')
    print('3.moderate exercise 3–5 days a week')
    print('4.exercises hard 6–7 days a week')
    print('5.extra active person ')
    exercise = int(input('Select your activity level:'))
    if (exercise == 1):
        print('Calorie need to burn for maintaining weight :', value * 1.2)
    if (exercise == 2):
        print('Calorie need to burn for maintaining weight :', value * 1.37)
    if (exercise == 3):
        print('Calorie need to burn for maintaining weight :', value * 1.55)
    if (exercise == 4):
        print('Calorie need to burn for maintaining weight :', value * 1.725)
    if (exercise == 5):
        print('Calorie need to burn for maintaining weight :', value * 1.9)

    # approxCalorieBurned()

def fitnessTracker():
    ## login and signup
    user_name = input('Enter Username : ')
    password = input('Enter Password : ')

    if(user.get(user_name)==None):
        user[user_name]=password
    elif(user.get(user_name)!=password):
        print("Incorrect Login Details")


    flag = 1
    while (flag == 1):
        print('\nWelcome to Fitness Tracker')
        print('Track yourself on the basis of :')
        print('1.) Workout')
        print('2.) BMI(Body Mass Index)')
        print('3.) WaterIntake')
        print('4.) BMR(Basal Metabolic Rate)')
        print('5.) Approximately Calorie Burnt')
        serialNumber = int(input('Select Option : '))
        if (serialNumber == 1):
            workout()
        if (serialNumber == 2):
            BMI()
        if (serialNumber == 3):
            waterIntake()
        if (serialNumber == 4):
            BMR()
        if (serialNumber == 5):
            approxCalorieBurnt()
        flag = int(input('\nWant to continue , Enter 1 for yes and 0 for No : '))
    print('Thanks for using fitness tracker')

user = {}

fitnessTracker()
