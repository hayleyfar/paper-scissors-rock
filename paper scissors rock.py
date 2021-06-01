#paper scissors rock game
import random
print("Welcome to my paper scissors rock game! \nYou will be asked paper, scissors or rock and the program will also pick as well :D")
#list
program_answers = ["paper","scissors","rock"]
print("\n")
users_choice = input("paper, scissors or rock? \nYour answer: ")
#random word from list
program = random.choice(program_answers)
print("Program answer: " ,program )
#tie for all paper, scissors or rock answers
if users_choice == program:
 print("tie")

while users_choice == "paper":
 if program == "scissors":
   print("you lose")
   break #stop code
 elif program == "rock":
   print("you win!")
   break

while users_choice == "scissors":
 if program == "paper":
   print("you win!")
   break
 elif program == "rock":
   print("you lose")
   break

while users_choice == "rock":
 if program == "scissors":
   print("you win!")
   break
 elif program == "paper":
   print("you lose")
   break
