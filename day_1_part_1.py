import csv


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        col1, col2 = [], []
        for row in reader:
            split_row = row[0].strip().split()
            if len(split_row) == 2:  # Ensure there are exactly two columns
                value1, value2 = map(int, split_row)
                col1.append(value1)
                col2.append(value2)
    return col1, col2


def sort_columns_independently(col1, col2):
    col1.sort()
    col2.sort()
    return col1, col2


def calculate_total_difference(col1, col2):
    total = 0
    for val1, val2 in zip(col1, col2):
        total += abs(val1 - val2)
    print(f"Total difference: {total}")
    return total


def main():
    input_file = './day_01_input.csv'
    col1, col2 = read_input_file(input_file)
    sorted_col1, sorted_col2 = sort_columns_independently(col1, col2)
    calculate_total_difference(sorted_col1, sorted_col2)


if __name__ == "__main__":
    main()
