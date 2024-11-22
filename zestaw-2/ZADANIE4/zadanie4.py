def fun(n):
    tab = []
    while n > 0:
        tab.append(n % 2)
        n = n // 2
    tab.reverse()
    max_zero = 0
    current = 0
    inside_gap = False
    for bit in tab:
        if bit == 1:
            if inside_gap:
                max_zero = max(max_zero, current)
            inside_gap = True
            current = 0
        elif inside_gap:
            current += 1
    return max_zero

if __name__ == "__main__":
    test_values = [529, 20, 15, 1041]
    for N in test_values:
        wynik = fun(N)
        print(f"Reprezentacja binarna {N}: {bin(N)}")
        print(f"fun({N}): {wynik}")
