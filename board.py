import copy
import random
import math

import pygame

pygame.font.init()

result_small_board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0]]

big_Result_Board = [[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 0]]


# unsolvable_board_3x3 = list([[5, 8, 1], [3, 7, 0], [2, 6, 4]])
# unsolvable_board_4x4 = list([[13, 1, 5,14], [8, 9, 12,3], [15, 7, 4,2], [6,10,0,11]])

# solvable_boards_3x3 = list([[5,4,7], [1,3,6], [8,2,0]],
#                            [[6,4,2], [5,3,7], [0,8,1]],
#                            [[8,6,7],[2,5,4],[3,0,1]],
#                            [[4,5,0],[8,1,3],[2,6,7]],
#                            [[7,6,4],[8,3,1],[2,0,5]],
#                            [[0,6,2],[8,1,4],[3,5,7]],
#                            [[6,7,8],[5,3,4],[2,5,1]],
#                            [[8,1,4],[2,0,7],[6,3,5]])

# solvable_boards_4x4 = list([[12, 3, 15, 11], [14, 9, 1, 7], [10, 13, 4, 5], [0, 6, 2, 8]],
#                            [[14, 13, 5, 15], [10, 9, 6, 2], [4, 12, 3, 11], [8, 7, 1, 0]],
#                            [[11, 9, 4, 5],[14, 0, 13, 12],[7, 1, 8, 2],[3, 6, 15, 10]],
#                            [[9, 8, 12, 1],[5, 7, 13, 0],[2, 10, 14, 3],[11, 15, 4, 6]],
#                            [[13, 6, 12, 2],[5, 0, 10, 1],[9, 11, 8, 15],[14, 7, 4, 3]],
#                            [[3, 10, 14, 11],[6, 13, 0, 1],[15, 12, 8, 2],[7, 5, 9, 4]],
#                            [[4, 6, 8, 5],[9, 12, 15, 0],[14, 10, 2, 7],[1, 11, 3, 13]],
#                            [[11, 1, 10, 15],[7, 0, 5, 9],[8, 2, 14, 3],[13, 6, 12, 4]])


def find_number_in_board(board, number=0):
    index = []
    for i in board:
        for j in i:
            if j == number:
                index.append(board.index(i))
                index.append(i.index(j))
    return index


class Board:
    def __init__(self, size_of_board: int, screen, buttons):
        self.size = size_of_board
        self.board = []
        # self.board = [[4, 5, 0], [8, 1, 3], [2, 6, 7]]
        self.board = [[12, 3, 15, 11], [14, 9, 1, 7], [10, 13, 4, 5], [0, 6, 2, 8]]
        self.copied_board = copy.deepcopy(self.board)
        self.buttons = buttons
        self.solved = False
        self.font = pygame.font.Font(None, 100)
        self.screen = screen
        self.solve_running = False
        self.time = 0
        self.is_board_solvable = False

        for button in self.buttons:
            button.assing_board(self)
        if len(self.board) <= 0:
            self.random_field_generation()
            self.is_solvable()
        else:
            self.is_solvable()




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

        self.copied_board = self.board
        self.is_solvable()

    def render_board(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                x = j * (100 + 5) + 5
                y = i * (100 + 5) + 5
                pygame.draw.rect(self.screen, (0, 255, 0), (x, y, 100, 100))
                text = self.font.render(str(self.board[i][j]), True, (0, 0, 0))
                self.screen.blit(text, (x, y))

        for button in self.buttons:
            button.render(self.screen)

        txt = 'Yes' if self.is_board_solvable else 'No'
        solvable_x, solvable_y = 5, 430
        pygame.draw.rect(self.screen, (27, 27, 179), (solvable_x, solvable_y, 430, 100))
        text = self.font.render(str(f"Solvable:{txt}"), True, (0, 0, 0))
        self.screen.blit(text, (solvable_x, solvable_y))

        time_x, time_y = 5, 510
        pygame.draw.rect(self.screen, (27, 27, 179), (time_x, time_y, 430, 100))
        text = self.font.render(str(f"Time: {self.time}"), True, (0, 0, 0))
        self.screen.blit(text, (time_x, time_y))

        pygame.display.flip()
        pygame.time.delay(0)
        pygame.event.pump()

    def get_all_possible_moves(self):
        moves = []

        zero = find_number_in_board(self.board)

        if zero[0] < self.size - 1:
            moves.append(self.swap_down)

        if zero[0] > 0:
            moves.append(self.swap_up)

        if zero[1] > 0:
            moves.append(self.swap_left)

        if zero[1] < self.size - 1:
            moves.append(self.swap_right)

        return moves

    def calculate_manhattan_distance(self):
        sum_manhattan_distance = 0
        for i in range(self.size):
            for j in range(self.size):
                value = self.board[i][j]
                if value == 0:
                    continue
                i_value = i
                j_value = j

                if self.size == 3:
                    i_goal_value, j_goal_value = find_number_in_board(result_small_board, value)
                else:
                    i_goal_value, j_goal_value = find_number_in_board(big_Result_Board, value)

                sum_manhattan_distance += (math.fabs(i_goal_value - i_value) + math.fabs(j_goal_value - j_value))
        return sum_manhattan_distance

    def swap(self, x, y):

        zero = find_number_in_board(self.board)

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

    def reset_board(self):
        self.board = self.copied_board
        self.time = 0

    def result_time(self, value):
        self.time = value

    def get_inv_count(self, arr):
        inv_count = 0
        empty_value = 0
        for i in range(0, self.size * self.size):
            for j in range(i + 1, self.size * self.size):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    def is_solvable(self):
        inv_count = self.get_inv_count([j for sub in self.board for j in sub])
        self.is_board_solvable = inv_count % 2 == 0
        return self.is_board_solvable
