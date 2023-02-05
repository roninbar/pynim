Player = int
Board = list[int]


def opponent(player: int) -> int:
    match player:
        case 1:
            return 2
        case 2:
            return 1
        case _:
            raise ValueError(f'Expected 1 or 2; got {player}.')


def initial() -> Board:
    return [5, 4, 3, 2, 1]


def finished(board: Board) -> bool:
    return all(row == 0 for row in board)


def valid(board: Board, row: int, how_many: int) -> bool:
    return row in range(1, 6) and 0 < how_many <= board[row - 1]


def move(board: Board, row: int, how_many: int) -> Board:
    board[row - 1] -= how_many
    return board


def putRow(row: int, num: int):
    stars = ' '.join(['*'] * num)
    print(f'{row} : {stars}')


def putBoard(board: Board):
    for row, num in enumerate(board, 1):
        putRow(row, num)


def getDigit(prompt: str) -> int:
    s = input(prompt)
    if s.isdigit():
        return int(s)
    else:
        print(f'ERROR: Invalid digit "{s}".')
        return getDigit(prompt)


def play(board: Board, player: Player):
    # putBoard(board)
    if finished(board):
        print(f'Player {opponent(player)} wins!')
    else:
        print(f'Player {player}, enter your move:')
        row = getDigit('Row? ')
        how_many = getDigit('How many? ')
        if valid(board, row, how_many):
            nextBoard = move(board, row, how_many)
            putBoard(nextBoard)
            play(board=nextBoard, player=opponent(player))
        else:
            print('ERROR: Invalid move.')
            play(board, player)


if __name__ == '__main__':
    board = initial()
    putBoard(board)
    play(board, 1)
