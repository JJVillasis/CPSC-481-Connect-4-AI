import numpy    #Create Multidimensional Array

class Connect4:

    #Class constructor for the game
    def __init__(s):
        s.ROWS = 6
        s.COLS = 7
        #Create empty board
        s.board = numpy.zeros((s.ROWS, s.COLS))
        #gameOver - Determines when a win condition is found
        s.gameOver = False
        #player1 - Determines when it is player 1's turn
        s.turn = 0

    #Check if the column in the board is filled
    def isValidLocation(s, col):
        return s.board[0][col] == 0

    #Given a column, find where the next open row is on the board
    def findRow(s, col):
        closestFilledRow = s.ROWS-1

        for x in range(0, s.ROWS):
            if s.board[x][col] != 0:
                closestFilledRow = x-1
                break

        return closestFilledRow

    #Place player token on given row and column
    def placeToken(s, row, col):
        s.board[row][col] = s.turn+1

    def printBoard(s):
        for x in range(s.ROWS):
            print(s.board[x])

        print()

    def game(s):
        #Loop until win condition is found
        while not s.gameOver:

            #Ask for player 1 input
            if s.turn == 0:
                while True:
                    s.printBoard()
                    sCol = int(input("Player 1's Turn (0-6): "))

                    #Check if chosen column is filled
                    if s.isValidLocation(sCol):
                        sRow = s.findRow(sCol)
                        break

                    else:
                        print("Column \'" + str(sCol) + "\' is Filled.\n")

                s.placeToken(sRow, sCol)


            #Ask for player 2 input
            else:
                while True:
                    s.printBoard()
                    sCol = int(input("Player 2's Turn (0-6): "))

                    #Check if chosen column is filled
                    if s.isValidLocation(sCol):
                        sRow = s.findRow(sCol)
                        break

                    else:
                        print("Column \'" + str(sCol) + "\' is Filled.\n")

                s.placeToken(sRow, sCol)

            s.turn += 1
            s.turn %= 2



test = Connect4()
test.game()
