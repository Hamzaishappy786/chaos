def get_word(N):
    if N % 15 == 0: return "bizzfuzz"
    elif N % 3 == 0: return "bizz"
    elif N % 5 == 0: return "fuzz"
    else: return str(N)

import sys
lane_hi_lane = sys.stdin.readline().strip()
T = int(lane_hi_lane)

for _ in range(T):
    word_1 = sys.stdin.readline().strip()
    word_2 = sys.stdin.readline().strip()

    if not word_1 or not word_2: break
    if word_1.isdigit():
        N = int(word_1) + 1
        print(get_word(N + 1))
        continue

    if word_2.isdigit():
        N = int(word_2)
        print(get_word(N + 1))
        continue

    if word_1 == "fuzz" and word_2 == "bizz":
        print("crap")
        continue

    N = -1
    for n_current in range(1, 106):
        if get_word(n_current) == word_2 and get_word(n_current - 1) == word_1:
            N = n_current
            break

    if N != -1: print(get_word(N + 1))