def largest_smallest(numbers):
    return max(numbers),min(numbers)

large,small = largest_smallest([10,5,30,2,20])

print("largest:",large)
print("smallest:",small)