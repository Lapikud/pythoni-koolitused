

def print_map(game_field):
    row_element_count = len(game_field[0])
    row_index_len = len(str(row_element_count))
    row_length = 2 * row_element_count + row_index_len + 2

    column_indices = map(str, range(row_element_count))
    print(f" ||{'|'.join(column_indices)}|")
    print("=" * row_length)

    for row_index, row in enumerate(game_field):

        row_elements = map(str, game_field[row_index])
        print(f"{row_index}||{'|'.join(row_elements)}|")
        print("-" * row_length)

if __name__ == "__main__":

    field1 = [[0,1,2,3,4,5],
              [1,2,3,4,5,6],
              [2,3,4,5,6,7],
              [3,4,5,6,7,8],
              [4,5,6,7,8,9]]


    print_map(field1)