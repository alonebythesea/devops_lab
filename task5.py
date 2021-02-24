def selfDividingNumbers(left, right):
    def self_dividing(n):
        for d in str(n):
            if d == '0' or n % int(d) > 0:
                return False
        return True
    out = []
    for n in range(left, right + 1):
        if self_dividing(n):
            out.append(n)
    return out


left, right = int(input()), int(input())
print(selfDividingNumbers(left, right))
