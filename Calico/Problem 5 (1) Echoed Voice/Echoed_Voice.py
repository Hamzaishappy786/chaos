import sys

BIG_MOD = 998244353

def read_my_input():
    t = sys.stdin.readline().strip()
    if not t:
        sys.exit()
    return int(t)

t = read_my_input()

for _ in range(t):
    line = sys.stdin.readline().strip()
    if not line:
        continue
    s, k = line.split()
    k = int(k)

    tiny_letters = {}
    MEGA_LETTERS = {}

    for ch in s:
        if ch.islower():
            tiny_letters[ch] = tiny_letters.get(ch, 0) + 1
        else:
            MEGA_LETTERS[ch.lower()] = MEGA_LETTERS.get(ch.lower(), 0) + 1

    for _ in range(k):
        baby_next = {}
        giga_next = {}
        for c in set(tiny_letters.keys()) | set(MEGA_LETTERS.keys()):
            l = tiny_letters.get(c, 0)
            u = MEGA_LETTERS.get(c, 0)
            baby_next[c] = u
            giga_next[c] = l + u
        tiny_letters, MEGA_LETTERS = baby_next, giga_next

    final_score = 0
    for c, n in tiny_letters.items():
        final_score += (ord(c) - 96) * n
    for c, n in MEGA_LETTERS.items():
        final_score += (ord(c.upper()) - 38) * n

    final_score %= BIG_MOD
    print(final_score)
