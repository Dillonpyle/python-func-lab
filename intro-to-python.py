# 1 sum to
def sum_to(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + i
    return sum


print(sum_to(5))

# 2 largest


def largest(list):
    return max(list)


print(largest([10, 4, 2, 231, 91, 54]))

# 3 occurances


def occurances(str1, str2):
    return str1.count(str2)


print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

# 4 product


def product(*args):
    x = 1
    for num in args:
        x *= num
    return x


print(product(4, 5))
print(product(10, 9))
print(product(2, 3, 4))
print(product(3, 5, 10, 6))
