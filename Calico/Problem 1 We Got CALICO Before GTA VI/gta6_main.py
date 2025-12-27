import sys

R_Y, R_M, R_D = 2026, 11, 19
G = "gta6"

meh_line1 = sys.stdin.readline().strip()
if not meh_line1: sys.exit()
T = int(meh_line1)

counter = 0
while counter < T:
    E = sys.stdin.readline().strip()
    D_L = sys.stdin.readline().strip()

    if not D_L: break
    Y, M, D = map(int, D_L.split())

    if Y < R_Y: print(f"we got {E} before {G}")
    elif Y > R_Y: print(f"we got {G} before {E}")
    else:
        if M < R_M: print(f"we got {E} before {G}")
        elif M > R_M: print(f"we got {G} before {E}")
        else:
            if D < R_D: print(f"we got {E} before {G}")
            elif D > R_D: print(f"we got {G} before {E}")

    counter += 1