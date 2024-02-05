def K(n, ns):
    count = 1
    LR = []
    RL = []
    for i in range(1, n):
        if count < ns[i]:
            LR.append(count)
            count += 1
        else:
            LR.append(ns[i])
            count = ns[i] + 1;

    count = 1