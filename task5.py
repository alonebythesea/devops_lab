def selfDividingNumbers(left):
    def self_dividing(n):
        for d in str(n):
            if d == '0' or n % int(d) > 0:
                return False
        return True
    out = []
    for n in range(left[0], left[1] + 1):
        if self_dividing(n):
            out.append(n)
    return out


left = [int(x) for x in input().split(' ')]
print(selfDividingNumbers(left))
