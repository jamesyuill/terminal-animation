cursor = [
    ['.','.','.','.','.',],
    ['.','.','.','.','o',],
    ['.','.','.','.','.',],
]

# def findTheO():
#     items_per_row = len(cursor[0])
#     matrix_dimensions = len(cursor)
#     total_items = items_per_row * matrix_dimensions
#     matrix_index = 0
#     item_index = 0
#     for row in cursor:
#         for i in row:
#             if i == 'o':
#                 break
#             else:
#                 item_index += 1
#         if i == 'o':
#             break
#         matrix_index += 1


#     x = item_index
#     return {"y":matrix_index,"x":x}

def currentPosition(cursor):
    for i, row in enumerate(cursor):
        for j, element in enumerate(row):
            if element == 'o':
                return {'y':i, 'x':j}
    return None


print(currentPosition(cursor))