n = int(input())

# code here
for i in range(1, n + 1):
    
    # spaces
    for j in range(n - i):
        print(" ", end="")
    
    # stars
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()