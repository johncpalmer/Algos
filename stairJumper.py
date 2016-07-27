# walking up n stairs, can do 1 or 2 or 3 at a time
# how many ways to reach nth stair?

def stairJumper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    cache = [0]*n
    cache[0] = 1
    cache[1] = 2
    cache[2] = 4

    for i in xrange(3,n):
        cache[i] = cache[i-3] + cache[i-2] + cache[i-1]

    return cache[n-1]

print(stairJumper(1))
print(stairJumper(2))
print(stairJumper(3))
print(stairJumper(4))
print(stairJumper(5))
