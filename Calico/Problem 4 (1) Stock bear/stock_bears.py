import sys
import math

BIG_ASS_NUMBER = 10000000000
big_bear_T_line = sys.stdin.readline().strip()
T_count = int(big_bear_T_line)

for test_case_number in range(T_count):
    board_dims_line = sys.stdin.readline().strip()
    if not board_dims_line: break

    k_pieces_line = sys.stdin.readline().strip()
    if not k_pieces_line: break
    k_count = int(k_pieces_line)

    chess_friends = []
    for piece_index in range(k_count):
        friend_line = sys.stdin.readline().strip()
        if not friend_line: break

        parts = friend_line.split()
        friend_type = parts[0]
        friend_x = int(parts[1])
        friend_y = int(parts[2])
        chess_friends.append((friend_x, friend_y, friend_type, piece_index))

    line_groups = {}
    for piece_index in range(k_count):
        x, y, piece_type, original_i = chess_friends[piece_index]
        key_horiz = ('H', y)
        line_groups.setdefault(key_horiz, []).append((x, y, piece_type, original_i))
        key_vert = ('V', x)
        line_groups.setdefault(key_vert, []).append((x, y, piece_type, original_i))
        key_diag = ('D', y - x)
        line_groups.setdefault(key_diag, []).append((x, y, piece_type, original_i))
        key_anti = ('A', y + x)
        line_groups.setdefault(key_anti, []).append((x, y, piece_type, original_i))

    total_slaps = 0
    for line_key, pals_on_line in line_groups.items():
        line_type = line_key[0]
        if line_type == 'H': pals_on_line.sort(key=lambda p: p[0])
        elif line_type == 'V': pals_on_line.sort(key=lambda p: p[1])
        else: pals_on_line.sort(key=lambda p: p[0])

        for i in range(len(pals_on_line)):
            Ax, Ay, A_type, A_idx = pals_on_line[i]
            if i + 1 < len(pals_on_line):
                Bx, By, B_type, B_idx = pals_on_line[i + 1]
                can_attack = False
                if line_type == 'H' or line_type == 'V':
                    if A_type == 'R' or A_type == 'Q': can_attack = True
                elif line_type == 'D' or line_type == 'A':
                    if A_type == 'B' or A_type == 'Q': can_attack = True
                if can_attack: total_slaps += 1

            if i - 1 >= 0:
                Bx, By, B_type, B_idx = pals_on_line[i - 1]
                can_attack = False
                if line_type == 'H' or line_type == 'V':
                    if A_type == 'R' or A_type == 'Q': can_attack = True
                elif line_type == 'D' or line_type == 'A':
                    if A_type == 'B' or A_type == 'Q': can_attack = True

                if can_attack: total_slaps += 1

    print(total_slaps // 2)