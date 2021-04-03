field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def print_field(my_field, de_bug):
    counter = 0
    print(' _ _ _')
    for line in my_field:
        edit_line = ""
        for element in line:
            if de_bug:
                counter += 1
                edit_line += f'|{element}{counter}'
            else:
                edit_line += f'|{element}'
        print(edit_line + '|')


def make_move(my_field, move, coo):
    if my_field[(coo - 1) // 3][(coo - 1) % 3] == "_":
        my_field[(coo - 1) // 3][(coo - 1) % 3] = move
        return my_field, True
    else:
        return my_field, False


def condition_won(my_field, move_type):
    for u in range(2):
        if my_field[u] == [move_type, move_type, move_type]:
            print(f"\nWon {move_type}")
            return True
        if my_field[u][u] == my_field[u - 1][u] and my_field[u - 1][u] == my_field[u - 2][u] and my_field[u][u] == move_type:
            print(f"\nWon {move_type}")
            return True
        if my_field[u][u] == my_field[u - 1][u - 1] and my_field[u - 1][u - 1] == my_field[u - 2][u - 2]:
            if my_field[u][u] == move_type:
                print(f"\nWon {move_type}")
                return True


print("Let's play tic tac toe")
move_type = ['X', 'O']
print(print_field(field , 1))
move_ch = 0
