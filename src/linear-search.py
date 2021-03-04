def linear_search(arr, target):
    # look at every item, check if it is the item we are looking for
    for item in arr:
        if item == target:
            # we have found our item
            return True
    return False    

our_array = [1, 2, 3, 4, 5, 16, 17, 18, 19]

 # sometimes the only option you have is to search through every possible location
 # this circumstance leaves us with a runtime of O(n)

# rather than representing an iterative behavior with a loop we can represent it with recursion
# we start by simplifying the conditon of how we check if the item is the target

# v1
def rec_search(arr, target):
    # check if item is target, if not -> move to next item
    if arr[0] == target:
        return True
    else:
        found = rec_search(arr[1:], target)
        return found
# v2
def rec_search(arr, target):
    # account for the case of arr shrinking to 0
    if len(arr) == 0:
        return False
    elif arr[0] == target:
        return True

    else:
        found = rec_search(arr[1:], target)
        return found