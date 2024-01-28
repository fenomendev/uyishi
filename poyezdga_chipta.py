n=int(input())
if n==8 or n==9:
    print("Business 140K")
elif n==1 or n==10:
    print("VIP 210K")
for i in range(2,8):
    if i==n:
        print('Econom 105K')            