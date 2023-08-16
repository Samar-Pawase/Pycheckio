'''
You have a number and you need to determine which digit in this number is the biggest.

Input: A positive integer (int).

Output: An integer 0-9 (int).
'''
def max_digit(value: int) -> int:
    return int(max(str(value)))

print("Example:")
print(max_digit(1029385))