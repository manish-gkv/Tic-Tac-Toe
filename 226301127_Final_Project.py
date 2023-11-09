#______________________Final_Capstone_Project________________________________#
#_________________________Manish_kumar_Akela_________________________________#
#___________________________226301127________________________________________#
#__________________________TIC_TAC_TOE_Game__________________________________#
#_____________________Submitted_to_Namit_Khanduja____________________________#

from random import randint

sample_board = """
This is the Sample Board for our Tic Tac Toe Game

   |   |
 7 | 8 | 9
   |   |
-----------
   |   |
 4 | 5 | 6
   |   |
-----------
   |   |
 1 | 2 | 3
   |   |

You have enter the position number between [1-9] for your move.
2 players should be able to play the game:
So Let's Start the Game!
"""


def player_details():
  """a function to take input details of Player 1 and Player 2."""

  player1 = input("Enter the name of player 1: ")
  player2 = input("Enter the name of player 2: ")
  print("Welcome to Tic Tac Toe Game", player1, "and", player2,
        "Let's Start the Game!")
  return player1, player2


def choose_first():
  """function that uses the random module to randomly decide which player goes
first.""" ""
  return randint(0, 1)


def display_board(board):
  """function to display the playing board. Board will have 3 rows and 3 columns.
Your function should accept a list of 10 elements of ‘X’ and ‘O’ called board."""
  print(f"""
     |   |
   {board[7]} | {board[8]} | {board[9]}
     |   |
  -----------
     |   |
   {board[4]} | {board[5]} | {board[6]}
     |   |
  -----------
     |   |
   {board[1]} | {board[2]} | {board[3]}
     |   |
  """)


def player_input(name):
  """function that take in a player input."""
  while True:
    player_input = int(
        input(
            f"Enter the position number between [1-9] for your move {name}: "))
    if 1 <= player_input <= 9:
      return player_input
    else:
      print(f"Enter a Valid move {name}")


def place_marker(board, marker, position):
  """function that takes in the board list object, a marker ('X' or 'O'), and a desired
  position (number 1-9) and assigns it to the board."""
  board[position] = marker


def win_check(board, mark):
  """function that takes in a board and a mark (X or O) and then
  checks to see if that mark has won. """
  return ((board[1] == board[2] == board[3] == mark)
          or (board[4] == board[5] == board[6] == mark)
          or (board[7] == board[8] == board[9] == mark)
          or (board[1] == board[4] == board[7] == mark)
          or (board[2] == board[5] == board[8] == mark)
          or (board[3] == board[6] == board[9] == mark)
          or (board[1] == board[5] == board[9] == mark)
          or (board[3] == board[5] == board[7] == mark))


def space_check(board, position):
  """function that returns a boolean indicating whether a space on the board is freely
    available."""
  return board[position] == ' '


def full_board_check(board):
  """function that checks if the board is full and returns a boolean value. True if full,
      False otherwise."""
  return ' ' not in board[1:]


def player_choice(board):
  """function that asks for a player's next position (as a number 1-9) and then uses the
function from step 6 to check if it's a free position. If it is, then return the position for later
use."""
  position = 0
  while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9
                         ] or not space_check(board, position):
    position = int(input("Choose your next position (1-9): "))
  return position


def replay():
  """function that asks the player if they want to play again and returns a boolean True
if they do want to play again."""
  return input("Do you want to play again? Enter 'yes' to play again: ").lower(
  ) == 'yes'


def main():
  while True:
    print("Welcome to Tic Tac Toe!")
    print(sample_board)
    the_board = [' '] * 10
    players = player_details()

    turn = choose_first()
    if turn == 0:
      player1_marker = 'X'
      player2_marker = 'O'
    else:
      player1_marker = 'O'
      player2_marker = 'X'
    play_game = input("Ready to play? Enter 'yes' or 'no': ").lower()
    print(f"{players[turn]} goes first.")

    if play_game == 'yes':
      game_on = True
    else:
      game_on = False

    while game_on:
      if turn == 0:
        display_board(the_board)
        position = player_input(players[turn])
        place_marker(the_board, player1_marker, position)

        if win_check(the_board, player1_marker):
          display_board(the_board)
          print("Congratulations!!!!!!!!!!!")
          print(f"{players[turn]} has won!")
          print()
          game_on = False
        else:
          if full_board_check(the_board):
            display_board(the_board)
            print("The game is a draw!")
            print()
            break
          else:
            turn = 1
      else:
        display_board(the_board)
        position = player_input(players[turn])
        place_marker(the_board, player2_marker, position)

        if win_check(the_board, player2_marker):
          display_board(the_board)
          print("Congratulations!!!!!!!!!!!")
          print(f"{players[turn]} has won!")
          print()
          game_on = False
        else:
          if full_board_check(the_board):
            display_board(the_board)
            print("The game is a draw!")
            print()
            break
          else:
            turn = 0

    if not replay():
      break


main()
print("\u00A9 2023-Manish-226301127")