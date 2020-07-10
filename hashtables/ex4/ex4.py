# Use dictionary keys as a set. Then solve this problem using sets.
# Create 2 dictionaries for pos and neg numbers
# Loop through pos dict
#       if key * -1 is in neg dictionary:
#            add to our list of results

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    pos = {}
    neg = {}

    for num in a:
        if num > 0:
            if num not in pos:
                pos[num] = None
        
        elif num < 0:
            if num not in neg:
                neg[num] = None
    
    result = []

    for number in pos:
        if (number * -1) in neg:
            result.append(number)

    return result


# Let's try writing another function
# This time, we only use 1 dictionary

# Take advantage of the fact that these 2 are effectively the same operation:
#    neg * -1 = pos
#    pos * -1 = neg

# Regardless of whether the positive or negative value is first,
# As long as you record the first number in the pair,
# You can loop through the rest of the list and check to see if value * -1 matches that number
#   If there is a match, then we have identified the pair

# Once again, this function solves the problem by using the dictionary as a set. 
# The values for the keys are irrelevant.

def has_negatives2(a):
    dict = {}
    result = []
    for number in a:
        if (number * -1) not in dict:
            dict[number] = 0
        else:
            result.append(abs(number))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    print(has_negatives2([-1, -2, 1, 2, 3, 4, -4]))
