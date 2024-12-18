import csv


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            # Split the row into integers
            split_row = list(map(int, row[0].strip().split()))
            data.append(split_row)
    return data


def check_trajectory(row):
    if len(row) < 2:
        return False

    # Determine initial direction
    if row[1] > row[0]:
        print(f"{row[0]} < {row[1]}", "increasing")
        direction = "increasing"
    elif row[1] < row[0]:
        print(f"{row[0]} > {row[1]}", "decreasing")
        direction = "decreasing"
    else:
        return False  # Initial numbers are equal
    for i in range(len(row) - 1):
        if direction == "increasing" and row[i + 1] <= row[i]:
            return False
        if direction == "decreasing" and row[i + 1] >= row[i]:
            return False
    return True


def validate_row(data):
    number_of_safe = 0

    for row in data:
        is_safe = False
        # Check the level evolution for the entire row
        if check_trajectory(row):
            print(row)
            for i in range(len(row) - 1):  # Check adjacent elements
                # Check if the condition for "safe" is satisfied
                if abs(row[i] - row[i + 1]) <= 3 and row[i] != row[i + 1]:
                    is_safe = True
                else:
                    is_safe = False
                    break
        if is_safe:
            number_of_safe += 1  # Count the row as "safe"

    print(number_of_safe)
    return number_of_safe


def main():
    input_file = './input.csv'
    data = read_input_file(input_file)
    validate_row(data)


if __name__ == "__main__":
    main()
