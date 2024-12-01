import random
instagram_users = [
    {"name": "Cristiano Ronaldo", 
     "career": "Footballer", 
     "followers": 630000000},

    {
        "name": "Lionel Messi",
      "career": "Footballer", 
      "followers": 500000000
    },

    {"name": "Selena Gomez", 
     "career": "Actor & Singer", 
     "followers": 430000000},
    {"name": "Kylie Jenner", 
     "career": "Businesswoman & Reality TV Star",
    "followers": 410000000},
    {"name": "Kim Kardashian", "career": "Businesswoman & Reality TV Star", "followers": 370000000},
    {"name": "Dwayne Johnson", "career": "Actor & Fitness Enthusiast", "followers": 350000000},
    {"name": "Ariana Grande", "career": "Singer", "followers": 340000000},
    {"name": "Beyoncé", "career": "Singer", "followers": 300000000},
    {"name": "Kendall Jenner", "career": "Model & Businesswoman", "followers": 280000000},
    {"name": "Neymar Jr", "career": "Footballer", "followers": 250000000},
    {"name": "Virat Kohli", "career": "Cricketer", "followers": 240000000},
    {"name": "Khloé Kardashian", "career": "Businesswoman & Reality TV Star", "followers": 230000000},
    {"name": "Justin Bieber", "career": "Singer", "followers": 230000000},
    {"name": "Taylor Swift", "career": "Singer-Songwriter", "followers": 230000000},
    {"name": "Nike", "career": "Sportswear Brand", "followers": 220000000},
    {"name": "National Geographic", "career": "Photography & Exploration", "followers": 210000000},
    {"name": "Real Madrid C.F.", "career": "Football Club", "followers": 190000000},
    {"name": "Cristiano Ronaldo Jr.", "career": "Footballer", "followers": 180000000},
    {"name": "Leonardo DiCaprio", "career": "Actor", "followers": 170000000},
    {"name": "Robert Downey Jr.", "career": "Actor", "followers": 160000000}
]

print("Welcome to Higher lower game. ")

score = 0

isRight = True

while isRight == True:
   rand1 = random.randint(1, len(instagram_users) - 1)
   firstPerson = instagram_users[rand1]
   fName = firstPerson["name"]
   fcareer = firstPerson["career"]
   fFollowers = firstPerson["followers"]
   print(f"{fName} a {fcareer} has {fFollowers} Followers \n")

   print('''__     ______  
\ \   / / ___| 
 \ \ / /\___ \ 
  \ V /  ___) |
   \_/  |____/  \n''')

   rand2 = random.randint(1, len(instagram_users) - 1)
   secondPerson = instagram_users[rand2]
   sname = secondPerson["name"]
   scareer = secondPerson["career"]
   sFollowers = secondPerson["followers"]
   print(f"{sname}, a {scareer} has higher or lower followers \n")

   target = input(f"type H if {fName} has more followers or L if lower ").upper()
    
   if target == "H" and fFollowers > sFollowers:
        score += 1
        print("Correct \n")
        
   elif target == "L" and fFollowers < sFollowers:
        score += 1
        print("Correct \n")
        
   else:
        print("You lose")
        isRight = False
   print(f"Your total score is: {score}")