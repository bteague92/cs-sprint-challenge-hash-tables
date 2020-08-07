# Your code here

def finder(files, queries):

    """
    YOUR CODE HERE
    """

    cache = {}

    #loop through queries
    for item in queries:
        #add queries to cache
        cache[item] = [item]

    #create list for results
    list = []

    #loop through files
    for item in files:
        #check if last part of file path is in cache
        if item.split("/")[-1] in cache:
            #if it is, append it to the list
            list.append(item)

    return list



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
