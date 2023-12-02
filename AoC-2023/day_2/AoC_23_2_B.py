def calculate_result(filename):
    colors = {'red': 12, 'green': 13, 'blue': 14}

    with open(filename, "r") as file:
        res = 0
        for idx, line in enumerate(file.readlines(), 1):
            game = line.strip().split(':')
            moves = game[1].split(';')

            game_power = 0
            max_colors = {'red': 0, 'green': 0, 'blue': 0}

            for move in moves:
                move_parts = move.split(',')

                for move_part in move_parts:
                    single_move_part = move_part.strip().split(' ')
                    print(single_move_part)

                    move_part_number = int(single_move_part[0])
                    move_part_color = single_move_part[1]

                    if max_colors[move_part_color] < move_part_number:
                        max_colors[move_part_color] = move_part_number

                game_power = max_colors['red'] * max_colors['green'] * max_colors['blue']

            res += game_power

        return res


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
