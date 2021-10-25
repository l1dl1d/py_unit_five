import random
def get_number():
    x = input("guess a number")
    if x == num:
        print("congratulations you guessed the right number")
    else:
        print("try again")
def get_guess():
    num = random.randint(1, 100)
    return num
def main():
