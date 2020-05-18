import random

def TicTacToeGame():
    Player1Selections = []
    Player2Selections = []
    selected = []
    turnCounter = random.randint(1,2)
    Player1 = input("Player 1, do you want to be X or O? ").upper()
    if Player1 != 'X' and Player1.upper() != 'O':
        print("Please select either X or O")
        TicTacToeGame()
    if Player1 == 'X':
        Player2 = 'O'
    else:
        Player2 = 'X'
    board = ' 1 | 2 | 3 \n *********\n 4 | 5 | 6 \n *********\n 7 | 8 | 9 '
    print(board)

    def currentPlayer():
        if turnCounter %2 == 0:
            return Player1
        else:
            return Player2

    def player_input(Player1Selections, Player2Selections, selected):
        if currentPlayer() == 'X':
            while 1 == 1:
                selection = input('Player one, please choose a grid number: ')
                if selection in selected:
                    print("That has already been selected")
                elif selection not in ['1','2','3','4','5','6','7','8','9']:
                    print("Please select a valid grid number")
                else:
                    Player1Selections = Player1Selections.append(int(selection))
                    selected = selected.append(selection)
                    break
        else:
            while 1 == 1:
                selection = input('Player two, please choose a grid number: ')
                if selection in selected:
                    print("That has already been selected")
                elif selection not in ['1','2','3','4','5','6','7','8','9']:
                    print("Please select a valid grid number")
                else:
                    Player2Selections = Player2Selections.append(int(selection))
                    selected = selected.append(selection)
                    break
        return selection


    while 1 == 1:
        board = board.replace(player_input(Player1Selections, Player2Selections, selected), currentPlayer())
        print(board)
        turnCounter += 1
        if ((board[1] ==  board[5] ==  board[9] == Player1) or # across the top
        (board[24] ==  board[28] ==  board[32] == Player1) or # across the middle
        (board[47] ==  board[51] ==  board[55] == Player1) or # across the bottom
        (board[1] ==  board[24] ==  board[47] == Player1) or # down the left side
        (board[5] ==  board[28] ==  board[51] == Player1) or # down the middle
        (board[9] ==  board[32] ==  board[55] == Player1) or # down the right side
        (board[1] ==  board[28] ==  board[55] == Player1) or # diagonal
        (board[9] ==  board[28] ==  board[47] == Player1)):  # diagonal
            newGameCheck = input('Player one is the winner, would you like to play again? ')
            if newGameCheck.lower == 'yes':
                TicTacToeGame()
            else:
                print('Thanks for playing my Tic Tac Toe Game')
                break
        if ((board[1] ==  board[5] ==  board[9] == Player2) or # across the top
        (board[24] ==  board[28] ==  board[32] == Player2) or # across the middle
        (board[47] ==  board[51] ==  board[55] == Player2) or # across the bottom
        (board[1] ==  board[24] ==  board[47] == Player2) or # down the left side
        (board[5] ==  board[28] ==  board[51] == Player2) or # down the middle
        (board[9] ==  board[32] ==  board[55] == Player2) or # down the right side
        (board[1] ==  board[28] ==  board[55] == Player2) or # diagonal
        (board[9] ==  board[28] ==  board[47] == Player2)):  # diagonal
            newGameCheck = input('Player two is the winner, would you like to play again? ')
            if newGameCheck == 'yes':
                TicTacToeGame()
            else:
                print('Thanks for playing my Tic Tac Toe Game')
                break
        if (board[1] != '1' and board[5] != '2' and board[9] != '3' and board[24] != '4' and board[28] != '5' and board[32] != '6' and
            board[47] != '7' and board[51] != '8' and board[55] != '9'):
            newGameCheck = input('The game is a tie, would you like to play again? ')
            print(newGameCheck)
            if newGameCheck.lower == 'yes':
                TicTacToeGame()
            else:
                print('Thanks for playing my Tic Tac Toe Game')
                break


print(TicTacToeGame())
