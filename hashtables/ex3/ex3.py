def intersection(arrays):

    cache = {}
    list = []

    #loop through arrays
    for arr in arrays:
        #loop through inner array
        for item in arr:
            #if items not in cache, add it
            if item not in cache:
                cache[item] = 1
            #if it is in cache, increment by one
            else:
                cache[item] += 1
    
    #loop through cache
    for item in cache:
        #if item == length of array then its in every array
        if cache[item] == len(arrays):
            list.append(item)

    return list


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
