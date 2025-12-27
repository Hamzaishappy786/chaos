import sys

BIG_NUM = 1000000000
big_bear_T_line = sys.stdin.readline().strip()
T_count = int(big_bear_T_line)

for test_case_number in range(T_count):
    board_dima_dima_dima_dima_dima_line = sys.stdin.readline().strip()
    if not board_dima_dima_dima_dima_dima_line: break

    k_pieces_line = sys.stdin.readline().strip()
    if not k_pieces_line: break
    k_count = int(k_pieces_line)

    chess_friends = []
    for idx in range(k_count):
        friend_line = sys.stdin.readline().strip()
        if not friend_line: break
        parts = friend_line.split()
        friend_type = parts[0]
        friend_x = int(parts[1])
        friend_y = int(parts[2])
        chess_friends.append((friend_type, friend_x, friend_y))

    total_slaps = 0
    for i in range(k_count):
        slapper_type, slapper_x, slapper_y = chess_friends[i]
        closest_pals_in_line = {}
        path_pals = []
        if slapper_type == 'R' or slapper_type == 'Q': path_pals.extend([(1, 0), (-1, 0), (0, 1), (0, -1)])
        if slapper_type == 'B' or slapper_type == 'Q': path_pals.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])
        for dx, dy in path_pals: closest_pals_in_line[(dx, dy)] = (BIG_NUM, -1)

        for j in range(k_count):
            if i == j: continue

            victim_type, victim_x, victim_y = chess_friends[j]
            dx_raw = victim_x - slapper_x
            dy_raw = victim_y - slapper_y

            if dx_raw == 0 and dy_raw != 0:
                d = abs(dy_raw)
                dx, dy = 0, dy_raw // d
            elif dy_raw == 0 and dx_raw != 0:
                d = abs(dx_raw)
                dx, dy = dx_raw // d, 0
            elif abs(dx_raw) == abs(dy_raw) and dx_raw != 0:
                d = abs(dx_raw)
                dx, dy = dx_raw // d, dy_raw // d
            else: continue

            direction_vector = (dx, dy)
            if direction_vector not in closest_pals_in_line: continue
            current_min_d, _ = closest_pals_in_line[direction_vector]
            if d < current_min_d: closest_pals_in_line[direction_vector] = (d, j)

        for lalalala, (d, j) in closest_pals_in_line.items():
            if j != -1: total_slaps += 1

    print(total_slaps)