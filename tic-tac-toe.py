# author: Solai
# 
#implementation of classic 3x3 Tic-Tac-Toe game simulation

import random

def displayboard(board):
  print("\n" * 100) #clear the screen
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |')

def user_input():
  '''
  output == (player 1 marker, player 2 marker)
  '''
  marker = ' '

  while not (marker == 'X' or marker == 'O'):
    marker = input('Player1: Enter X or O:').upper()
  
  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')

def place_marker(board, marker, pos):
  board[pos] = marker

def wincheck(board, mark):
  return ((board[1] == board[2] == board[3] == mark) or #bottom row
  (board[4] == board[5] == board[6] == mark) or #middle row
  (board[7] == board[8] == board[9] == mark) or #top row
  (board[7] == board[4] == board[1] == mark) or #1st column
  (board[8] == board[5] == board[2] == mark) or #2nd column
  (board[9] == board[6] == board[3] == mark) or #3rd column
  (board[7] == board[5] == board[3] == mark) or #1st diagonal
  (board[9] == board[5] == board[1] == mark)) #2nd diagonal

def choose_first_player():
  toss = random.randint(0, 1)
  if toss == 0:
    return 'Player1'
  else:
    return 'Player2'

def is_free_slot(board, pos):
  return board[pos] == ' '

def is_board_full(board):
  for i in range(1, 10):
    if is_free_slot(board, i):
      return False

  return True

def get_player_choice_for_pos(board):
  pos = 0

  while pos not in range(1, 10) or is_free_slot(board, pos) == False:
    pos = int(input('Enter the slot to fill: (1-9)'))
    
  return pos

def playagain():
  ch = input('Enter Yes to play again!').upper()
  return ch == 'YES' or ch == 'Y'

#play the game
print('Welcome to Tic-Tac-Toe game')

while True:
  #play the game
  ##setup the game such as board, marker, who will play first - player1 or player2
  gameboard = [' ']*10
  p1_marker, p2_marker = user_input()
  
  play_turn = choose_first_player()
  print(play_turn + 'will play first')
  
  ok_to_play = input('ready to play the game? Y or N?').upper()
  if ok_to_play == 'Y':
    is_play = True
  else:
    is_play = False

  ##actual play  
  while is_play:
    ### p1's turn
    if play_turn == 'p1':
      # display the current board
      displayboard(gameboard)
      # let the player choose the position to fill
      pos = get_player_choice_for_pos(gameboard)
      # place the marker on the chosen position
      place_marker(gameboard, p1_marker, pos)
      # check if p1 won
      if wincheck(gameboard, p1_marker):
        displayboard(gameboard)
        print('P1 has won this game!!!')
        is_play = False
      # check if there is a tie
      else:
        if is_board_full(gameboard):
          displayboard(gameboard)
          print('game is tied!')
          is_play = False
        # if it is no win or no tie, then let the p2 play.
        else:
          play_turn = 'p2'
    ### p2's turn
    else:
      # display the current board
      displayboard(gameboard)
      # let the player choose the position to fill
      pos = get_player_choice_for_pos(gameboard)
      # place the marker on the chosen position
      place_marker(gameboard, p2_marker, pos)
      # check if p2 won
      if wincheck(gameboard, p2_marker):
        displayboard(gameboard)
        print('P2 has won this game!!!')
        is_play = False
      # check if there is a tie
      else:
        if is_board_full(gameboard):
          displayboard(gameboard)
          print('game is tied!')
          is_play = False
        # if it is no win or no tie, then let the p1 play.
        else:
          play_turn = 'p1'    
  
  #players don't want to continue with a new game! 
  #this is after someone winning the current game or there is a tie. 
  if not playagain():
    break
