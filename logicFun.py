import random

    # Logical Functions..

def drawBoard(board):
    # draw the board that it was passed..(list of strings)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '\n---*---*---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '\n---*---*---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def getBoardCopy(board):
    # Make copy of the board list..
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)

    return dupeBoard

    #**********
def playAgain():        #Provide option to play again...
    print('\n \n********Do you want to play again?********\n')
    print("[1]: to play again?..\n"
          "[2]: to back in Beginning list...")
    x = int(input("\nEnter number of the above to going>>> "))
    while not (x == 1 or x == 2):
        x = int(input("Enter number of the above to going>>> "))
    if x == 1:
        welcomePro()
    elif x == 2:
        welcomePro()

def whoGoesFirst_Computer():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def whoGoesFirst_User():
    #choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def inputPlayerLetter():
    # Returns list with the player’s letter as the first item, and the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


    # **********
def isSpaceFree(board, move):       # Return true if free on board.
    return board[move] == ' '

def isBoardFull(board):            # Return True if every space on the board has been taken.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def isWinner(bo, le):               #check if one win
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))    # diagonal


    # **********

def makeMove(board, letter, move):
    board[move] = letter

def getPlayerMove(board,trun):
    # return Move number...the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print(f'trun {trun}: "What is your next move? (1-9)"')
        move = input()
    return int(move)

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

    #**********

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

        # **********
        # **********

        ## Initialization Functions
def welcomePro():
    print("******Welcome in Tic-Tac-Toe-console-game..******")
    print("[1]: to Start Game with Computer... \n"
          "[2]: to Start Game with user player...\n"
          "[3]: to Help or Learn 'How to Game?'..\n"
          "[4]: to cancel the Game.. ")
    ch=0
    while not (ch == 1 or ch == 2 or ch == 3):
        ch = int(input("Enter number of the above to going>>> "))
        if ch == 1:
            StartGameWithComputer()
        elif ch == 2:
            StartGameUsers()
        elif ch == 3:
            rf = open("helps.txt", 'r')
            data = rf.read()
            print(data)
            rf.close()
            y=int(input('Enter 1 , to back..'))
            if y == 1:
                welcomePro()

        elif ch == 4:
            exit()


def StartGameWithComputer():
    while True:
        theBoard = [' '] * 10  # Reset the board
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst_Computer()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':  # Player’s turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard,"player")
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is over !')
                        break
                    else:
                        turn = 'computer'


            else:  # Computer’s turn.
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

        if not playAgain():
            break


def StartGameUsers():
    while True:
        theBoard = [' '] * 10  # Reset the board
        player1Letter, player2Letter = inputPlayerLetter()
        turn = whoGoesFirst_User()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player1':  # Player1’s turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard,turn)
                makeMove(theBoard, player1Letter, move)

                if isWinner(theBoard, player1Letter):
                    drawBoard(theBoard)
                    print('Hooray! player1 have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player2'


            else:  # player2’s turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard,turn)
                makeMove(theBoard, player2Letter, move)

                if isWinner(theBoard, player2Letter):
                    drawBoard(theBoard)
                    print('Hooray! player2 have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player1'

        if not playAgain():
            break



