import csv


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [list(map(int, row[0].strip().split())) for row in reader]
    return data


def check_trajectory(row):
    if len(row) < 2:
        return False

    direction = "increasing" if row[1] > row[0] else "decreasing"

    for i in range(len(row) - 1):
        if direction == "increasing" and row[i + 1] <= row[i]:
            return False
        if direction == "decreasing" and row[i + 1] >= row[i]:
            return False

    return True


def process_row(row):
    stats = {
        "increase": 0,
        "decrease": 0,
        "deviation": 0,
        "deviation_indices": []
    }

    for i in range(len(row) - 1):
        if row[i + 1] > row[i]:
            stats["increase"] += 1
        elif row[i + 1] < row[i]:
            stats["decrease"] += 1
        else:
            stats["deviation"] += 1
            stats["deviation_indices"].append(i + 1)

    return stats


def remove_outlier(row, index):
    if index is not None and 0 <= index < len(row):
        return row[:index] + row[index + 1:]
    return row


def handle_outliers(row, stats):
    if stats["deviation"] == 1:
        return remove_outlier(row, stats["deviation_indices"][0])

    for i in range(len(row)):
        modified_row = remove_outlier(row, i)
        if check_trajectory(modified_row) and check_range(modified_row):
            return modified_row

    return row


def check_range(row):
    return all(abs(row[i] - row[i + 1]) <= 3 and row[i] != row[i + 1] for i in range(len(row) - 1))


def check_whole_level_trajectory(data):
    number_of_safe = 0

    for row in data:
        if len(row) < 2:
            continue

        stats = process_row(row)
        updated_row = handle_outliers(row, stats)

        print("Original row:", row)
        print("Processed row:", updated_row)

        if check_trajectory(updated_row) and check_range(updated_row):
            number_of_safe += 1
            print("Safe row.")
        else:
            print("Unsafe row.")
            print(f"Stats - Increase: {stats['increase']}, Decrease: {stats['decrease']}, Deviation: {stats['deviation']}\n")

    print("Reports now safe:", number_of_safe)
    return number_of_safe


def validate_rows(data):
    return sum(1 for row in data if check_trajectory(row) and check_range(row))


def main():
    input_file = './input.csv'
    data = read_input_file(input_file)

    print("Validated rows (strict rule):", validate_rows(data))
    print("Validated rows (with Problem Dampener):", check_whole_level_trajectory(data))


if __name__ == "__main__":
    main()
