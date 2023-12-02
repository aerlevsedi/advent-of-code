def calculate_result(filename):
    digits_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
              'nine': 9}

    with open(filename, "r") as file:
        res = 0
        for idx, line in enumerate(file):
            found_words = []
            for key in digits_map.keys():
                index = line.find(key)
                if index != -1:
                    found_words.append((index, key))

            digits = list(filter(lambda x: x.isdigit() or x in digits_map.keys(), line))

            number = digits[0] + digits[-1]
            res += int(number)
        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
