import numpy as np
import random
import sys

Card_Types = {
1: "Hearts",
2: "Spades",
3: "Diamonds",
4: "Clubs"
}

Card_numbers = [1,2,3,4,5,6,7,8,9,10]
Card_face = ["Jack", "Queen","King"]

print("Hello! Welcome to my Blackjack Game!")
name = input("What is your name: ")
print("Hello %s!" % (name))

# pulls a card
# returns a dictionary containing card and card type
def pullcard() :
    card = random.randrange(1,14)
    if card == 11 or card == 12 or card == 13 :
        card = Card_face[card - 11]
    
    card_type = Card_Types[random.randrange(1,5)]
    card_info = (card,card_type)
    return card_info

# prints a card
# needs a list as input for card, and an int declaring card number
def printcard(card, card_number) :
    print("Card %d: %s of %s" % (card_number, card[0], card[1]))

# returns point value for given card(s)
def cardpoints(*card) :
    cardpoint = 0
    for cardnum in card :
        if cardnum == "King" or cardnum == "Jack" or cardnum == "Queen":
            return 10
        else :
            cardpoint = cardpoint + cardnum
    return cardpoint

# checks if player busted
def bust(points) :
    if points > 21 :
        print("You busted...")
        quit()

card1 = pullcard()
card2 = pullcard()

printcard(card1, 1)
printcard(card2, 2)

CPU_card1 = pullcard()
CPU_card2 = pullcard()

loop = 1
while loop == 1 :
    move = input("Hit or Stand: ")
    print(move)
    if move == 'hit' or move == 'Hit' :
        card3 = pullcard()
        printcard(card3, 3)
        # print(cardpoints(card1[0],card2[0],card3[0]))
        bust(cardpoints(card1[0],card2[0],card3[0]))
    else :
        # print(cardpoints(card1[0],card2[0]))
        pass
        














