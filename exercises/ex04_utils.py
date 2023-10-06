"""EX04: Utils exercise."""
__author__ = "730679428"

def all(search_list: list[int], num: int) -> bool:
    i: int = 0
    while i < len(search_list):
        if search_list[i] != num:
            return False
        else:
            i += 1
    return True


def max(search_list: list[int]) -> int:
    if len(search_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    largest: int = search_list[0]
    while i < len(search_list):
        if search_list[i] > largest:
            largest = search_list[i]
        i += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    i: int = 0
    if len(list1) != len(list2):
        return False
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True