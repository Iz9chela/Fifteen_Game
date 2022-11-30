# a = [[3, 2], [0, 9, 4]]
#
#
# def found_zero_in_board(item, board):
#     index = []
#     for i in board:
#         for j in i:
#             if j == item:
#                 index.append(board.index(i))
#                 index.append(i.index(j))
#     return index
#
#
# print(found_zero_in_board(0, a))

# board1 = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 0]]
#
# board2 = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 0]]
#
# board_min_solve = [[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 0]]
#
# board_max_solve = [[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 0]]
# #
# print(board1 == board_min_solve)
#
# print(board2 == board_max_solve)

# user_says = input("Please enter the string > ")
# print(user_says)

# words = "Hello, \"test\" 'world'!"
# print(words)

# s = r'C:\d\new.txt'
# print(s)

# name = 'John'
# age = 15
# print(f'My name is {name} and my age is {age}')

# s = 'Hello World'
# for l in s:
#     print(f"{l}", end=' ')

# year = 2002
#
# while year <= 2022:
#     print(year)
#     year += 1
# else:
#     print("Done!")

# l = [1, 2, 3, 'Hi', ['test1', 1], 'world', True]
# l2 = list('hello')
# l3 = list((1, 2, 3))
# l5 = [i for i in 'Hello world' if i not in ['a', 'e', 'o', ' ']]
# print(l, l2, l3, l5, sep='\n')
#
# l6 = list(range(1, 16))
# print(l6)
#
# for i in range(1, 3):
#     print(f'cycle #{i}')
#     for j in range(1, 3):
#         print(f'Inside cycle #{j}')

# l = [1, 2, 3, 'Hi', ['test1', 1], 'world', True]
# print(l[4][0])
# l.append('new')
# l2 = ['hi', 19]
# l.extend(l2)
# print(l)

# t1 = tuple((1, 2, 3))
# print(t1)

# nums = {1, 2, 3, 4, 5, 6, 7, 7, 5, 3, 2, 6}
# nums2 = set(nums)
# print(nums2)

# set() - mutable type
# frozenset() - unmutable type

# product1 = {'title': 'Sony',
#             'price': 100,
#             }

# A* test
# sorted_saved_fields: list[tuple[tuple[tuple[int]], int]] = [
#         (board.export_board(), get_f_score(board.export_board(), g_score))]
#     astarset_explored_fields: set[tuple[tuple[tuple[int]], int]] = set()
# while saved_fields:
#     current_field = sorted_saved_fields.pop()[0]
#     if current_field in astarset_explored_fields:
#         continue
#     astarset_explored_fields.add(current_field)
#     if is_correct(current_field):
#         print(f"Solution has been found with {len(explored_fields)} explored fields")
#         return True
#
#     board.import_board(current_field)
#     moves = board.get_all_possible_moves()
#     for move in moves:
#         move()
#         new_field = board.export_board()
#         if new_field not in explored_fields:
#             sorted_saved_fields.append((new_field, get_f_score(new_field, g_score + 1)))
#         else:
#             explored_fields
#         board.import_board(current_field)
#     g_score += 1
#     sorted_saved_fields.sort(key=lambda x: x[1], reverse=True)
# A* test

# saved_fields = []
#
# abc = {333: 1, 444: 2, 555: 3, 666: 4, 777: 0}
# sorted_possible_fields = dict(sorted(abc.items(), key=lambda item: item[1]))
# print(sorted_possible_fields)
# for field in sorted_possible_fields:
#     saved_fields.append(field)
#
# print(saved_fields)


# A* test2
# while open_fields:
#     tuple_field = open_fields[0]
#     if tuple_field in closed_fields_sets:
#         continue
#     current_field = open_fields[0][0]
#     if is_correct(current_field):
#         print(f"Solution has been found with {len(closed_fields)} explored fields")
#         return True
#     board.import_board(current_field)
#     # print(current_field)
#     moves = board.get_all_possible_moves()
#     unsorted_possible_fields = {}
#     for move in moves:
#         move()
#         new_tuple_field = (board.export_board(), get_f_score(board.export_board(), g_score + 1))
#         if new_tuple_field[0] in open_fields[0][0]:
#             field_before_value = [x[0][1] for x in open_fields[0] if x[0][1] == new_tuple_field[1]]
#             if new_tuple_field[1] < field_before_value[0]:
#                 result = [
#                     idx for idx, tup in enumerate(open_fields) if tup[0] == new_tuple_field[0]
#                 ]
#                 del open_fields[result[0]]
#                 unsorted_possible_fields.update({new_tuple_field: new_tuple_field[1]})
#                 # open_fields.insert(result[0], new_tuple_field)
#         else:
#             unsorted_possible_fields.update({new_tuple_field: new_tuple_field[1]})
#             # open_fields.append(new_tuple_field)
#         board.import_board(current_field)
#     sorted_possible_fields = dict(sorted(unsorted_possible_fields.items(), key=lambda kv: kv[1]))
#     closed_fields.append(tuple_field)
#     closed_fields_sets.update(tuple_field)
#     g_score += 1
#     for field in sorted_possible_fields:
#         open_fields.append(field)
#     del open_fields[0]
# A* test2

mass_tuple: list[tuple[int, int]] = [(333, 1), (444, 2), (555, 3), (666, 4), (777, 0)]
mass_tuple.sort(key=lambda x: x[1], reverse=False)
print(mass_tuple)
new_tuple = (777, 1)
if new_tuple[0] in mass_tuple[0]:
    print("Yooo")
    field_before_value = [x[1] for x in mass_tuple if x[0] == new_tuple[0]]
    if new_tuple[1] < field_before_value[0]:
        result = [
            idx for idx, tup in enumerate(mass_tuple) if tup[0] == new_tuple[0]
        ]
        del mass_tuple[result[0]]
        mass_tuple.insert(result[0], new_tuple)
        print(mass_tuple)
    else:
        mass_tuple.append(new_tuple)
# --------------

