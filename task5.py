def selfDividingNumbers(borders):
    def self_dividing(n):
        for d in str(n):
            if d == '0' or n % int(d) > 0:
                return False
        return True
    out = []
    for n in range(borders[0], borders[1] + 1):
        if self_dividing(n):
            out.append(n)
    return out


borders = [int(x) for x in input().split(' ')]
print(selfDividingNumbers(borders))
