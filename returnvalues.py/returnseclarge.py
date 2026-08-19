
def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]

print(second_largest([10,20,5,40,30]))

