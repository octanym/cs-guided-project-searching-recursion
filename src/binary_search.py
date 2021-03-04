def binary_search():
    #  declare  min = 0 and max = len of array - 1
    min = 0
    max - len(array) - 1
    while not max < min:
        #  figure out the guess value by geting the middle integer between min and max
        guess = (max + min) // 2
        # if array[guess] equals the target, we found the element, return the index
        if array[guess] == target:
            return guess
        # if guess was too low, reset min to be one more than the guess
        elif array[guess] < target:
            min = guess + 1
        # if guess was too high, reset max to be one less than the guess
        else:
            max = guess - 1
        #  no match was found
    return -1