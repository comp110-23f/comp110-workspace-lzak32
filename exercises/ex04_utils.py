"""EX04: Utils exercise."""
__author__ = "730679428"


def all(search_list: list[int], num: int) -> bool:
    """Returns bool if all nums in list are equal to num."""
    # initialize index
    i: int = 0
    # return False if list is empty
    if len(search_list) == 0:
        return False
    # check each item of list
    while i < len(search_list):
        if search_list[i] != num:
            return False
        else:
            i += 1
    return True


def max(search_list: list[int]) -> int:
    """Returns the int with largest value in list."""
    if len(search_list) == 0:
        raise ValueError("max() arg is an empty List")
    # start at index 1
    i: int = 1
    # initialize largest value
    largest: int = search_list[0]
    # loop through list to check if item is new largest
    while i < len(search_list):
        if search_list[i] > largest:
            largest = search_list[i]
        i += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns bool for if two lists are equal."""
    # initialize index
    i: int = 0
    # ensure lists are of same length
    if len(list1) != len(list2):
        return False
    # check each item in list
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True