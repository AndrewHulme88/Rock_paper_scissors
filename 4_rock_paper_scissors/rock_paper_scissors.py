import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ai_choice = random.randint(0,2)
player_choice = input("0 for rock, 1 for paper or 2 for scissors?\n")

if player_choice == "0" and ai_choice == 0:
    print("You choose rock!")
    print(rock)
    print("The computer chose rock!")
    print(rock)
    print("It's a draw!")
elif player_choice == "0" and ai_choice == 1:
    print("You choose rock!")
    print(rock)
    print("The computer chose paper!")
    print(paper)
    print("You lose!")    
elif player_choice == "0" and ai_choice == 2:
    print("You choose rock!")
    print(rock)
    print("The computer chose scissors!")
    print(scissors)
    print("You win!")  
elif player_choice == "1" and ai_choice == 0:
    print("You choose paper!")
    print(paper)
    print("The computer chose rock!")
    print(rock)
    print("You win!")  
elif player_choice == "1" and ai_choice == 1:
    print("You choose paper!")
    print(paper)
    print("The computer chose paper!")
    print(paper)
    print("It's a draw!")  
elif player_choice == "1" and ai_choice == 2:
    print("You choose paper!")
    print(paper)
    print("The computer chose scissors!")
    print(scissors)
    print("You lose!")  
elif player_choice == "2" and ai_choice == 0:
    print("You choose scissors!")
    print(scissors)
    print("The computer chose rock!")
    print(rock)
    print("You lose!")  
elif player_choice == "2" and ai_choice == 1:
    print("You choose scissors!")
    print(scissors)
    print("The computer chose paper!")
    print(paper)
    print("You win!")  
elif player_choice == "2" and ai_choice == 2:
    print("You choose scissors!")
    print(scissors)
    print("The computer chose scissors!")
    print(scissors)
    print("It's a draw!")  
