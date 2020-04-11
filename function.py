def func(n, debug=False):
    if n <= 1:
        return True
    seq_count = 0
    original_n = n
    if debug:
        num_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if debug:
            num_list.append(n)
        seq_count += 1
        # if seq_count > original_n * original_n:
        #     print(f'{original_n} runs too long')
        #     return False
    if debug:
        print(num_list)
    return True
