#Written by: Liam Hendrickson on 10/08/2017
#   A game of Rock, Paper, Scissors, Lizard, Spock using a random number generator 
#   Can repeat if the player wishes and will keep score to print out when the player chooses to quit


import random

#   Rules and instructions on how to play

def instructions():   
    
    print("\nTo play Rock, Paper, Scissors, Lizard, Spock type in your what you would like to throw")
    print("The computer will randomly select what to throw and will state who wins the toss")
    print("\nRemember: Rock beats Scissors and Lizard \n\t  Paper beats Rock and Spock \n\t  Scissors beats Lizard and Paper \n\t  Lizard beats Spock and Paper \n\t  Spock beats Rock and Scissors")

    
    main()
    
#   Plays the game

def main():
    
    response = "y"

    total_wins = 0

    total_losses = 0
    
    while response == "yes" or response == "Yes" or response == "y" or response == "Y" or response == "Yes":

        players_throw = str(input("\n\nWhat do you want to throw?  "))

#   Assign a value to players_throw
        
        if players_throw ==  "lizard" or players_throw == "Lizard" :

            players_throw_value = 1
         
        elif players_throw ==  "rock" or players_throw == "Rock":

            players_throw_value = 2

        elif players_throw ==  "paper" or players_throw == "Paper":

            players_throw_value = 3

        elif players_throw ==  "spock" or players_throw == "Spock":

            players_throw_value = 4

        elif players_throw ==  "scissors" or players_throw == "Scissors":

            players_throw_value = 5

        else:   #   Invalid Input

            print("\nError: please enter a valid response")

            main()

#   Get a random number

        computers_throw_value = random.randint(1, 5)

#   Assign a string to the generated number

        if computers_throw_value == 1:

            computers_throw = "Lizard"

        elif computers_throw_value == 2:

            computers_throw = "Rock"

        elif computers_throw_value == 3:

            computers_throw = "Paper"

        elif computers_throw_value == 4:

            computers_throw = "Spock"

        elif computers_throw_value == 5:

            computers_throw = "Scissors"

#   Tie Game Conditions

        if computers_throw_value == players_throw_value: 

            print("\nComputer plays", computers_throw)
            print("Tie Game")
           

            wins = 0
            losses = 0
            
#   Losing Throws
    
        elif (players_throw_value == 1) and (computers_throw_value == 2 or computers_throw_value == 5):

            print("\nComputer plays", computers_throw)
            print(computers_throw, "beats", players_throw)
            print("You Lose")
           

            wins = 0
            losses = 1

        elif (players_throw_value == 2) and (computers_throw_value == 3 or computers_throw_value == 4):

            print("\nComputer plays", computers_throw)
            print(computers_throw, "beats", players_throw)
            print("You Lose")
           

            wins = 0
            losses = 1

        elif (players_throw_value == 3) and (computers_throw_value == 1 or computers_throw_value == 5):

            print("\nComputer plays", computers_throw)
            print(computers_throw, "beats", players_throw)
            print("You Lose")
            

            wins = 0
            losses = 1

        elif (players_throw_value == 4) and (computers_throw_value == 3 or computers_throw_value == 1):

            print("\nComputer plays", computers_throw)
            print(computers_throw, "beats", players_throw)
            print("You Lose")
           

            wins = 0
            losses = 1

        elif (players_throw_value == 5) and (computers_throw_value == 4 or computers_throw_value == 2):

            print("\nComputer plays", computers_throw)
            print(computers_throw, "beats", players_throw)
            print("You Lose")
          

            wins = 0
            losses = 1

#Winning Throw
    
        else:

            print("\nComputer plays", computers_throw)
            print(players_throw, "beats", computers_throw)
            print("Congratulations! You Win!")
           
            wins = 1
            losses = 0

        response = str(input("\nWould you like to play again? y/n:  "))

        total_wins += wins
        
        total_losses += losses

    score(total_wins, total_losses)

#   Decide winner when player chooses to quit

def score(wins, losses):

    total_wins = wins 

    total_losses = losses

    if total_wins > total_losses:

        print("\nYou Win", total_wins, " - ", total_losses)

    elif total_losses > total_wins:

        print("\nComputer Wins", total_losses, " - ", total_wins)

    elif total_wins == total_losses:

        print("\nYou Tied", total_wins, " - ", total_losses)

instructions()

