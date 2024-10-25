def find_second_largest_number(numbers):
    #check if the list has 2 or more numbers, throw an error if not
    if len(numbers) < 2:
        return "There must be at least 2 numbers"

    #set the largest and second largest numbers to negative infinity to ensure the smaller than all numbers in the list
    largest = second_largest = float('-inf')

    #compare each num in the numbers list to the largest and second largest numbers
    for num in numbers:
        if num > largest:
            # Update second largest first
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "Error: There is no second largest number (all numbers might be the same)."

    return second_largest



numbers = [12, 35, 1, 10, 3, 1]
second_largest = find_second_largest_number(numbers)
print(f"The second largest number is: {second_largest}")


