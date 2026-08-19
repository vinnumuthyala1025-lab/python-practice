def unique(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

print(unique([1,2,2,3,4,4,5]))