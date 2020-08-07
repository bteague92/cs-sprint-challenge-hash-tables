# Your code here

def finder(files, queries):

    """
    YOUR CODE HERE
    """

    cache = {}

    #add queries to cache
    for item in queries:
        cache[item] = [item]

    result = []

    #add matching file paths to results
    for item in files:
        #check if last part of file path is in cache
        if item.split("/")[-1] in cache:
            result.append(item)

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
