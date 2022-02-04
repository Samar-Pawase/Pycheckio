'''
You have a sequence of strings, and you'd like to determine the most frequently occurring string in the sequence. It can be only one.

Input: non empty list of strings.

Output: a string.
'''

def most_frequent(data):
    return max(data,key=data.count)

data = ["a", "b", "c", "a", "b", "a"]
print(most_frequent(data))