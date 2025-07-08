def count_lines_in_file(filename):
    """
    Counts the number of lines in a file.

    :param filename: The name of the file to count lines in.
    :return: The number of lines in the file.
    """
    try:
        with open(filename, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
if __name__ == "__main__":
    filename = 'readme.txt'
    line_count = count_lines_in_file(filename)
    print(f"The file '{filename}' contains {line_count} lines.")
