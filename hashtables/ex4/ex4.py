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


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
