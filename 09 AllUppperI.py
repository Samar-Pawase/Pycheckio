'''
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string (str).

Output: A logic value (bool).

Examples:

assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
'''
def is_all_upper(a):
    return a.upper() == a

a = "ALL UPPER"
print(is_all_upper(a))