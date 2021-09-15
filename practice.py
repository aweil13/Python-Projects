import random

guess_number = random.randint(1,20)

print("Howdy! What's your name?")
username = input("Name: ")

guesses = 3

print(username,'you have three attempts to guess a number between 1 and 20')

for i in range(1, guesses+1):
  guess = input("Guess:")
  guess = int(guess)
  if guess == guess_number:
    print(f"Congrats {username}, you win!")
    break
  elif guess > guess_number:
    print("Your number is too high!")
    guesses = guesses - 1
    print(f"You have {guesses} remaining.")
  elif guess < guess_number:
    print("Your number is too low!")
    guesses = guesses - 1
    print(f"You have {guesses} remaining.")
  elif guesses <= 0:
    print("You lose!")
  