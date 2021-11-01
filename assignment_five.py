#Khalid
#10/30/21
#This program plays a guessing game that which generates a random number for the player to guess.
#There are three games and after every game the program gives how many tries it took to guess the random number.
#At the end the program gives you the average of the total amount of guess from all the games together.
import random
def get_number():
    """
    this function gets a random number and stores it in the variable num
    :return: returns a random number between 1 and 100
    """
    num = random.randint(1, 100)
    return num

def get_guess():
    """
    this function prevents players from going outside of the 1 to 100 range when guessing a number
    :return: returns number that is guessed between 1 and 100
    """
    while True:
        x = str(input("guess a number between one and one hundred"))
        if int(x) < 100 and int(x) > 1:
            return x
def main():
    """
    this function runs the entire game and calls all the other functions to put everything together
    :return: returns the entire game with everything put together
    """
    guesses_for_all_games = 0
    for y in range(3):
        total_guesses = 0
        num = get_number()
        while True:
            x = get_guess()
            total_guesses = total_guesses + 1
            guesses_for_all_games = guesses_for_all_games + 1
            if int(x) == num:
                print("congratulations you guessed the right number, it took you", total_guesses, "tries to get the answer")
                break
            elif int(x) > num:
                print("number was too high")
            else:
                print("number was too low")
    print("your average out of all three games was", guesses_for_all_games/3)
if __name__ == '__main__':
    main()
