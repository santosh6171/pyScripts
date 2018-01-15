i="yes"
while i != "no":
         player1opt = input("Player1 - Please enter your choice: rock/paper/scissors\n")
         if player1opt not in ('rock','paper','scissors'):
             print ("The option entered was incorrect, please start the game again with the correct option")
             exit()
         player2opt = input("Player2 - Please enter your choice: rock/paper/scissors\n")
         if player2opt not in ('rock','paper','scissors'):
             print ("The option entered was incorrect, please start the game again with the correct option")
             exit()
             
         if player1opt == "rock":
            if player2opt == "scissors":
                print ("Player1 wins Congratulations!, {0} beats {1}\n" .format(player1opt,player2opt))
            elif player2opt == "paper":
                print ("Player2 wins Congratulations!, {0} beats {1}\n" .format(player2opt,player1opt))
            else:
                print ("Errr..its a tie, both have opted for {0}\n" .format(player1opt))
         elif player1opt == "scissors":
            if player2opt == "rock":
                print ("Player2 wins Congratulations!, {0} beats {1}\n" .format(player2opt,player1opt))
            elif player2opt == "paper":
                print ("Player1 wins Congratulations!, {0} beats {1}\n" .format(player1opt,player2opt))
            else:
                print ("Errr..its a tie, both have opted for {0}\n" .format(player1opt))
         else:
            if player2opt == "scissors":
                print ("Player2 wins Congratulations!, {0} beats {1}\n" .format(player2opt,player1opt))
            elif player2opt == "rock":
                print ("Player1 wins Congratulations!, {0} beats {1}\n" .format(player1opt,player2opt))
            else:
                print ("Errr..its a tie, both have opted for {0}\n" .format(player1opt))

         i = input("Please press yes if you would like to play the game again else press no\n" )

