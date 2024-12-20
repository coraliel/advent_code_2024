directions = {
    "upper": (-1, 0),
    "lower": (1, 0),
    "next": (0, 1),
    "previous": (0, -1),
    "upper_left": (-1, -1),
    "upper_right": (-1, 1),
    "lower_left": (1, -1),
    "lower_right": (1, 1),
}


def get_diagonal_direction(direction):
    """
    Returns the coordinates of the opposite diagonal direction.
    """
    diagonal_pairs = {
        "upper_left": "lower_right",
        "lower_right": "upper_left",
        "upper_right": "lower_left",
        "lower_left": "upper_right",
    }
    if direction not in diagonal_pairs:
        raise ValueError(f"Invalid diagonal direction: {direction}")
    return directions[diagonal_pairs[direction]]


def read_file_to_array(file_path):
    """
    Reads a file and converts it into a 2D array.
    """
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]


def is_within_bounds(array, row, col):
    """
    Checks if the given position is within the bounds of the array.
    """
    return 0 <= row < len(array) and 0 <= col < len(array[0])


def get_position(array, row, col, direction):
    """
    Calculates the position based on the direction and ensures it's within bounds.
    """
    row_offset, col_offset = direction
    next_row = row + row_offset
    next_col = col + col_offset
    if is_within_bounds(array, next_row, next_col):
        return next_row, next_col
    return None, None


def find_pattern(multi_array, start_symbol, pattern, directions_to_check):
    """
    Finds occurrences of a pattern in the given directions.
    """
    count = 0

    for row_index, row in enumerate(multi_array):
        for col_index, value in enumerate(row):
            if value == start_symbol:
                for direction_name, direction in directions_to_check.items():
                    found = True
                    for i, symbol in enumerate(pattern):
                        next_row, next_col = row_index + i * direction[0], col_index + i * direction[1]
                        if not is_within_bounds(multi_array, next_row, next_col) or multi_array[next_row][next_col] != symbol:
                            found = False
                            break

                    if found:
                        print(f"Found '{''.join(pattern)}' in {direction_name} starting at ({row_index}, {col_index})")
                        count += 1
    return count


def look_for_xmas(multi_array):
    """
    Finds all occurrences of 'XMAS' in any direction.
    """
    symbols = ['X', 'M', 'A', 'S']
    count = find_pattern(multi_array, 'X', symbols, directions)
    print(f"Total 'XMAS' found: {count}")
    return count


def look_for_x_mas(multi_array):
    """
    Counts occurrences of 'MAS' or 'SAM' patterns forming an 'X' around 'A'.
    """
    count = 0

    for row_index, row in enumerate(multi_array):
        for col_index, value in enumerate(row):
            if value == 'A':  # Start from 'A'
                # Get diagonal positions
                ul_row, ul_col = get_position(multi_array, row_index, col_index, directions["upper_left"])  # Upper left
                lr_row, lr_col = get_position(multi_array, row_index, col_index, directions["lower_right"])  # Lower right
                ur_row, ur_col = get_position(multi_array, row_index, col_index, directions["upper_right"])  # Upper right
                ll_row, ll_col = get_position(multi_array, row_index, col_index, directions["lower_left"])  # Lower left

                # Check first diagonal (upper-left to lower-right)
                if (
                        ul_row is not None and lr_row is not None and  # Ensure positions exist
                        (
                                (multi_array[ul_row][ul_col] == 'M' and multi_array[lr_row][lr_col] == 'S') or
                                (multi_array[ul_row][ul_col] == 'S' and multi_array[lr_row][lr_col] == 'M')
                        )
                ):
                    # Check opposite diagonal (upper-right to lower-left)
                    if (
                            ur_row is not None and ll_row is not None and
                            (
                                    (multi_array[ur_row][ur_col] == 'M' and multi_array[ll_row][ll_col] == 'S') or
                                    (multi_array[ur_row][ur_col] == 'S' and multi_array[ll_row][ll_col] == 'M')
                            )
                    ):
                        print(f"Found 'MAS' or 'SAM' cross at ({row_index}, {col_index})")
                        count += 1

    print(f"Total 'MAS' or 'SAM' crosses found: {count}")
    return count


def main():
    input_file = './input.csv'
    multi_dimensional_array = read_file_to_array(input_file)
    # look_for_xmas(multi_dimensional_array)
    look_for_x_mas(multi_dimensional_array)


if __name__ == "__main__":
    main()
