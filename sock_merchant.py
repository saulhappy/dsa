def sock_merchant(arr, n):
    pairs = 0
    socks = {}

    for sock in arr:
        if sock in socks:
            socks[sock] += 1
        else:
            socks[sock] = 1

    for value in socks.values():
        pairs += value // 2
    
    return pairs


# ANOTHER, MORE PYTHONIC METHOD USING COLLECTIONS
from collections import Counter
return sum(sock // 2 for sock in Counter(arr).values())

print(sock_merchant([1,2,1,2,1,3,2], 7))
