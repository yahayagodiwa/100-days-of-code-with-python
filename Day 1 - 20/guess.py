# import random

# print("Welcome to number guessing Game \n")
# level = input("Choose how hard you want it. easy, medium or hard? \n").lower()

# isAtempt = True
    
# if level == "easy":
#     attempts = 10
# elif level == "medium":
#     attempts = 7
# elif level == "hard":
#     attempts = 5
# else:
#     print("Enter a valid level. easy, medium or hard ")
#     isAtempt = False
   
# while isAtempt == True:
   
#     answer = random.randint(1, 101)
#     guess = int(input("Guess a number \n"))

#     if guess < answer:
#         print("Too low ")
#     elif guess > answer:
#         print('Too high ')
#     else:
#         print(f"Congratulations! You've guessed the number {answer} correctly!")
    
#     if guess != answer:
#        if attempts != 1:
#           attempts -= 1
#           print(f"You have {attempts} attempts left ")
#        else:
#           print("You lose")
#           isAtempt = False
          
   
