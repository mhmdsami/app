import sys
import threading


def search_file(file_name, reserved_word):
    with open(file_name, 'r') as file:
        for line in file:
            if reserved_word in line:
                print(f"{file_name}: {line.rstrip()}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python search_word.py [reserved_word] [file1] [file2] ...")
        sys.exit(1)

    reserved_word = sys.argv[1]
    files = sys.argv[2:]

    threads = []
    for file_name in files:
        t = threading.Thread(target=search_file, args=(file_name, reserved_word))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
