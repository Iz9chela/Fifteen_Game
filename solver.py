from board import Board
import time

small_Result_Board = ((1, 2, 3),
                      (4, 5, 6),
                      (7, 8, 0))
big_Result_Board = ((1, 2, 3, 4),
                    (5, 6, 7, 8),
                    (9, 10, 11, 12),
                    (13, 14, 15, 0))


def get_field_with_value(board: Board):
    right_tiles_in_board = 0
    # for i in range(len(field)):
    #     row = field[i]
    #     for j in range(len(row)):
    #         if len(field) == 3:
    #             if field[i][j] == small_Result_Board[i][j]:
    #                 right_tiles_in_board += 1
    #         else:
    #             if field[i][j] == big_Result_Board[i][j]:
    #                 right_tiles_in_board += 1
    # return {field: right_tiles_in_board}
    return board.export_board(), board.calculate_manhattan_distance()


def is_correct(current_board):
    if current_board == small_Result_Board or current_board == big_Result_Board:
        return 1
    return 0


def solver(board: Board, board_solver: str):
    min_score = 100
    start_time = time.time()
    if board.size == 3:
        saved_fields: list[tuple[tuple[int]]] = [board.export_board()]
        explored_fields = set()
        sorted_saved_fields: list[tuple[tuple[tuple[int]], int]] = [
            (board.export_board(), board.calculate_manhattan_distance())]
        explored_saved_fields: set[tuple[tuple[tuple[int]], int]] = set()
    else:
        saved_fields: list[tuple[tuple[tuple[int]]]] = [board.export_board()]
        explored_fields = set()
        sorted_saved_fields: list[tuple[tuple[tuple[tuple[int]]], int]] = [
            (board.export_board(), board.calculate_manhattan_distance())]
        explored_saved_fields: set[tuple[tuple[tuple[tuple[int]]], int]] = set()

    if board_solver == "DFS":
        while saved_fields:
            current_field = saved_fields.pop()
            if current_field in explored_fields:
                continue
            explored_fields.add(current_field)
            board.import_board(current_field)
            # board.render_board()
            if is_correct(current_field):
                print(f"Solution has been found with {len(explored_fields)} explored fields")
                board.result_time(round(time.time() - start_time, 2))
                print(round(time.time() - start_time, 2))
                return True
            moves = board.get_all_possible_moves()
            for move in moves:
                move()
                # board.render_board()
                new_field = board.export_board()
                saved_fields.append(new_field)
                board.import_board(current_field)
    elif board_solver == "GREEDY":
        while saved_fields:
            current_field = saved_fields.pop()
            if current_field in explored_fields:
                continue
            explored_fields.add(current_field)
            board.import_board(current_field)
            board.render_board()
            if is_correct(current_field):
                print(f"Solution has been found with {len(explored_fields)} explored fields")
                board.result_time(round(time.time() - start_time, 2))
                # print(round(time.time() - start_time, 2))
                return True

            moves = board.get_all_possible_moves()
            possible_fields = {}
            for move in moves:
                move()
                board.render_board()
                new_possible_field, new_field_value = get_field_with_value(board)
                possible_fields.update({new_possible_field: new_field_value})
                saved_fields.append(new_possible_field)
                board.import_board(current_field)
            sorted_possible_fields = dict(sorted(possible_fields.items(), key=lambda item: item[1], reverse=True))
            for field in sorted_possible_fields:
                saved_fields.append(field)
    elif board_solver == "A_STAR":
        while saved_fields:
            current_field = sorted_saved_fields[0][0]
            current_field_score = sorted_saved_fields[0][1]
            board.import_board(current_field)
            board.render_board()
            if is_correct(current_field):
                print(f"Solution has been found with {len(explored_saved_fields)} explored fields")
                board.result_time(round(time.time() - start_time, 2))
                # print(round(time.time() - start_time, 2))
                return True
            moves = board.get_all_possible_moves()
            possible_manhattan_moves = {}
            for move in moves:
                move()
                board.render_board()
                new_field = board.export_board()
                new_field_score = board.calculate_manhattan_distance()
                possible_manhattan_moves.update({new_field: new_field_score})
                board.import_board(current_field)
            sorted_possible_manhattan_moves = \
                dict(sorted(possible_manhattan_moves.items(), key=lambda item: item[1], reverse=False))
            min_field = min(sorted_possible_manhattan_moves.items(), key=lambda value: value[1])
            if min_field[1] < min_score and min_field not in explored_saved_fields:
                min_score = min_field[1]
                sorted_saved_fields.append(min_field)
            for field in sorted_possible_manhattan_moves.items():
                if field not in explored_saved_fields and field not in sorted_saved_fields:
                    sorted_saved_fields.append(field)
            explored_saved_fields.add((current_field, current_field_score))
            del sorted_saved_fields[0]
            sorted_saved_fields.sort(key=lambda a: a[1])


def dfs_solve(board: Board):
    print('Solving with DFS')
    board.solved = solver(board, "DFS")
    if board.solved:
        print('SUCCESS')
    else:
        print("Unable to solve such board with DFS")


def greedy_solve(board: Board):
    print('Solving with GREEDY')
    board.solved = solver(board, "GREEDY")
    if board.solved:
        print('SUCCESS')
    else:
        print("Unable to solve such board with GREEDY")


def a_star_solve(board: Board):
    print('Solving with A_STAR')
    board.solved = solver(board, "A_STAR")
    if board.solved:
        print('SUCCESS')
    else:
        print("Unable to solve such board with A_STAR")
