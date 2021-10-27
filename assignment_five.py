import random
def get_guess():
    num = random.randint(1, 100)
    return num
def get_number():
    num = str(random.randint(1, 100))
    while True:
        x = str(input("guess a number"))
        if x == num:
            print("congratulations you guessed the right number")
            break
        elif x > num:
            print("number was too high")
        else:
            print("number was too low")
def main():
    get_guess()
    print(get_number())
if __name__ == '__main__':
    main()
