from board import Board
from sys import setrecursionlimit

setrecursionlimit(100000)
limit = 100000
small_Result_Board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0]]
big_Result_Board = [[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 0]]

moves = [None] * limit
best_moves = [None] * limit
best_depth = limit


def isCorrect(currentboard: Board):
    if currentboard.board == small_Result_Board or currentboard.board == big_Result_Board:
        return 1
    return 0


def dfs(board: Board):
    if board.backtrack_count >= limit:
        return False

    if isCorrect(board):
        print(f"Solution has been found with {board.backtrack_count} steps")
        return True

    if board.swap_down():
        board.swap_down()
        make_branch(board, dfs)
        board.backtrack_count += 1
        board.swap_up()
    if board.swap_up():
        board.swap_up()
        make_branch(board, dfs)
        board.backtrack_count += 1
        board.swap_down()
    if board.swap_left():
        board.swap_left()
        make_branch(board, dfs)
        board.backtrack_count += 1
        board.swap_right()
    if board.swap_right():
        board.swap_right()
        make_branch(board, dfs)
        board.backtrack_count += 1
        board.swap_left()


def make_branch(board: Board, func):
    is_new_field = board.update_field()  # update whole field
    if is_new_field:
        if board.board == board.small_Result_Board or board.board == board.big_Result_Board:
            return True
        return func(board)
    else:
        return False


def dfs_solve(board: Board):
    print('Solving with DFS')
    board.solved = dfs(board)
    if board.solved:
        print('SUCCESS')
        print(f'Solve ended in {board.backtrack_count} backtracks')
    else:
        print("Unable to solve such board with DFS")
