

def print_map(game_field, pointer_coords=(1,1)):

    row_count = len(game_field)
    col_count = len(game_field[0])
    pointer_row, pointer_col = pointer_coords

    if not pointer_row < row_count:
        raise Exception(f"Pointer out of bounds: field has {row_count} rows, pointer is at index {pointer_row}.")
    if not pointer_col < col_count:
        raise Exception(f"Pointer out of bounds: field has {col_count} columns, pointer is at index {pointer_col}.")

    for row_index, row in enumerate(game_field):

        row_elements = list(map(str, game_field[row_index]))

        if row_index == pointer_row and pointer_col != 0:
            print(f" {'  '.join(row_elements[:pointer_col])}" + \
                  f" <{row_elements[pointer_col]}> " + \
                  '  '.join(row_elements[pointer_col + 1:]))

        elif row_index == pointer_row and pointer_col == 0:
            print(f"<{row_elements[0]}> {'  '.join(row_elements[1:])}")

        else:
            print(f" {'  '.join(row_elements)}")


if __name__ == "__main__":

    field1 = [[0,1,2,3,4,5],
              [1,2,3,4,5,6],
              [2,3,4,5,6,7],
              [3,4,5,6,7,8],
              [4,5,6,7,8,9]]


    print_map(field1, (0, 0))
    print()
    print_map(field1, (0, 1))
    print()
    print_map(field1, (3, 3))
    print()
    # Row/columns error
    # print_map(field1, (5, 3))
    # print_map(field1, (4, 6))
