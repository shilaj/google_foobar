def solution(n):
    x = int(n)
    count = 0
    while x > 1:
        if x % 2 == 0:
            x = x/2
        elif (x == 3 or x % 4 == 1):
            x = x - 1
        else: 
            x = x + 1 

        count += 1

    return count