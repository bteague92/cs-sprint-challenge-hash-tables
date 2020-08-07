def has_negatives(a):

    cache = {}
    list = []

    for item in a:
        #add to hash table
        cache[item] = item
        if -item in cache:
            if item != 0:
                if item < 0:
                    list.append(item * -1)
                else:
                    list.append(item)
    return list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
