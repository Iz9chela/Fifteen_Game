from board import Board
from solver import dfs_solve, greedy_solve, a_star_solve

# ------------------------------------------------------------------Test-------------------------
if __name__ == '__main__':
    board_size = 3
    board = Board(board_size)
    # print(board.calculate_manhattan_distance())
    # board.random_field_generation()
    # print(board)
    # dfs_solve(board)
    # greedy_solve(board)
    a_star_solve(board)
# ------------------------------------------------------------------Test-------------------------
