from board import Board

small_Result_Board = ((1, 2, 3),
                      (4, 5, 6),
                      (7, 8, 0))
big_Result_Board = ((1, 2, 3, 4),
                    (5, 6, 7, 8),
                    (9, 10, 11, 12),
                    (13, 14, 15, 0))


def get_field_with_value(field):
    right_tiles_in_board = 0
    for i in range(len(field)):
        row = field[i]
        for j in range(len(row)):
            if field[i][j] == small_Result_Board[i][j]:
                right_tiles_in_board += 1
    return {field: right_tiles_in_board}


def is_correct(current_board):
    if current_board == small_Result_Board or current_board == big_Result_Board:
        return 1
    return 0


def solver(board: Board, board_solver: str):
    saved_fields: list[tuple[tuple[int]]] = [board.export_board()]
    explored_fields = set()

    if board_solver == "DFS":
        while saved_fields:
            current_field = saved_fields.pop()
            if current_field in explored_fields:
                continue
            explored_fields.add(current_field)
            if is_correct(current_field):
                print(f"Solution has been found with {len(explored_fields)} explored fields")
                return True

            board.import_board(current_field)
            # print(current_field)
            moves = board.get_all_possible_moves()
            for move in moves:
                move()
                new_field = board.export_board()
                saved_fields.append(new_field)
                board.import_board(current_field)
        print(f'Explored {len(explored_fields)} fields')
    elif board_solver == "GREEDY":
        while saved_fields:
            current_field = saved_fields.pop()
            if current_field in explored_fields:
                continue
            explored_fields.add(current_field)
            if is_correct(current_field):
                print(f"Solution has been found with {len(explored_fields)} explored fields")
                return True

            board.import_board(current_field)
            moves = board.get_all_possible_moves()
            possible_fields = {}
            for move in moves:
                move()
                new_field = board.export_board()
                new_field_with_value = get_field_with_value(new_field)
                possible_fields.update(new_field_with_value)
                saved_fields.append(new_field)
                board.import_board(current_field)
            sorted_possible_fields = dict(sorted(possible_fields.items(), key=lambda item: item[1]))
            for field in sorted_possible_fields:
                # print(field)
                saved_fields.append(field)
        print(f'Explored {len(explored_fields)} fields')


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
