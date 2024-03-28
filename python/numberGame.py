import random

# Generate a random number between 1 and 100 (or any desired range)
secret_number = random.randint(1, 100)

# Set maximum tries
max_tries = 3

# Start the guessing loop
for guess_count in range(max_tries):
  # Get user guess
  guess = int(input("Guess a number between 1 and 100: "))

  # Check if guess is correct
  if guess == secret_number:
    print("Congratulations! You guessed the number in", guess_count + 1, "tries.")
    break  # Exit the loop on correct guess

  # Provide hint based on guess
  elif guess < secret_number:
    print("Your guess is too low. Try again.")
  else:
    print("Your guess is too high. Try again.")

# Reveal the answer if not guessed within tries
if guess_count == max_tries - 1:
  print("You ran out of tries. The secret number was", secret_number)
