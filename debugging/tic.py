#!/usr/bin/python3

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check all rows, columns, and diagonals for a winner."""
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0,1,2) for player {player}: "))
            col = int(input(f"Enter column (0,1,2) for player {player}: "))

            # Validate input range
            if row not in [0,1,2] or col not in [0,1,2]:
                print("Invalid position! Please enter 0, 1, or 2.")
                continue

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Check if spot is empty
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place move
        board[row][col] = player

        # Check winner BEFORE switching player
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Switch players
        player = "O" if player == "X" else "X"

        # Check for tie
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

tic_tac_toe()
