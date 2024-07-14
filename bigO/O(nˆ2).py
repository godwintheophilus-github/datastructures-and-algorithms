def print_range(n: str) -> None:
    for i in range(n):
        for j in range(n):
            print(i)
            print(j)


print_range(100) # this is O(nˆ2) complexity