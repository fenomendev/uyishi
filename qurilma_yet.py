n=int(input())
k=int(input())
if (n % k == 0):
    print(n // k)
else:
    print(n // k + 1)