a = [[3, 2], [0, 9, 4]]


def found_zero_in_board(item, board):
    index = []
    for i in board:
        for j in i:
            if j == item:
                index.append(board.index(i))
                index.append(i.index(j))
    return index


print(found_zero_in_board(0, a))

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
