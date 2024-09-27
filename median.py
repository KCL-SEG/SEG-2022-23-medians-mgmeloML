"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(nums):
    n = len(nums)
    nums.sort()
    if n % 2 == 1:
        return nums[int((n+1/2) - 1)]
    else:
        return (nums[int(n/2 - 1)] + nums[int((n + 2)/2 - 1)]) / 2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
    
print(numbers)
print(median(numbers))


