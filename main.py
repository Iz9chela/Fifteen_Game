import random

def print_board(game_board):
    for i in game_board:
        for j in i:
            print(j, end="  ")
        print()


def check_if_could_be_swapped():  # check if we could swap numbers
    pass


def swap_up():
    pass


def swap_down():
    pass


def swap_left():
    pass


def swap_right():
    pass


class Board:
    def __init__(self, size_of_board: int):
        self.size = size_of_board
        self.board = []
        self.small_Result_Board = [[1, 2, 3],
                                   [4, 5, 6],
                                   [7, 8, 0]]
        self.big_Result_Board = [[1, 2, 3, 4],
                                 [5, 6, 7, 8],
                                 [9, 10, 11, 12],
                                 [13, 14, 15, 0]]

    def __repr__(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=" ")
            print()

    def __str__(self):
        board_string = '-' * self.size * 6 + '\n'
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] < 10:
                    board_string += ' │ ' + str(self.board[i][j]) + " "
                else:
                    board_string += ' │ ' + str(self.board[i][j])
                if j == self.size - 1:
                    board_string += ' │\n'
        board_string += '-' * self.size * 6 + '\n'
        return board_string

    def refresh_board(self):
        print(self)
        if self.board == self.small_Result_Board or self.board == self.big_Result_Board:
            print("Board has been solved")
            return False
        return True

    def random_board_generation(self):
        arr = range(self.size * self.size)
        numbers = random.sample(arr, self.size * self.size)
        for row in range(self.size):
            self.board.append([])
            for column in range(self.size):
                self.board[row].append(numbers[row * self.size + column])
        return board


# ------------------------------------------------------------------Test-------------------------
if __name__ == '__main__':
    board = Board(4)
    board.random_board_generation()
    print(board)

    # print_board(big_Result_Board)

    # random_board_generation(4)
# ------------------------------------------------------------------Test-------------------------
