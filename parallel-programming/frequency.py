import multiprocessing


def count_chars(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def frequency(strings, worker_count):
    pool = multiprocessing.Pool(worker_count)
    char_count = {}
    for result in pool.map(count_chars, strings):
        for char, count in result.items():
            if char in char_count:
                char_count[char] += count
            else:
                char_count[char] = count
    return char_count


if __name__ == "__main__":
    print(frequency(["cpp", "python", "hello world", "typescript", "rust"], 5))
