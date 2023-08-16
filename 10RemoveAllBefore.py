'''
Not all of the elements are important. What you need to do here is to remove from the sequence all of the elements before the given one.

example:

For the illustration we have a sequence [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 - which are 1 and 2.

We have two edge cases here: (1) if a cutting element cannot be found, then the sequence shoudn't be changed. (2) if the sequence is empty, then it should remain empty.

Input: List and the border element.

Output: List or another Iterable (tuple, iterator, generator).
'''

def remove_all_before(items: list, border: int):
    if border in items:
        return items[items.index(border):]
    return items

