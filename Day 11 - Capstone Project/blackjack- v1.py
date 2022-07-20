############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
import random
import click

def blackjack():
  user_cards = []
  computer_cards = []
  
  if(start_game == 'y'):
    print(logo)
    
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    user_score = user_cards[0] + user_cards[1]
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_score = computer_cards[0] + computer_cards[1]
    print(f"    Computer's first card: {computer_cards[0]}")

    turns_over = False

    while user_score < 21 and not turns_over:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card == 'y':
        current_score = random.choice(cards)
        if(current_score == 11 and user_score + current_score > 21):
            current_score = 1  
        user_cards.append(current_score)
        user_score += current_score
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
      else:
        turns_over = True

    while computer_score < 17:
      current_score = random.choice(cards)
      if(current_score == 11 and computer_score + current_score > 21):
            current_score = 1 
      computer_cards.append(current_score)
      computer_score += current_score

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score:   {computer_score}")

    if user_score == 21:
      print("Win with a Blackjack 😎")
    elif user_score > 21:
      print("You went over. You lose 😭")
    elif computer_score > 21:
      print("Opponent went over. You win 😁")
    elif (computer_score > user_score):
      print("You lose 😤")
    else:
      print("You won 😃")

    
start_game = 'y'

while(start_game == 'y'):
  start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  click.clear()
  blackjack()
  

