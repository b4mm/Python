def main():
    print("Welcome to my Tic Tac Toe game.")

    board = {
        1: "[ ]", 2: "[ ]", 3: "[ ]",
        4: "[ ]", 5: "[ ]", 6: "[ ]",
        7: "[ ]", 8: "[ ]", 9: "[ ]",
    }

    print("_______________________________")
    print("-----------" + board[1] + board[2] + board[3] + "-----------")
    print("-----------" + board[4] + board[5] + board[6] + "-----------")
    print("-----------" + board[7] + board[8] + board[9] + "-----------")
    print("_______________________________")

    while True:
        #Marks the start of Player 1's turn.
        player1_coordinate = player_turn(1)

        # Catches if the player picked a filled coordinate.
        while board[player1_coordinate] == "[0]" or board[player1_coordinate] == "[X]":
            print("Please enter an unused coordinate: ")
            player1_coordinate = player_turn(1)

        # Updates the Board.
        board[player1_coordinate] = "[X]"
        print("_______________________________")
        print("-----------" + board[1] + board[2] + board[3] + "-----------")
        print("-----------" + board[4] + board[5] + board[6] + "-----------")
        print("-----------" + board[7] + board[8] + board[9] + "-----------")
        print("_______________________________")

        row1, row2, row3 = rows(board)
        column1, column2, column3 = columns(board)
        diagnol1, diagnol2 = diagnols(board)

        # # Checks if player 1 met the win condition.
        win_condition = "[X]" * 3
        if (row1 == win_condition or row2 == win_condition or row3 == win_condition or
        column1 == win_condition or column2 == win_condition or column3 == win_condition
        or diagnol1 == win_condition or diagnol2 == win_condition):
            print("Player 1 Wins!!")
            break

        # Marks the start of Player 2's turn.
        player2_coordinate = player_turn(2)

        # Catches if the player picked a filled coordinate.
        while board[player2_coordinate] == "[0]" or board[player2_coordinate] == "[X]":
            print("Please enter an unused coordinate: ")
            player2_coordinate = player_turn(2)

        # Updates the Board.
        board[player2_coordinate] = "[0]"
        print("_______________________________")
        print("-----------" + board[1] + board[2] + board[3] + "-----------")
        print("-----------" + board[4] + board[5] + board[6] + "-----------")
        print("-----------" + board[7] + board[8] + board[9] + "-----------")
        print("_______________________________")

        row1, row2, row3 = rows(board)
        column1, column2, column3 = columns(board)
        diagnol1, diagnol2 = diagnols(board)

        # Checks if player 2 met the win condition.
        win_condition = "[0]" * 3
        if (row1 == win_condition or row2 == win_condition or row3 == win_condition or
                column1 == win_condition or column2 == win_condition or column3 == win_condition
                or diagnol1 == win_condition or diagnol2 == win_condition):
            print("Player 2 Wins!!")
            break

    print("Game Over.")


def player_turn(which_player):
    # The player must enter a coordinate from 1-9 to break out of the loop and return a value.
    while True:
        try:
            coordinate = int(input(f"Player {which_player} Enter a Coordinate: "))
            if 1 <= coordinate <= 9:
                return coordinate
            else:
                print("Coordinate must exist between 1-9. Try again. ")
        except:
            print("Please enter a coordinate from 1-9. ")


# Defines the rows for the Tic Tac Toe game.
def rows(board):
    row1 = board[1] + board[2] + board[3]
    row2 = board[4] + board[5] + board[6]
    row3 = board[7] + board[8] + board[9]
    return row1, row2, row3

# Defines the columns for the Tic Tac Toe game.
def columns(board):
    column1 = board[1] + board[4] + board[7]
    column2 = board[2] + board[5] + board[8]
    column3 = board[3] + board[6] + board[9]
    return column1, column2, column3

# Defines the diagnols for the Tic Tac Toe game.
def diagnols(board):
    diagnol1 = board[1] + board[5] + board[9]
    diagnol2 = board[3] + board[5] + board[7]
    return diagnol1, diagnol2

main()
