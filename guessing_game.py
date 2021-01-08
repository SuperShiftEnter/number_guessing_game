import random as rnd

random_number = rnd.randint(1, 100)
is_correct = False

# remove comment to print random number
print(random_number)

print("Please guess a full number between 1 and 100. \nIf you wish to stop playing, press Ctrl+C.")

while is_correct == False:
    user_input = input("Input: ")
    try:
        if int(user_input) == random_number:
            print(F"Well done! \n{user_input} is correct!")
            is_correct = True
        elif int(user_input) < 1 or int(user_input) > 100:
            print(F"{user_input} is out of bounds (1 - 100)")
        else:
            if int(user_input) > random_number:
                print("Please enter a lower number.")
            else:
                print("Please enter a higher number.")
    except ValueError:
        print(F"{user_input} is not a valid number.")
        continue
