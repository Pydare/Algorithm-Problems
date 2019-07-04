from IPython.display import clear_output
def display_board(board):
    print(' | | ')
    print('' + board[7] + '|' + board[8] + '|' + board[9])
    print(' | | ')
    print('------')
    print(' | | ')
    print('' + board[4] + '|' + board[5] + '|' + board[6])
    print(' | | ')
    print('------')
    print(' | | ')
    print('' + board[1] + '|' + board[2] + '|' + board[3])
    print(' | | ')

def player_input():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        if letter == 'X':
            return ['X','O']
        else:
            return ['O','X']

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    #this function returns true if the player has won
    return(board[7]==mark and board[8]==mark and board[9]==mark) 
    (board[4]==mark and board[5]==mark and board[6]==mark) 
    (board[1]==mark and board[2]==mark and board[3]==mark) 
    (board[1]==mark and board[4]==mark and board[7]==mark) 
    (board[8]==mark and board[2]==mark and board[5]==mark) 
    (board[9]==mark and board[6]==mark and board[3]==mark) 
    (board[7]==mark and board[5]==mark and board[3]==mark) 
    (board[1]==mark and board[5]==mark and board[9]==mark)

import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else: 
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

def full_board(board):
    for num in range(0,10):
        if space_check(board,num):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split()or not space_check(board,int(position)):
        print('Whats your next move? (1-9)')
        position = input()
        return int(position)

def replay():
    print('Do you want to play again?(Y or N)')
    return input().lower().startswith('y')

#time for main shit
print('WELCOME TO TICTACTOE')
while True:
    board = [' ']*10
    player_one_letter, player_two_letter = player_input() 
    turn = choose_first()
    print('The '+ turn + ' would go first')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player_one_letter,position)

            if win_check(board,player_one_letter):
                display_board(board)
                print('CONGRATS, PLAYER ONE!')
                gameIsPlaying = False
            else:
                if full_board(board):
                    display_board(board)
                    print('THE GAME IS A TIE')
                    break
                else:
                    turn = 'Player 2'
        else:
            position = player_choice(board)
            place_marker(board,player_two_letter,position)

            if win_check(board,player_two_letter):
                display_board(board)
                print('CONGRATS, PLAYER TWO!')
                gameIsPlaying = false
            else:
                if full_board(board):
                    display_board(board)
                    print('THE GAME IS A TIE')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
        
         
        


