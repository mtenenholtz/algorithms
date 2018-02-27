def reverse_int(num):
    rev_num = [x for x in reversed(str(num))]
    if num < 0:
        _ = rev_num.pop()
        return int(''.join(rev_num)) * -1
    return int(''.join(rev_num))
