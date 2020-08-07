def has_negatives(a):

    cache = {}
    list = []

    #loop through values
    for item in a:
        #add to hash table
        cache[item] = item
        #if opposite is in table
        if -item in cache:
            #if item doesnt equal zero
            if item != 0:
                #if item is less than zero append positive version
                if item < 0:
                    list.append(item * -1)
                #else append item
                else:
                    list.append(item)
    return list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
