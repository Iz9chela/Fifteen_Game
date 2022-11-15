import random


def print_board(game_board):
    for i in game_board:
        for j in i:
            print(j, end="  ")
        print()


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
        self.small_Result_Board = [[1, 2, 3],
                                   [4, 5, 6],
                                   [7, 8, 0]]
        self.big_Result_Board = [[1, 2, 3, 4],
                                 [5, 6, 7, 8],
                                 [9, 10, 11, 12],
                                 [13, 14, 15, 0]]
        self.visited_field_hashes = set()
        self.backtrack_count = 0
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

    def process_new_field(self):
        hashedBoard = tuple(map(tuple, self.board))
        # print(hashedBoard)
        new_field_hash = hash(hashedBoard)  # get unique hash about our board
        if new_field_hash not in self.visited_field_hashes:
            return new_field_hash
        return None

    def update_field(self):
        self.refresh_field()
        new_field_hash = self.process_new_field()
        if new_field_hash is None:
            return False

        self.visited_field_hashes.add(new_field_hash)

        return True

    def refresh_field(self):
        print(self)
        if self.board == self.small_Result_Board or self.board == self.big_Result_Board:
            print("Board has been solved")
            return False
        return True

    def random_field_generation(self):
        self.board = []
        arr = range(self.size * self.size)
        numbers = random.sample(arr, self.size * self.size)
        for row in range(self.size):
            self.board.append([])
            for column in range(self.size):
                self.board[row].append(numbers[row * self.size + column])

    def get_all_possible_moves(self):
        moves = {}

        zero = found_zero_in_board(self.board)

        if zero[0] < self.size - 1:
            moves.update({"DOWN": self.swap_down()})  # move down

        if zero[0] > 0:
            moves.update({"UP": self.swap_up()})  # move up

        if zero[1] > 0:
            moves.update({"LEFT": self.swap_left()})  # move left

        if zero[1] < self.size - 1:
            moves.update({"RIGHT": self.swap_right()})  # move right

        return moves

    def swap(self, x, y):  # check if we could swap numbers

        zero = found_zero_in_board(self.board)
        # print("Positions of 0 in list >> ", zero)
        if (zero[0] + x < 0 or zero[0] + x > self.size - 1
                or zero[1] + y < 0 or zero[1] + y > self.size - 1):
            return False

        # print("After check")

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