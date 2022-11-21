import random

test_board = ['#','X','O','X','O','X','O','X','O','X']
def display_board(board):
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('------')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('------')
  print(board[7] + '|' + board[8] + '|' + board[9])
  return board
  
def define_players():
  #player_two_sign = None
  while True:
    # player_two_sign = None
    player_one_sign = input("please chose your sign 'X' or 'O'")
    if player_one_sign == 'X':
      player_two_sign = 'O'
      break
    elif player_one_sign == 'O':
      player_two_sign = 'X'
      break
    else:
      pass
  return (player_one_sign, player_two_sign)
#define_players()

def place_marker(board,marker,position):
  board[position] = marker
# place_marker(test_board, '$', 8)
# display_board(test_board)

def win_check(board, mark):
 return ((board[1] == mark and board[2] == mark and board[3] == mark) or
 (board[4] == mark and board[5] == mark and board[6] == mark) or
 (board[7] == mark and board[8] == mark and board[9] == mark) or
 (board[1] == mark and board[4] == mark and board[7] == mark) or
 (board[2] == mark and board[5] == mark and board[8] == mark) or
 (board[3] == mark and board[6] == mark and board[9] == mark) or
 (board[1] == mark and board[5] == mark and board[9] == mark) or
 (board[3] == mark and board[5] == mark and board[7] == mark))
def choose_first():
  flip = random.randint(0,1)
  if flip == 0:
    return 'Player 1'
  else:
    return ' Player 2'

def space_check(board, position):
  return board[position] == ' '

def full_board(board):
  for i in range(1,10):
    if space_check(board, i):
      return False
    
  return True

def player_choice(board):
  position = 0
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    position = int(input("choose a position (1 -- 9)"))
  return position

def play_again():
  choice = input("Would you like to play again? 'Yes' or 'No'")
  return choice == 'Yes'

print("Welcome to the Game Ready!")
while True:

  the_board = [' ']*10
  player_one, player_two = define_players()

  turn = choose_first()
  print(turn+ ' will play first')

  stating = input("Ready to go! Y or N")
  if stating == 'Y':
    game_on = True
  else: 
    game_on = False
  
  while game_on:
    if turn == 'Player 1':
      display_board(the_board)
      position = player_choice(the_board)
      place_marker(the_board, player_one, position)
      if win_check(the_board, player_one):
        display_board(the_board)
        print('Player one has won!')
        game_on = False
      else:
          if full_board(the_board):
            display_board(the_board)
            print('tie game ')
            game_on = False
          else:
            turn = 'Player 2'
    else:
      if turn == 'Player 2':
        display_board(the_board)
        position = player_choice(the_board)
        place_marker(the_board, player_two, position)
      if win_check(the_board, player_two):
        display_board(the_board)
        print('Player Two has won!')
        game_on = False
      else:
          if full_board(the_board):
            display_board(the_board)
            print('tie game ')
            game_on = False
          else:
            turn = 'Player 1'


  if not play_again():
    break
