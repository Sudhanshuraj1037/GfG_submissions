n = int(input())

# code here
sum = 0
if n == 0:
    print('0')
else:
    for i in range(1,n+1):
        sum = sum + i
    print(sum)