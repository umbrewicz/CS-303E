from ControlGame import *

ERROR1 = "Value must be an even integer in the range [2..64]. Try again."

def playGame():
    """This is the driver for the ControlGame class.  It implements the
    game.  The board is 8x8 (64 'cells') and is initially empty.  There
    are two players designated 'Red' and 'Blue'.  Red plays first followed by Blue,
    and play alternates.  There are up to 64 turns.  In each turn, the
    next player places a token in any open cell.

    The goal is to control as much territory as possible.  A player
    controls a row if he has more tokens in the row than his opponent.
    He controls a column if he has more tokens in the column than his
    opponent.  He controls a cell, if he occupies a cell and at
    least two adjacent cells. Some cells have fewer than 4 neighbors.

    """

    # Print welcome message.
    print("Welcome to the Control Game!")

    # Get the number of turns to play.  Must be an even integer
    # between [2..64].  Accept inputs until one is legal. 
    while True:
        turnsStr = input("\nHow many turns to play (even integer <= 64): ").strip()
        if turnsStr.isdigit():
            turns = int(turnsStr)
            if turns % 2 == 0 and 2 <= turns <= 64:
                # If it's legal, break out of loop
                break
            else:
                # If it's not legal, try again.
                print(ERROR1)
                continue
        else:
            # If it's not a string containing only digits, try again.
            print(ERROR1)
            continue

    # Initialize the game with the number of turns to take 
    # indicated by the user. 
    game = ControlGame( turns )
    print( game )

    # Each round consists of 2 turns, one for Red and one for Blue.
    # We made sure that there's an even number of turns.
    for turn in range( turns ):
        player = game.getCurrentPlayer()
        # This previously had a ; instead of :.
        print( "Turn ", turn, ": ", player, "\'s turn to play.", sep="")

        # Keep at it until a legal turn is played.
        while True:
            # Accept coordinates from the user.
            rowStr, colStr = input("Enter row, col for player " + player + ": ").split(",")

            # First check whether the row, col values represent integers:
            if rowStr.strip().isdigit() and colStr.strip().isdigit():

                # If so, extract the integers from the strings:
                row, col = int(rowStr), int(colStr)

                # Method takeTurn does two things.  It updates the board
                # but only if the indicated move is legal.  It also returns 
                # a Boolean indicating whether the move was taken or not.
                if game.takeTurn( row, col ):
                    break
            else:
                print("You've entered an illegal move. Try again.")
                continue

        # Print the game board.
        print( game )
        # Print the current score.
        red, blue = game.getScore()
        print("\nThe current score is Red:", red, "Blue:", blue, "\n")

    # When all turns are completed, report who won, if anyone.
    print("\nYou've completed the game.\nFinal score: Red ", red, ", Blue ", blue, sep = "")
    if red > blue:
        print("Red wins!")
    elif red == blue:
        print("Red and Blue tied!")
    else:
        print("Blue wins!")

# Invoke this to actually play the game.
playGame()
