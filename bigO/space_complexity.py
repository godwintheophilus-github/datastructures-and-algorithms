def sum(n: str) -> int :
    if n <= 0:
        return 0
    return n + sum(n-1)

print(sum(3))