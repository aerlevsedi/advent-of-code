def calculate_result(filename):
    with open(filename, "r") as file:
        res = 0
        for idx, line in enumerate(file.readlines()):
            print(idx, line)
        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
