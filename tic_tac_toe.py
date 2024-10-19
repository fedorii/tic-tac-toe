def update_board(board, move, char):
    board = [[board[0][0], board[0][1], board[0][2]],
             [board[1][0], board[1][1], board[1][2]],
             [board[2][0], board[2][1], board[2][2]]]
    cells = {
        "7": "0 0", "8": "0 1", "9": "0 2",
        "4": "1 0", "5": "1 1", "6": "1 2",
        "1": "2 0", "2": "2 1", "3": "2 2",
    }
    if 1 <= move <= 9:
        row = int(cells[str(move)].split()[0])
        col = int(cells[str(move)].split()[1])
        if board[row][col] == ' ':
            board[row][col] = char
            return board    
        else:
            raise ValueError
    else:
        raise KeyError

def check_win(b):
    if b[0][0] == b[0][1] == b[0][2] and b[0][0] != ' ' or\
       b[1][0] == b[1][1] == b[1][2] and b[1][0] != ' ' or\
       b[2][0] == b[2][1] == b[2][2] and b[2][0] != ' ' or\
       b[0][0] == b[1][0] == b[2][0] and b[0][0] != ' ' or\
       b[0][1] == b[1][1] == b[2][1] and b[0][1] != ' ' or\
       b[0][2] == b[1][2] == b[2][2] and b[0][2] != ' ' or\
       b[0][0] == b[1][1] == b[2][2] and b[0][0] != ' ' or\
       b[0][2] == b[1][1] == b[2][0] and b[0][2] != ' ':
        return 1
    elif ' ' not in b[0] and ' ' not in b[1] and ' ' not in b[2]:
        return 2
    return 0

def display_board(board):
    a, b, c = board[0][0], board[0][1], board[0][2]
    d, e, f = board[1][0], board[1][1], board[1][2]
    g, h, i = board[2][0], board[2][1], board[2][2]

    board = f'''
            |       |        
        {a}   |   {b}   |   {c}
            |       |
    --------+-------+--------
            |       |        
        {d}   |   {e}   |   {f}
            |       |
    --------+-------+--------
            |       |       
        {g}   |   {h}   |   {i}
            |       |
    '''
    print(board)

def display_result(winner):
    if winner == 2:
        print("Draw!")
    elif winner == 1:
        print(char, " wins!")


board_cells = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
winner = False
char = "O" # You can replace to "X" if want to start with it

while not winner:
    try:
        char = "X" if char == "O" else "O"
        player_move = int(input(f"{char}, your turn: "))
        try:
            try:
                board_cells = update_board(board_cells, player_move, char)
                winner = check_win(board_cells)
            except ValueError:
                print('\nThis cell is already filled, choose another\n')
                char = "X" if char == "O" else "O"
            except KeyError:
                print('\nChoose a number from 1 to 9\n')
                char = "X" if char == "O" else "O"
        except ValueError:
            print('\nChoose cell from numpad\n')
    except ValueError:
        print('\nChoose cell from numpad\n')
        char = "X" if char == "O" else "O"
    except KeyboardInterrupt:
        print("\nYou stopped the game\n")
        break
    display_board(board_cells)

display_result(winner)