print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to retrieve a code to have access to the prize.\nYou will each have one life and one life only so think wisely before answering!\nAlso Allah is watching you so no CHEATING!!!")
Name = input("What is your Name?")
print("Assalamualaikum " + Name)
Start_Game=input("Are you ready to start?").lower()
if Start_Game != "yes" and Start_Game!=" yes" and Start_Game!="yh":
    print("Thank you for playing See you next time!")
else:
    print("Say BismiAllah, Lets begin:")
    Step1= input("You are at your first step, If you answer the question correct you can move to the next stage.\nSo " + Name+ " What can you hold in your right hand,but never in your left hand?\n" ).lower()
    if Step1 != "your left hand" and Step1!="left hand" and Step1!="my left hand" and Step1!="lefthand": # if you used or here it wouldnt work, because say you picked left hand it wouldnt equal the first one but would the second one which makes the if true as thats the or rules and would trigger the print statement
        print("WRONG!,YOU HAVE LOST THE GAME,GOODBYE.")
    else:
        print("Well done, You seem like a smart one but dont get too confident.")
        Step2=input("You are at the second step now "+ Name +".""Your next question is:\nTwo in a corner, one in a room, zero in a house, but one in a shelter. What am I?\n").lower()
        if Step2=="r" or Step2=="the letter r" or Step2=="letter r":
            print("You think you're on a roll, Dont worry it only gets harder from here,\nYou have 3 more questions left brace yourself.")
            Step3=input("The 22nd and 24th presidents of the United States of America had the same parents but were not brothers.\nHow can this be possible?\n")
            if Step3=="they are the same person" or Step3=="1 person" or Step3=="1 man" or Step3=="one man" or Step3=="they were the same person" or Step3=="same person" or Step3=="he was both" or Step3=="it/’s the same president twice" or Step3=="The president served twice" or Step3=="president served twice" or Step3=="same man":
                print("Well done, Two more questions from the Promise land")
                Step4=input("You're on the 4th step "+Name+ ".""Next question:A man steals a $100 bill from a shop. He then uses that $100 bill to buy $70 worth of goods. The shop owner hands him back $30 in change.\nHow much money did the shop owner lose? $").lower()
                if Step4 != "100" and Step4!="one hundred":
                    print("SO CLOSE BUT SO FAR, MAYBE NEXT TIME BUDDY, GAME OVER!")
                else:
                    print("WOW, You made it to the last Stage, No pressure!")
                    Step5=input("You walk into a room, and you see a bed. On that bed, there are two cows, four dogs, one cat, a bear, three chickens flying above the bed and a goose.\nHow many legs are on the floor?").lower()
                    if Step5 != "6" and Step5!="six" and Step5!=" 6" and Step5!=" six":
                        print("Im sorry to say this, But you have failed at the last hurdle, Maybe next time.LOSER!")
                    else:
                        print("CONGRATULATIONS!!!!! YOU ARE THE WINNER refer the Code 'Happy Hippo' to redeem prize.")

            else:
                print("LOSER!!! GAME OVER, GOOD TRY BUT NOT GOOD ENOUGH!")




        else:
            print("LOSER!!! GAME OVER, GOOD TRY BUT NOT GOOD ENOUGH!")


