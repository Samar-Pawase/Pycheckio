'''
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string (str), that consists of digits.

Output: An integer (int).
'''

def beginning_zeros(a: str) -> int:
    count = 0
    for i in a:
        if i=='0':
            count+=1
        elif(i!='0'):
            break
    return count

print("Example:")
print(beginning_zeros("00010"))
print(beginning_zeros("010010"))
print(beginning_zeros("0"))