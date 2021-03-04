############### Blackjack Project #####################
import random
from art import logo
from replit import clear

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
  return sum(cards)
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def compare(user_score, computer_score):
  """Compare de user_score againts the computer_score"""
  if computer_score == user_score:
    return "It's a draw."
  elif computer_score == 0 or user_score > 21:
    return "The computer won!"    
  elif user_score == 0:
    return "You have a Blackjack! You win! "    
  elif computer_score > 21:
    return "You win!"
  elif user_score > computer_score:
    return "You win!"   
  elif computer_score > user_score:
    return "The computer won!"
def play_game():
  game_over = False
  print(logo)
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    total_score = sum(user_cards)
    print(f"Your cards: , {user_cards} Total Score:  {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      response = input("Do you want another card? Type 'y' or 'n' : ")
      if response == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand {user_cards}, Your final score {user_score}")
  print(f"Computer final hand: {computer_cards}, Computer final score: {computer_score}")
  print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' :") == "y":
  clear()
  play_game()
