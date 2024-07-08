import math

# Constants
X = 'X'
O = 'O'
EMPTY = ' '

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if the board is full
def board_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to evaluate the current state of the board
def evaluate(board):
    if check_winner(board, X):
        return 1  # X wins
    elif check_winner(board, O):
        return -1  # O wins
    else:
        return 0  # Draw

# Minimax function with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    elif board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = X
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = O
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI using minimax with alpha-beta pruning
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = X
                eval = minimax(board, 0, alpha, beta, False)
                board[row][col] = EMPTY
                
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

# Main function to run the Tic-Tac-Toe game
def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    
    current_player = X
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while not board_full(board):
        if current_player == X:
            row, col = find_best_move(board)
            board[row][col] = X
            print(f"AI plays X at ({row}, {col})")
        else:
            valid_move = False
            while not valid_move:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if board[row][col] == EMPTY:
                        board[row][col] = O
                        valid_move = True
                    else:
                        print("That position is already taken. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number (0-2).")
        
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            return
        
        # Switch player
        current_player = O if current_player == X else X
    
    print("It's a draw!")

# Start the game
if __name__ == "__main__":
    play_game()

