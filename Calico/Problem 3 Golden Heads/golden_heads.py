import sys

lane_hi_lane = sys.stdin.readline().strip()
T = int(lane_hi_lane)

for shiyaun in range(T):
    line = sys.stdin.readline().strip()
    if not line: break

    parts = line.split()
    if len(parts) < 2: break

    N, M = int(parts[0]), int(parts[1])
    max_depths = [0] * M
    for i in range(N):
        row = sys.stdin.readline().strip()
        if not row: break
        for j in range(M):
            if j < len(row):
                char = row[j]
                if char != '.':
                    depth = int(char)
                    if depth > max_depths[j]: max_depths[j] = depth

    total_area = 0
    for depth in max_depths: total_area += depth
    print(total_area)