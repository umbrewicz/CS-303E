# File: ControlGame.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
# 
# Date: 4/8/2022
# Description of Program: This program provides functions used in the Control Game.

MAX_TURNS = 64

class ControlGame:

    def __init__(self, turnsToPlay = MAX_TURNS):
        # This initializes the game with an empty board, the current
        # player set to 'Red' and the number of turns
        # specified by the user (defaults to 64).  turnsToPlay must
        # be an even number in the range [2..64].

        self.board = [[".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."]]
        self.currentPlayer = "Red"
        self.turns = turnsToPlay
        

    def __str__(self):
        # Permit displaying the header "Current board is:" following by the 
        # board.

        return "\nCurrent board is: \n  0 1 2 3 4 5 6 7\n0 " + " ".join(self.board[0]) + "\n1 " + " ".join(self.board[1]) + "\n2 " + " ".join(self.board[2]) + "\n3 " + " ".join(self.board[3])+ "\n4 " + " ".join(self.board[4])  + "\n5 " + " ".join(self.board[5]) + "\n6 " + " ".join(self.board[6]) + "\n7 " + " ".join(self.board[7])
                

    def getCurrentPlayer(self):
        # Return the current player, 'Red' or 'Blue'

        return self.currentPlayer

    def swapCurrentPlayer(self):
        # If the current player is 'Red', set it to 'Blue', and 
        # vice versa.

        if self.currentPlayer == "Red":
            self.currentPlayer = "Blue"
        elif self.currentPlayer == "Blue":
            self.currentPlayer = "Red"
    
    def getBoardState(self):
        # Return the current board.

        return self.board
    
    def takeTurn(self, row, col):
        # This attempts to add the current player's token to cell
        # (row, col).  Check whether the cell is legal and is not
        # occupied.  If the checks pass add the current player's
        # token to that cell.  Finally, return a Boolean value 
        # indicating whether or not the turn occurred.
        
        if row < 8 and col < 8:
            if self.board[row][col] == ".":
                if self.currentPlayer == "Red":
                    self.board[row][col] = "R"
                    self.swapCurrentPlayer()
                    return True
                elif self.currentPlayer == "Blue":
                    self.board[row][col] = "B"
                    self.swapCurrentPlayer()
                    return True
            else:
                print("Invalid turn. Cannot place piece on occupied cell.")
                return False
        else:
            print("Invalid turn. Location is out of bounds.")
            return False
    
    def getScore(self):
        # Calculate the sum of rows, columns, and cells controlled by
        # Red and Blue.  Return this as a pair (red, blue).  This is
        # the most complicated method, so it's probably a good idea 
        # to write subsidiary functions for this.

        red = 0
        blue = 0
        counter = 0

        # Calculate the sum of rows controlled by each player.

        rowWinner = []

        for row in self.board:
            for col in self.board:
                if row[counter] == "R":
                    red += 1
                elif row[counter] == "B":
                    blue += 1
                counter += 1
            if red > blue:
                rowWinner.append("R")
            elif blue > red:
                rowWinner.append("B")
            elif red == blue:
                rowWinner.append(".")
            red = 0
            blue = 0
            counter = 0

        # Calculate the sum of columns controlled by each player.

        colWinner = []

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[j][i] == "R":
                    red += 1
                elif self.board[j][i] == "B":
                    blue += 1
                counter += 1
            if red > blue:
                colWinner.append("R")
            elif blue > red:
                colWinner.append("B")
            elif red == blue:
                colWinner.append(".")
            red = 0
            blue = 0
            counter = 0

        # Calculate the sum of cells controlled by each player.

        redCells = 0
        blueCells = 0

        for row in range(len(self.board)):
            for col in range(len(self.board)):
                
                cell = self.board[row][col]
                
                '''
                self.board[row - 1][col] = cell above current cell
                self.board[row + 1][col] = cell bellow current cell
                self.board[row][col + 1] = cell to the right of current cell
                self.board[row][col - 1] = cell to the left of current cell
                '''
                
                # Cells in row 0
                
                if row == 0:
                    if col == 0:
                        
                        if cell == "R":
                            if self.board[row + 1][col] == "R" and self.board[row][col + 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row + 1][col] == "B" and self.board[row][col + 1] == "B":
                                blueCells += 1
                                
                    elif 0 < col < 7:
                        
                        if cell == "R":
                            if self.board[row + 1][col] == "R" and (self.board[row][col - 1] == "R" or self.board[row][col + 1] == "R"):
                                redCells += 1
                            elif self.board[row][col - 1] == "R" and self.board[row][col + 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row + 1][col] == "B" and (self.board[row][col - 1] == "B" or self.board[row][col + 1] == "B"):
                                blueCells += 1
                            elif self.board[row][col - 1] == "B" and self.board[row][col + 1] == "B":
                                blueCells += 1
                                
                    elif col == 7:
                        
                        if cell == "R":
                            if self.board[row + 1][col] == "R" and self.board[row][col - 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row + 1][col] == "B" and self.board[row][col - 1] == "B":
                                blueCells += 1
                                
                # Cells in rows 1 to 6
                
                elif 0 < row < 7:
                    if col == 0:
                        
                        if cell == "R":
                            if self.board[row + 1][col] == "R" and (self.board[row - 1][col] == "R" or self.board[row][col + 1] == "R"):
                                redCells += 1
                            elif self.board[row - 1][col] == "R" and self.board[row][col + 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row + 1][col] == "B" and (self.board[row - 1][col] == "B" or self.board[row][col + 1] == "B"):
                                blueCells += 1
                            elif self.board[row - 1][col] == "B" and self.board[row][col + 1] == "B":
                                blueCells += 1
                                
                    elif 0 < col < 7:
                    
                        if cell == "R":
                            if self.board[row + 1][col] == "R" and (self.board[row - 1][col] == "R" or self.board[row][col - 1] == "R" or self.board[row][col + 1] == "R"):
                                redCells += 1
                            elif self.board[row - 1][col] == "R" and (self.board[row][col - 1] == "R" or self.board[row][col + 1] == "R"):
                                redCells += 1
                            elif self.board[row][col - 1] == "R" and self.board[row][col + 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row + 1][col] == "B" and (self.board[row - 1][col] == "B" or self.board[row][col - 1] == "B" or self.board[row][col + 1] == "B"):
                                blueCells += 1
                            elif self.board[row - 1][col] == "B" and (self.board[row][col - 1] == "B" or self.board[row][col + 1] == "B"):
                                blueCells += 1
                            elif self.board[row][col - 1] == "B" and self.board[row][col + 1] == "B":
                                blueCells += 1
                                
                    elif col == 7:
                        
                        if cell == "R":
                            if self.board[row - 1][col] == "R" and (self.board[row + 1][col] == "R" or self.board[row][col - 1] == "R"):
                                redCells += 1
                            elif self.board[row + 1][col] == "R" and self.board[row][col - 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row - 1][col] == "B" and (self.board[row + 1][col] == "B" or self.board[row][col - 1] == "B"):
                                blueCells += 1
                            elif self.board[row + 1][col] == "B" and self.board[row][col - 1] == "B":
                                blueCells += 1

                # Cells in row 7
                
                elif row == 7:
                    if col == 0:
                        
                        if cell == "R":
                            if self.board[row - 1][col] == "R" and self.board[row][col + 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row - 1][col] == "B" and self.board[row][col + 1] == "B":
                                blueCells += 1

                    elif 0 < col < 7:
                        
                        if cell == "R":
                            if self.board[row - 1][col] == "R" and (self.board[row][col - 1] == "R" or self.board[row][col + 1] == "R"):
                                redCells += 1
                            elif self.board[row][col - 1] == "R" and self.board[row][col + 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row - 1][col] == "B " and (self.board[row][col - 1] == "B" or self.board[row][col + 1] == "B"):
                                blueCells += 1
                            elif self.board[row][col - 1] == "B" and self.board[row][col + 1] == "B":
                                blueCells += 1
                            
                    elif col == 7:
                        
                        if cell == "R":
                            if self.board[row - 1][col] == "R" and self.board[row][col - 1] == "R":
                                redCells += 1
                        elif cell == "B":
                            if self.board[row - 1][col] == "B" and self.board[row][col - 1] == "B":
                                blueCells += 1
               
        # Transcribe rowWinner, colWinner, and cellScore lists to returnable variables

        totalRed = redCells
        totalBlue = blueCells

        for i in range(len(rowWinner)):
            if rowWinner[i] == "R":
                totalRed += 1
            elif rowWinner[i] == "B":
                totalBlue += 1
            i += 1
                
        i = 0

        for i in range(len(colWinner)):
            if colWinner[i] == "R":
                totalRed += 1
            elif colWinner[i] == "B":
                totalBlue += 1
            i += 1
            
        return totalRed, totalBlue
