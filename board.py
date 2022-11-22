import random


def found_zero_in_board(board):
    index = []
    for i in board:
        for j in i:
            if j == 0:
                index.append(board.index(i))
                index.append(i.index(j))
    return index


class Board:
    def __init__(self, size_of_board: int):
        self.size = size_of_board
        self.board = [[3, 8, 5],
                      [0, 4, 2],
                      [1, 6, 7]]
        self.solved = False

    def __repr__(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=" ")
            print()

    def __str__(self):
        board_string = ""
        for i in range(self.size):
            board_string += '-' * self.size * 6 + '\n'
            for j in range(self.size):
                if self.board[i][j] < 10:
                    board_string += ' │ ' + str(self.board[i][j]) + " "
                else:
                    board_string += ' │ ' + str(self.board[i][j])
                if j == self.size - 1:
                    board_string += ' │\n'
        board_string += '-' * self.size * 6 + '\n'
        return board_string

    def random_field_generation(self):
        self.board = []
        arr = range(self.size * self.size)
        numbers = random.sample(arr, self.size * self.size)
        for row in range(self.size):
            self.board.append([])
            for column in range(self.size):
                self.board[row].append(numbers[row * self.size + column])

    def get_all_possible_moves(self):
        moves = []

        zero = found_zero_in_board(self.board)

        if zero[0] < self.size - 1:
            moves.append(self.swap_down)

        if zero[0] > 0:
            moves.append(self.swap_up)

        if zero[1] > 0:
            moves.append(self.swap_left)

        if zero[1] < self.size - 1:
            moves.append(self.swap_right)

        return moves

    def swap(self, x, y):

        zero = found_zero_in_board(self.board)

        if (zero[0] + x < 0 or zero[0] + x > self.size - 1
                or zero[1] + y < 0 or zero[1] + y > self.size - 1):
            return False

        self.board[zero[0]][zero[1]], self.board[zero[0] + x][zero[1] + y] = \
            self.board[zero[0] + x][zero[1] + y], self.board[zero[0]][zero[1]]

        return True

    def swap_up(self):
        return self.swap(-1, 0)

    def swap_down(self):
        return self.swap(1, 0)

    def swap_left(self):
        return self.swap(0, -1)

    def swap_right(self):
        return self.swap(0, 1)

    def import_board(self, board_save):
        imported_board = []
        for row in board_save:
            imported_board.append(list(row))
        self.board = imported_board

    def export_board(self) -> tuple[tuple[int]]:
        rows_as_tuples = []
        for row in self.board:
            rows_as_tuples.append(tuple(row))
        return tuple(rows_as_tuples)
