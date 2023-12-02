def calculate_result(filename):
    colors = {'red': 12, 'green': 13, 'blue': 14}

    with open(filename, "r") as file:
        res = 0
        for idx, line in enumerate(file.readlines(), 1):
            game = line.strip().split(':')
            moves = game[1].split(';')

            is_possible = True
            for move in moves:
                move_parts = move.split(',')

                for move_part in move_parts:
                    single_move_part = move_part.strip().split(' ')
                    print(single_move_part)
                    move_part_number = int(single_move_part[0])
                    move_part_color = single_move_part[1]

                    if move_part_number > colors[move_part_color]:
                        is_possible = False
                        break

                if not is_possible:
                    break

            if is_possible:
                res += idx

        print(res)

        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
