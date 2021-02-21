import random

chips = 100
choice = 1
exit = False
playerTotal = 0
computerTotal = 0
compCoice = 1
run = True

loop = True
print("You have ", chips, " chips.\n")
while exit == False:                                                                        #while we don't exit
    bet = int(input("Please enter bet 1-10 chips (Not more than you have):"))               #input num of chips
    while loop == True:
        if bet < 1 or bet > 10 or bet > chips:
            bet = int(input("Please enter bet 1-10 chips (Not more than you have):"))       #input num of chips
            loop = True
        else:
            loop = False
    loop = True

          
    randNum1 = random.randint (1,10)                
    randNum2 = random.randint (1,10)
    print("Your cards are: ", randNum1, " ", randNum2)
    dealerNum = random.randint (1,10)
    computerTotal+=dealerNum
    print("Visible dealer card: ", dealerNum)
    playerTotal = playerTotal + randNum1 + randNum2
    print("Your total = ", playerTotal)
    if randNum1 == 1 and randNum2 == 10 or randNum1 == 10 and randNum2 == 1 :   #if user has blackjack
        print("BlackJack!!")
        wins = True
    else:                                                                       #Keep going if no black jack
        while run == True:
            choice = int(input("Choose one: \n1. Hit \n2. Stay. "))
            while loop == True:                                                 #tests to make sure proper data
                   if choice<1 or choice >2:
                       loop = True
                       choice = int(input("Please choose either '1' or '2'! "))
                   else:
                       loop = False
            loop = True                                                         #resets loop for next time
            if choice == 1:
                randNum2 = random.randint (1,10)
                playerTotal += randNum2
                print("Your new card is ", randNum2)
                print("Your total = ", playerTotal)
                if playerTotal > 21:
                    print("Your total is:", playerTotal,"that is over 21, you lose")
                    wins = False
                    run = False
            if choice == 2:                                                     #computer's turn now. simulate hidden card
                print("Computer Turn:\n")
               
    
                
                while computerTotal < 17:                                       #computer takes cards until seventeen or greater
                        dealerNum = random.randint (1,10)
                        computerTotal +=dealerNum
                        print("The new dealer card: ", dealerNum)
                        print("The dealer total is: ", computerTotal)
                        
                if computerTotal > 21:                                          
                        wins = True
                elif computerTotal>playerTotal:
                        wins = False
                else:
                        wins = True
                run = False
                    
                        
    if computerTotal == playerTotal:                                            #tie
        print("It's a tie! You get your money back!")
    elif wins == True:                                                          #win
        print("\nYou Win!\n")
        chips+=bet
        print("You have ", chips, " chips.\n")                                  #loose
    elif wins == False:
        print("\nYou loose\n")
        chips-=bet
        print("You have ", chips, " chips.\n")
    bet = 0                                                                     #resets variables
    playerTotal = 0
    computerTotal = 0
    if chips > 0:
        choice = int(input("Choose 1:\n1. Play again\n2. Quit\n"))
        while loop == True:                                                     #tests to make sure proper data
            if choice<1 or choice >2:
                loop = True
                choice = int(input("Please choose either '1' or '2'! "))
            else:
                loop = False
        loop = True                                                             #resets loop
        if choice ==1:
            run = True
            
        if choice ==2:
            exit = True
    else:
        print("You have no chips. You lose.")
        exit = True
        
                        
                
              
                
            
        

    
