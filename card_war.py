import random

suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
  'ten', 'jack', 'queen', 'king', 'ace')

values = {
  'two':2,
  'three':3,
  'four':4,
  'five':5,
  'six':6,
  'seven':7,
  'eight':8,
  'nine':9,
  'ten':10,
  'jack':11,
  'queen':12,
  'king':13,
  'ace':14
}

#CARD CLASS
class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__(self):
    return f"{self.rank }  of   {self.suit}"

# first_card = Card('Hearts', 'two')
# print(first_card.value)
class Deck:
  def __init__(self):
    self.all_cards = []
    for suit in suits:
      for rank in ranks:
        created_card = Card(suit, rank)
        self.all_cards.append(created_card)
  def shuffle(self):
     random.shuffle(self.all_cards)
  
  def deal_one(self):
    return self.all_cards.pop()
  

class Player:

  def __init__(self, name):
    self.name = name 
    self.all_cards = []
  
  def remove_one_card(self):
    return self.all_cards.pop(0)

  def add_cards(self, new_cards):
    if type(new_cards) == type([]):
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)
  
  def __str__(self):
    return f"Player {self.name} has {len(self.add_cards)} cards."


player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()

player_one.add_cards(new_deck.all_cards[::2])
player_two.add_cards(new_deck.all_cards[1::2])
print(player_one.all_cards[0])

game_on = True

round_num = 0

while game_on:
  round_num += 1
  print(f"Round {round_num}")
  if len(player_one.all_cards) == 0:
    print(f"Game Over: Player one out of cards, Plyaer two wins!")
    game_on = False
    break
  if len(player_two.all_cards) == 0:
    print(f"Game Over: Player two out of cards, Plyaer one wins!")
    game_on = False
    break

  player_one_cards = []
  player_one_cards.append(player_one.remove_one_card())
  player_two_cards = []
  player_two_cards.append(player_two.remove_one_card())
 
  at_war = True
  while at_war:

    if player_one_cards[-1].value > player_two_cards[-1].value:
      player_one.add_cards(player_one_cards)
      player_one.add_cards(player_two_cards)
      at_war = False
    elif player_one_cards[-1].value < player_two_cards[-1].value:
      player_two.add_cards(player_one_cards)
      player_two.add_cards(player_two_cards)
      at_war = False
    
    else:
      print("WAR!")
      if len(player_one.all_cards) < 5:
        print("Player One unable to continue")
        print("Player two wins!")
        game_on = False
        break
      elif len(player_two.all_cards) < 5:
        print("Player Two unable to continue")
        print("Player one wins!")
        game_on = False
        break
      else:
        for num in range (5):
          player_one_cards.append(player_one.remove_one_card())
          player_two_cards.append(player_two.remove_one_card())







