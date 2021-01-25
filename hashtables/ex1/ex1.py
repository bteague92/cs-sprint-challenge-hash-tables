def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    cache = {}

    #loop through range
    for item in range(length):
        #if limit - the index of weights is in the cache return item and counterpart
        if limit - weights[item] in cache:
            return [item, cache[limit - weights[item]]]
        else:
            #else add weight at index to cache
            cache[weights[item]] = item

    return None