def calculate_result(filename):
    with open(filename, "r") as file:
        parts_sum = 0
        engine = file.readlines()

    for i in range(len(engine)):
        prev_line = []
        next_line = []
        if i != 0:
            prev_line = engine[i-1].strip()
        line = engine[i].strip()
        if i != len(engine)-1:
            next_line = engine[i+1].strip()

        for char_idx, char in enumerate(line):
            number_up = 0
            number_up_left = 0
            number_up_right = 0
            number_left = 0
            number_right = 0
            number_down = 0
            number_down_left = 0
            number_down_right = 0

            if char != '.' and not char.isdigit():
                if i != 0:
                    if prev_line[char_idx].isdigit():
                        number_up = find_number(prev_line, char_idx, 0)
                    else:
                        if char_idx-1 >= 0 and prev_line[char_idx-1].isdigit():
                            number_up_left = find_number(prev_line, char_idx-1, -1)
                        if char_idx+1 < len(line) and prev_line[char_idx+1].isdigit():
                            number_up_right = find_number(prev_line, char_idx+1, 1)

                if i != len(engine)-1:
                    if next_line[char_idx].isdigit():
                        number_down = find_number(next_line, char_idx, 0)
                    else:
                        if char_idx-1 >= 0 and next_line[char_idx-1].isdigit():
                            number_down_left = find_number(next_line, char_idx-1, -1)
                        if char_idx+1 < len(next_line) and next_line[char_idx+1].isdigit():
                            number_down_right = find_number(next_line, char_idx+1, 1)


                if char_idx-1 >= 0 and line[char_idx-1].isdigit():
                    number_left = find_number(line, char_idx-1, -1)

                if char_idx+1 < len(line) and line[char_idx+1].isdigit():
                    number_right = find_number(line, char_idx+1, 1)

                parts_sum += (number_left + number_right + number_down + number_down_left + number_down_right
                              + number_up + number_up_left + number_up_right)

    return parts_sum


def find_number(line, char_idx, direction):
    number = 0

    if direction == 0 or direction == -1:
        while char_idx >= 0 and line[char_idx].isdigit():
            char_idx -= 1
        return find_number(line, char_idx+1, 1)

    while char_idx <= len(line)-1 and char_idx >= 0 and line[char_idx].isdigit():
        number = number * 10 + int(line[char_idx])
        char_idx += direction
    return number


if __name__ == "__main__":
    # print(find_number("..123.12", 4, -1))
    result = calculate_result("input.txt")
    print(result)
