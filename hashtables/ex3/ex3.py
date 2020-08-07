def intersection(arrays):

    cache = {}
    count = 0

    for item in arrays[count]:
        if count < len(arrays):
            if item in cache:
                result.append(item)
                count += 1
            else: 
                cache[item] = [item]
                count += 1
        else:
            if item in cache:
                result.append(item)
            else: 
                cache[item] = [item]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
