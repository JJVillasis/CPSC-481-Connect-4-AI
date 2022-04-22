import numpy    #Create Multidimensional Array

class Connect4:

    #Class constructor for the game
    def __init__(s):
        #Board dimensions
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

    #Clean print of the board array
    def printBoard(s):
        for x in range(s.ROWS):
            print(s.board[x])
        print()

    #Check if the most recent move is a win condition - Horizontal Check
    def winCheckH(s, pRow, pCol):
        line = 1

        #Check right of the token
        for c in range (pCol+1, s.COLS):
            if s.board[pRow][c] == s.turn+1:
                line += 1
            else:
                break

        #Check left of the token
        for c in range(pCol-1, -1, -1):
            if s.board[pRow][c] == s.turn+1:
                line += 1
            else:
                break

        #Win condition found if 4-in-a-row or more
        if line >= 4:
            return True

    #Check if the most recent move is a win condition - Vertical Check
    def winCheckV(s, pRow, pCol):
        line = 0

        for r in range(pRow, s.ROWS):
            if s.board[r][pCol] == s.turn+1:
                line += 1
            else:
                break

        #Win condition found if 4-in-a-row or more
        if line >= 4:
            return True

    #Check if the most recent move is a win condition - Diagonal(/) Check
    def winCheckDF(s, pRow, pCol):
        line = 1

        #Top-right Check
        tCol = pCol+1
        for row in range(pRow-1, 0, -1):
            if tCol < 7 and s.board[row][tCol] == s.turn+1:
                line += 1
                tCol += 1
            else:
                break

        #Bottom-left check
        tCol = pCol-1
        for row in range(pRow+1, s.ROWS):
            if tCol >= 0 and s.board[row][tCol] == s.turn+1:
                line += 1
                tCol -= 1
            else:
                break

        #Win condition found if 4-in-a-row or more
        if line >= 4:
            return True

    #Check if the most recent move is a win condition - Diagonal(\) Check
    def winCheckDB(s, pRow, pCol):
        line = 1

        #Top-left check
        tCol = pCol-1
        for row in range(pRow-1, 0, -1):
            if tCol >= 0 and s.board[row][tCol] == s.turn+1:
                line += 1
                tCol -= 1
            else:
                break

        #Bottom-Right
        tCol = pCol+1
        for row in range(pRow+1, s.ROWS):
            if tCol < 7 and s.board[row][tCol] == s.turn+1:
                line += 1
                tCol += 1
            else:
                break

        #Win condition found if 4-in-a-row or more
        if line >= 4:
            return True

    #Check if the most recent move is a win condition
    def winCondition(s, pRow, pCol):
        #Check horizontally
        hori = s.winCheckH(pRow, pCol)

        #Check vertically
        vert = s.winCheckV(pRow, pCol)

        #Check diagonally
        diagF = s.winCheckDF(pRow, pCol)
        diagB = s.winCheckDB(pRow, pCol)

        return hori or vert or diagF or diagB


    def game(s):
        #Loop until win condition is found
        while not s.gameOver:

            #Ask for player 1 input
            if s.turn == 0:
                while True:
                    s.printBoard()
                    sCol = int(input("Player 1's Turn (0-6): "))
                    print()

                    #Check if chosen column is filled
                    if s.isValidLocation(sCol):
                        sRow = s.findRow(sCol)
                        break

                    #If Column is filled, choose another
                    else:
                        print("Column \'" + str(sCol) + "\' is Filled.\n")

                #Place Player 1's token
                s.placeToken(sRow, sCol)

            #Ask for player 2 input
            else:
                while True:
                    s.printBoard()
                    sCol = int(input("Player 2's Turn (0-6): "))
                    print()

                    #Check if chosen column is filled
                    if s.isValidLocation(sCol):
                        sRow = s.findRow(sCol)
                        break

                    #If Column is filled, choose another
                    else:
                        print("Column \'" + str(sCol) + "\' is Filled.\n")

                #Place Player 2's token
                s.placeToken(sRow, sCol)

            if s.winCondition(sRow, sCol):
                s.gameOver = True

            #Next Turn
            else:
                s.turn += 1
                s.turn %= 2

        #Game Over
        s.printBoard()
        print("Player " + str(s.turn+1) + " Wins! Game Over!\n")




test = Connect4()
test.game()
