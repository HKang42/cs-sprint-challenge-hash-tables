# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Loop through list of file paths and create dictionary where each key is
    # the file (last entry in the path) and each value a list of file path(s)
    path_dict = {}
    for path in files:

        file = path.split("/")[-1]
        if file not in path_dict:
            path_dict[file] = [path]
        
        else:
            path_dict[file] += [path]

    result = []

    # Loop through every file in the query
    #   If the file exists in our dictionary:
    #       record the filepath(s) for that file
    
    for file in queries:
        if file in path_dict:
            result += (path_dict[file])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
