def nid():
# Input: a list instead of a single integer
    a = list(map(int, input("Enter values for a (space-separated): ").split()))

# Input for sets A and B
    A = set(map(int, input("Enter set A values (space-separated): ").split()))
    B = set(map(int, input("Enter set B values (space-separated): ").split()))

    total = 0

# Iterate through the list 'a' instead of a single integer
    for i in a:
        if i in A:
            total += 1
        elif i in B:
            total -= 1

    print(total)

nid()


