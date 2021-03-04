"""
I was bored one day and decided to look at last names in the phonebook for my
area.

I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.

When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."

Example:

surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.

*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""
def find_rotation_point(surnames):
    # crate floor index at zero
    # create ceiling index art length - 1
    # keep track of first_name in our window
    #  first_name = surnames[floor_index]

    # while floor index < ceiling_index:
        # guess in the middle of floor and ceiling
        # guess = ceiling + floor // 2( get middle index)
        # if word at guess index is larger than firat_name
            # shrink our floor down to the guess index
        # else
            # shrink our ceiling down to the guess_index

        # if we reach a point where there are only two items left between
        # ceiling and floor, return item at ceiling
        # that item will always be alphabetically smaller
    pass


