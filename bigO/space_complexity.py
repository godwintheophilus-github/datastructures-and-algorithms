def sum(n: str) -> int :
    if n <= 0:
        return 0
    return n + sum(n-1) # value is stored in stack

print(sum(3))