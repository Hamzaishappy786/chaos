import sys, math

t = int(sys.stdin.readline().strip())
for shiyaun in range(t):
    n = int(sys.stdin.readline().strip())
    awake, snooze = [], []

    for _ in range(n):
        Xi, Yi, Si, Ri = sys.stdin.readline().strip().split()
        Xi, Yi, Si = float(Xi), float(Yi), float(Si)
        if Ri in ("awaken", "woke_up"): awake.append((Xi, Yi, Si))
        else: snooze.append((Xi, Yi, Si))

    x_lo, x_hi = -1e18, 1e18
    y_lo, y_hi = -1e18, 1e18

    cx = sum(x for x, _, _ in awake) / len(awake)
    cy = sum(y for _, y, _ in awake) / len(awake)

    awake.sort(key=lambda a: (a[0]-cx)**2 + (a[1]-cy)**2)
    awake = awake[:20]
    epsilin = 1e-7
    x_min = min(x for x, y, s in awake) - 20
    x_max = max(x for x, y, s in awake) + 20
    y_min = min(y for x, y, s in awake) - 20
    y_max = max(y for x, y, s in awake) + 20

    found = False
    for ix in range(int(math.floor(x_min)), int(math.ceil(x_max))+1):
        if found: break
        for iy in range(int(math.floor(y_min)), int(math.ceil(y_max))+1):
            xE = ix + 0.5
            yE = iy + 0.5
            smin, smax = 0.0, 1e30
            valid = True

            for x, y, s in awake:
                d2 = (x - xE)**2 + (y - yE)**2
                smin = max(smin, s * d2)

            for x, y, s in snooze:
                d2 = (x - xE)**2 + (y - yE)**2
                smax = min(smax, s * d2)

            if smin < smax - epsilin:
                print(ix, iy, ix + 1, iy + 1)
                found = True
                break