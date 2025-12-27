import sys

DIDDY_NUM = 998244353
t = int(sys.stdin.readline().strip())
for i in range(t):
    line = sys.stdin.readline().strip()
    if not line: continue
    s, k = line.split()
    k = int(k)

    smol, SCREAM = {}, {}
    for ch in s:
        if ch.islower(): smol[ch] = smol.get(ch, 0) + 1
        else: SCREAM[ch.lower()] = SCREAM.get(ch.lower(), 0) + 1

    for lalalala in range(k):
        next_smol, next_SCREAM = {}, {}
        for c in set(smol.keys()) | set(SCREAM.keys()):
            l, u = smol.get(c, 0), SCREAM.get(c, 0)
            next_smol[c], next_SCREAM[c] = u, l + u
        smol, SCREAM = next_smol, next_SCREAM

    result = 0
    for c, n in smol.items(): result += (ord(c) - 96) * n
    for c, n in SCREAM.items(): result += (ord(c.upper()) - 38) * n

    print(result % DIDDY_NUM)