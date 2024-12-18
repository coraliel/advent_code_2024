import re


def read_file(file_path):
    """Read the contents of a file and return it."""
    with open(file_path, "r") as file:
        return file.read()


def extract_multiplications(data):
    """Extract pairs of numbers from 'mul(digit,digit)' patterns in the data."""
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return [(int(a), int(b)) for a, b in re.findall(pattern, data)]


def calculate_total(pairs):
    """Calculate the total of all products from the extracted pairs."""
    total = sum(a * b for a, b in pairs)
    print(f"Total of all 'mul(digit,digit)' products: {total}")


def split_data(data):
    pattern = r"(?=(do|don't)\(\))"
    return re.split(pattern, data, flags=re.IGNORECASE)


def sort_data(data):
    matches = split_data(data)  # Split the data
    # Filter out matches that start with "don't"
    filtered_matches = [match for match in matches if not match.strip().lower().startswith("don't")]
    return ''.join(filtered_matches)


def main():
    input_file = './input.csv'
    print("Unfiltered data: ")
    data = read_file(input_file)
    pairs = extract_multiplications(data)
    calculate_total(pairs)
    print("Filtered data: ")
    data_do = sort_data(data)
    pairs = extract_multiplications(data_do)
    calculate_total(pairs)


if __name__ == "__main__":
    main()
