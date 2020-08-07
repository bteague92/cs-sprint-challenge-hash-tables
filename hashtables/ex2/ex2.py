#  Hint:  You may not need all of these.  Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    for item in tickets:
        cache[item.source] = item.destination

    fixed = []

    next = cache["NONE"]
    # print("NEXT: ", next)
    fixed.append(next)

    for item in range(0, length):
        next = cache[next]
        # print("NEXT INNER: ", next)
        # print(next)
        fixed.append(next)
        if next == "NONE":
            break

    return fixed