import traceback

def calculator():
    # get user's input on dog_age
    dog_age = input("Enter your dog's age in years: ")
    try:
        # cast to a float
        d_age = float(dog_age)
        # convert dog age to human age
        # ensure input is not negative
        if d_age > 0:
            if d_age <= 1:
                h_age = d_age * 15
            elif d_age <= 2:
                h_age = d_age * 12
            elif d_age <= 3:
                h_age = d_age * 9.3
            elif d_age <= 4:
                h_age = d_age * 8
            elif d_age <= 5:
                h_age = d_age * 7.2
            else:
                h_age = 36 + (d_age - 5) * 7
            human_age = round(h_age, 2)
            # print instruction for valid input
            print('The given dog age', dog_age, 'is', str(human_age), 'in human years')
        else:
            print('Age cannot be a negative number.')
    except ValueError:
        print(dog_age, 'is invalid.')

calculator()  # This line calls the calculator function
