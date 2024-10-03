# d)TODO: Implement a function called `secret_number_game` that does the following:
# - Use a variable `secret_number` set to 42
# - The function should take one parameter `guess`
# - If the guess is correct, it should print "Correct!" and increment a global counter `correct_guesses`
# - If the guess is incorrect, it should print "Wrong!" and increment a global counter `wrong_guesses`
# - The function should then be used in the while loop below to guess the secret number.
# Your code here

# Global counters
correct_guesses = 0
wrong_guesses = 0

def secret_number_game(guess):
    global correct_guesses, wrong_guesses
    secret_number = 42
    
    if guess == secret_number:
        print("Correct!")
        correct_guesses += 1
    else:
        print("Wrong!")
        wrong_guesses += 1

while True:
    guess = int(input("Enter a guess: "))
    secret_number_game(guess)
    print(f"Correct guesses: {correct_guesses}, Wrong guesses: {wrong_guesses}")
    if correct_guesses == 1:
        break