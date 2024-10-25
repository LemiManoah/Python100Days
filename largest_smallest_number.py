def find_smallest_and_largest(numbers):
    if not numbers:
        return None, None #if list is empty, return empty for both

    #set the largest and smallest numbers to be the number at the index [0]
    largest = smallest = numbers[0]

    #iterate through the list starting from the second element
    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return smallest, largest



numbers = [10, 3, 6, 1, 9, 15, -2]
largest, smallest = find_smallest_and_largest(numbers)
print(f"Largest: {largest}, Smallest: {smallest}")
