import random

celebrity_names = [
    "Tom Hanks", "Leonardo DiCaprio", "Angelina Jolie", "Beyoncé", "Brad Pitt", 
    "Emma Watson", "Robert Downey Jr.", "Ariana Grande", "Dwayne Johnson", 
    "Scarlett Johansson", "Chris Hemsworth", "Rihanna", "Johnny Depp", "Taylor Swift",
    "Will Smith", "Meryl Streep", "Kanye West", "Oprah Winfrey", "Selena Gomez", 
    "Ellen DeGeneres", "Kylie Jenner"
]

def generate_random_celebrity():
    return random.choice(celebrity_names)

def guess_the_celebrity():
    celebrity = generate_random_celebrity()
    print("Welcome to the Celebrity Guessing Game! ")
    print("Guess the celebrity's name (case-sensitive): ")
    
    attempts = 3
    while attempts > 0:
        guess = input(f"You have {attempts} attempts left: ").strip()
        
        if guess == celebrity:
            print("Congratulations! You guessed the celebrity correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Wrong guess. Try again!")
            else:
                print(f"Sorry, you've run out of attempts. The celebrity was: {celebrity}")

guess_the_celebrity()
