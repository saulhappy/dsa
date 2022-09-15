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
