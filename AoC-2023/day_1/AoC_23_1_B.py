def calculate_result(filename):
    digits_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                  'nine': 9}

    with open(filename, "r") as file:
        res = 0
        for idx, line in enumerate(file):
            found_words = []
            for key in digits_map.keys():
                first_index = line.find(key)
                last_index = line.rfind(key)

                if first_index != -1:
                    found_words.append((first_index, digits_map.get(key)))

                if last_index != -1 and last_index != first_index:
                    found_words.append((last_index, digits_map.get(key)))

            for number in digits_map.values():
                first_index = line.find(str(number))
                last_index = line.rfind(str(number))

                if first_index != -1:
                    found_words.append((first_index, number))

                if last_index != -1 and last_index != first_index:
                    found_words.append((last_index, number))

            found_words.sort(key=lambda x: x[0])
            number = int(found_words[0][1]*10 + found_words[-1][1])
            res += number
        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
