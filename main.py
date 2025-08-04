import random

def main():
    # generate random number 1 - 100
    secret_number = random.randint(1, 100)

    print("Welcome to the Guess the Number game! By ZCode")
    print("I have selected a number between 1 and 100 and you have 7 attempts. Can You Try it?")

    attempts = 7

    while True:
        try:
            # Get User Play
            guess_choice = int(input("Enter your number: "))
            attempts -= 1
            
            if attempts < 0:
                print("Sorry, you've run out of attempts! The number was:", secret_number)
                break

            # Check Options
            if guess_choice == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess_choice < secret_number:
                print("Too low! Try again.")
                print(f'your remaining opportunities {attempts}')
            else:
                print("Too high! Try again.")
                print(f'your remaining opportunities {attempts}')

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
