#-------Global VAriables--------


#game board
board = ["-","-","-","-","-","-","-","-","-",]

game_still_going = True

#Who won or tie
winner = None

#who's turn is it
current_player = "X"

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


 #if game is still going





#play a game of tic tac toe 
def play_game():

  # Dispay intial Board

  display_board()

  #while the game is still going
  while game_still_going:


   #handle  a single turn or an arbitrary player
   handle_turn(current_player)

   #Checks if the game is over
   check_if_game_over()

   #flip to other player
   flip_player()

   #The game has ended
  if winner == "X" or winner == "O":
    print(winner+" won.")
  elif winner == None:
    print("It's a tie")

  
  



def handle_turn(player):

  print(player+" 's turn")
  position = input("Choose a number between 1-9:")
  valid = False
  while not valid:

   while position not in ["1","2","3","4","5","6","7","8","9"]:
     position = input("Choose a position From  1-9:")
  
   position = int(position)- 1

   if board[position] == "-":
     valid = True
   else:
     print("You can't go there")

  board[position] = player
  display_board()

def check_if_game_over():
  check_if_win()
  check_if_tie()
  return



def check_if_win():
#setup global VAriables
 global winner


 #check rows
 row_winner = check_rows()

 #check columns
   
 columns_winner = check_columns()
  
 #check diagonals
 diagonal_winner = check_diagonal()

 if row_winner:
   winner = row_winner

 elif  columns_winner:
   winner = columns_winner

 elif diagonal_winner:
   winner = diagonal_winner

 else:
   winner = None
 return



def check_rows():
  #set up global variable 
  global game_still_going


  #check if any of the rows have the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3: 
   game_still_going = False
  
  #return the winner 

  if row_1:
    return board[0]

  elif row_2:
    return board[3]
  elif row_3:
    return board[6]

  return

def check_columns():
  global game_still_going


  #check if any of the columns  have the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3: 
   game_still_going = False
  
  #return the winner X or O 

  if column_1:
    return board[0]

  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return



def check_diagonal():
  global game_still_going


  #check if any of the diagonals have the same value (and is not empty)
  diagonal_1 = board[2] == board[4] == board[6] != "-"
  diagonal_2 = board[0] == board[4] == board[8] != "-"
  
  if diagonal_1 or diagonal_2 : 
   game_still_going = False
  
  #return the winner X or O

  if diagonal_1:
    return board[2]

  elif diagonal_2:
    return board[0]

    
  return


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  #global variable we need
  global current_player
  #if the current player was "X"  then change it to "O" 
  if current_player == "X":
    current_player = "O"
  #if the current player was "O" then change it to "X"
  elif current_player == "O":
    current_player = "X"
  return

play_game()
  
