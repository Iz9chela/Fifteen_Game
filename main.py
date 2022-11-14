from board import Board
from solver import dfs_solve

# ------------------------------------------------------------------Test-------------------------
if __name__ == '__main__':
    board_size = 3
    board = Board(board_size)
    dfs_solve(board)
    # -----------------------------
    # board.random_field_generation()
    # print(board)
    # board.swap_down()
    # print(board)
    # board.swap_left()
    # print(board)
    # board.swap_down()
    # print(board)
    # board.swap_right()
    # print(board)
# ------------------------------------------------------------------Test-------------------------
