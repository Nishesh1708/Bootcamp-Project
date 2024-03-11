import random
def display_board(board):
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+" "+board[9]+' ')
    print('-'*11)
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+" "+board[6]+' ')
    print('-'*11)
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+" "+board[3]+' ')
    return

def player_input():
    while True:
        player1=input('Player 1 choose X or O...')
        if player1=="X":
            player2='O'
            break
        elif player1=='O':
            player2='X'
            break
        else:
            print('INVALID input....Try again....')
    return player1,player2

def place_marker(board,marker,position):
    board[position]=marker
    return

def win_check(board,marker):
    if (board[7] == marker and board[8] == marker and board[9] == marker) or (board[4] == marker and board[5] == marker and board[6] == marker) or (board[1] == marker and board[2] == marker and board[3] == marker) or (board[7] == marker and board[4] == marker and board[1] == marker) or (board[8] == marker and board[5] == marker and board[2] == marker) or (board[9] == marker and board[6] == marker and board[3] == marker) or (board[7] == marker and board[5] == marker and board[3] == marker) or (board[9] == marker and board[5] == marker and board[1] == marker) :
        return True
    
    

def choose_player():
    x=random.randint(1,2)
    if x==1:
        print("Player 1 goes first.")
        return 1
    if x==2:
        print('Player 2 goes first.')
        return 2
    
def space_check(board,position):
    
        if board[position]==' ':
            return True
        else:
            return False
        
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i)==True:
            return False
    return True
        
def player_choice(board):
    next_position=int(input('Enter next position ='))
    if 0<next_position<10:
        if space_check(board,next_position)==True:
            return next_position
        else:
            print('Position already full....Choose another position...')
            player_choice(lst)
    else:
        print('INVALID range....Choose another....')
        player_choice(lst)
    

def replay():
    y=input('Do you wan to replay?....(Y/N)....')
    if y=='Y':
        return 'y'
    elif y=='N':
        print('THANKS FOR PLAYING....')
        return
    
print('Welcome to the TIC-TAC-TOE game...')
while True:
    lst=[' ']*10
    player1,player2=player_input()
    turn=choose_player()
    while True:
        if turn==1:
            display_board(lst)
            next_position=player_choice(lst)
            place_marker(lst,player1,next_position)

            if win_check(lst,player1)==True:
                display_board(lst)
                print('Congratulations!! Player 1 has won...')
                break
            else:
                if full_board_check(lst)==True:
                   print('Game is draw....')
                   break
                else:
                    turn=2

        else:
            display_board(lst)
            next_position=player_choice(lst)
            place_marker(lst,player2,next_position)

            if win_check(lst,player1)==True:
                display_board(lst)
                print('Congratulations!! Player 2 has won...')
                break
            else:
                if full_board_check(lst)==True:
                   print('Game is draw....')
                   break
                else:
                    turn=1

    if replay()!='y':
        break


