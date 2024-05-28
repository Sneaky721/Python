import random

player_number = 0
player_name = ""
player_symbol = ""
ai_symbol = ""
vs_ai = ""

player_move = 1 #by defult

game_board = [" "] * 9
game_winner = ""
winning_symbol = ""

player2_name = ""
player2_move = 2
player2_symbol = ""


def getUserInfo():
    global player_number, player_name, player_symbol, ai_symbol, vs_ai, player_move, is_player_first, vs_player, player2_move, player2_symbol, player2_name
    player_number += 1
    player_name = input("Enter your name ")
    opponent = input("Do you want to play vs Computer(C) or Player(P)? [C/P]").upper()
    if opponent == "P":
        print("%s You are designated as primary player" %player_name)
        player_symbol = input("Enter the symbol you want to play with [X/O] ").upper()
        if player_symbol == "X":
            player2_symbol = "O"
        else:
            player2_symbol = "X"
        player_move = input("Enter what move you want first(1) or second(2) [1/2] ")
        if player_move == 1:
            player2_move = 2
        else:
            player2_move = 1
        player2_name = input("Secondary user, please enter your name ")
    else:
        player_symbol = input("Enter the symbol you want to play with [X/O] ").upper()
        if player_symbol == "X":
            ai_symbol = "O"
        else:
            ai_symbol = "X"
        
        vs_ai = input("Enter what Ai you want to play against [W/S] (Weak, Strong) ").upper()
        player_move = input("Enter what move you want first(1) or second(2) [1/2] ")

def printLayoutBoard():
    global game_board
    game_board = [" "] * 9
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")
    print("")

def printBoard():
    global game_board
    print(" %s | %s | %s " % (game_board[0], game_board[1], game_board[2]))
    print("-----------")
    print(" %s | %s | %s " % (game_board[3], game_board[4], game_board[5]))
    print("-----------")
    print(" %s | %s | %s " % (game_board[6], game_board[7], game_board[8]))
    print("")


def getUserInput():
    global game_board, player_symbol
    while True:
        print("")
        user_move = input("Enter the number where you want to place your marker: ")
        # Check if the input is not empty, is a digit, and within the valid range
        if user_move and user_move.isdigit() and 0 <= int(user_move) < 9:
            if game_board[int(user_move)] == " ":
                game_board[int(user_move)] = player_symbol
                break
            else:
                print("Spot already taken.")
        else:
            print("Invalid input. Please enter a number between 0 and 8.")


def checkWin():
    global game_board
    # Define all possible winning combinations
    win_conditions = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]

    # Check each winning combination
    for condition in win_conditions:
        if game_board[condition[0]] == game_board[condition[1]] == game_board[condition[2]] != ' ':
            return True  # Found a winning combination

    return False  # No winning combination found
def is_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for x, y, z in win_conditions:
        if board[x] == board[y] == board[z] == symbol:
            return True
    return False

def is_draw(board):
    return " " not in board

def minimax(board, depth, is_maximizing):
    if is_win(board, ai_symbol):
        return 10
    elif is_win(board, player_symbol):
        return -10
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(len(board)):
            if board[i] == "":
                board[i] = ai_symbol
                score = minimax(board, depth + 1, False)
                board[i] = " "  # Undo the move
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = player_symbol
                    score = minimax(board, depth + 1, True)
                    board[i] = " "  # Undo the move
                    best_score = min(score, best_score)
            return best_score

        def find_best_move(board, symbol):
            best_score = -float('inf') if symbol == ai_symbol else float('inf')
            best_move = -1
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = symbol
                    score = minimax(board, 0, symbol == player_symbol)
                    board[i] = " "  # Undo the move
                    if (symbol == ai_symbol and score > best_score) or (symbol == player_symbol and score < best_score):
                        best_score = score
                        best_move = i
            return best_move

        def hardAi():
            best_move = find_best_move(game_board, ai_symbol)
            if best_move != -1:
                game_board[best_move] = ai_symbol
                print("AI places", ai_symbol, "in position", best_move)
                printBoard()

def getAiInput():
    global vs_ai
    if vs_ai == "W":
        easyAi()
    elif vs_ai == "S":
        hardAi()


def easyAi():
    global game_board, ai_symbol
    while True:
        ai_move = random.randint(0, 8)
        if game_board[ai_move] == " ":
            game_board[ai_move] = ai_symbol
            print("Weak Ai has move at: %s" % ai_move)
            return

def evaluate(board):
    if is_win(board, ai_symbol):
        return 10
    elif is_win(board, player_symbol):
        return -10
    else:
        return 0


def minimax(board, depth, is_maximizing):
    if is_win(board, ai_symbol):
        return 10
    elif is_win(board, player_symbol):
        return -10
    elif " " not in board:  # Draw
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = ai_symbol  # Make a move
                score = minimax(board, depth + 1, False)
                board[i] = " "  # Undo the move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = player_symbol
                score = minimax(board, depth + 1, True)
                board[i] = " "  # Undo the move
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(len(board)):
        if board[i] == " ":
            board[i] = ai_symbol
            score = minimax(board, 0, False)
            board[i] = " "  # Undo the move
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def hardAi():
    best_move = find_best_move(game_board)
    if best_move is not None:
        game_board[best_move] = ai_symbol
        print("AI places", ai_symbol, "in position", best_move)
    else:
        print("No moves left")

def getUser2Input():
    global game_board, player2_symbol
    while True:
        print("")
        user2_move = input("Player 2, Enter the number where you want to place your marker ")
        if user2_move >= "9":
            print("Invalid spot")
        elif game_board[int(user2_move)] == " ":
            game_board[int(user2_move)] = player2_symbol
            break
        else:
            print("Invalid spot")


def playAi():
    if player_move == "1":
        while True:
            getUserInput()
            printBoard()
            if checkWin():
                print("The Player %s has won the game" %player_name)
                game_winner = player_name
                winning_symbol = player_symbol
                break
            getAiInput()
            printBoard()
            if checkWin():
                print("The Ai has won")
                game_winner = vs_ai
                winning_symbol = ai_symbol
                break
            if " " not in game_board:
                print("The game ended in a draw")
                break
    else:
        while True:
            getAiInput()
            printBoard()
            if checkWin():
                print("The Ai has won")
                game_winner = vs_ai
                winning_symbol = ai_symbol
                break
            getUserInput()
            printBoard()
            if checkWin():
                print("The Player has won")
                game_winner = player_name
                winning_symbol = player_symbol
                break
            if " " not in game_board:
                print("The game ended in a draw")
                game_winner = "DRAW"
                winning_symbol = " "
                break



def playLocalHuman():
    if player_move == "1":
        while True:
            getUserInput()
            printBoard()
            if checkWin():
                print("%s has won" % player_name)
                game_winner = player_name
                winning_symbol = player_symbol
                break
            getUser2Input()
            printBoard()
            if checkWin():
                print("%s has won" % player2_name)
                game_winner = player2_name
                winning_symbol = player2_symbol
                break
            if " " not in game_board:
                print("The game ended in a draw")
                break
    else:
        while True:
            getUser2Input()
            printBoard()
            if checkWin():
                print("%s has won" % player2_name)
                game_winner = player2_name
                winning_symbol = player2_symbol
                break
            getUserInput()
            printBoard()
            if checkWin():
                print("%s has won" %player_name)
                game_winner = player_name
                winning_symbol = player_symbol
                break
            if " " not in game_board:
                print("The game ended in a draw")
                game_winner = "DRAW"
                winning_symbol = " "
                break


        

while True:
    getUserInfo()
    printLayoutBoard()
    
    if vs_ai == "":
        playLocalHuman()
    else:
        playAi()
    
    continue_playing = input("Do you want to play again [Y/N]").upper()
    if continue_playing == "Y":
        print("ANOTHER GAME IT IS!!!")
    else:
        break
