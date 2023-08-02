from sys import argv
import json
import file_handler


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]

    # Open the files and send it to the file reader
    input_file = open(file_path, 'r')

    file = file_handler.File_handler()
    file.read_file(input_file)


if __name__ == "__main__":
    main()
