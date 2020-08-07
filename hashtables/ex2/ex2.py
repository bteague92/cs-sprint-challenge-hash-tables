#  Hint:  You may not need all of these.  Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}

    #loop through tickets and add to cache
    for item in tickets:
        cache[item.source] = item.destination

    fixed = []

    #set first
    next = cache["NONE"]
    # print("NEXT: ", next)
    #put first in list
    fixed.append(next)

    #loop through
    for item in range(0, length):
        #set next to the next ticket
        next = cache[next]
        # print("NEXT INNER: ", next)
        # print(next)
        #append next ticket to list
        fixed.append(next)
        #if next is None then its the end so exit
        if next == "NONE":
            break

    return fixed