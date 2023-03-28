import time


def func1(file_path):
    start = time.time()
    lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.replace("\n", ""))
    end = time.time()
    print(f"time:{end - start}")
    return lines


def func2(file_path):
    start = time.time()
    lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    end = time.time()
    print(f"time:{end - start}")
    return lines


def func3(file_path):
    start = time.time()
    lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            lines.append(line.rstrip())
    end = time.time()
    print(f"time:{end - start}")
    return lines


file_path_test = "first10.txt"
func1(file_path_test)
func2(file_path_test)
func3(file_path_test)
