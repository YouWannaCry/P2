def print_board(board):
    for i in range(0, 7, 3):
        print(board[i] + '|' + board[i+1] + '|' + board[i+2])
board = ['1.1','1.2','1.3',
         '2.1','2.2','2.3',
         '3.1','3.2','3.3']
print_board(board)
gameEnd = False
tx = True
while not gameEnd:
    try:
        position = int(input('Donde colocar la ficha? (1-9): '))
        board[position - 1] = 'x' if tx else 'o'
    except:
        print('Movimiento no valido')
    print_board(board)
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[1] == board[5] == board[9] or
        board[3] == board[5] == board[7]):
        print('El ganador es: ' + 'x') if tx else print('El ganador es: ' + 'o')
        gameEnd = True
    tx = not tx
