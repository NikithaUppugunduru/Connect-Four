def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 29)


def is_valid_move(board, column):
    return board[0][column] == ' '


def drop_piece(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            break


def check_winner(board, player):
   
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    
    for row in range(3):
        for col in range(7):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

   
    for row in range(3, 6):
        for col in range(4):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def main():
    player_turn = 1
    board = create_board()

    while True:
        print_board(board)

        try:
            column = int(input(f"Player {player_turn}, choose a column (1-7): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= column <= 6 and is_valid_move(board, column):
            drop_piece(board, column, 'X' if player_turn == 1 else 'O')

            if check_winner(board, 'X' if player_turn == 1 else 'O'):
                print_board(board)
                print(f"Player {player_turn} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            player_turn = 3 - player_turn  # Switch player (1 -> 2, 2 -> 1)
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()
