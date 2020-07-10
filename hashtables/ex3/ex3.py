def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    num_dict = {}

    for sublist in arrays:

        for num in sublist:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
    
    result = []

    for number in num_dict:
        if num_dict[number] >= 2:
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))