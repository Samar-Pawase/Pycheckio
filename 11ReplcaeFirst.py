'''
In a given sequence the first element should become the last one. An empty sequence or with only one element should stay the same.

example

Input: List.

Output: List or another Iterable (tuple, iterator, generator).
'''
def replace_first(items: list):
    if(len(items)<=1):
        return items
    else:
        items.append(items.pop(0))
        return items

print("Example:")
print(list(replace_first([1, 2, 3, 4])))
replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]
replace_first([]) == []