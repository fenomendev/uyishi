s = input()
check = 0
for i in s:
    if i == '1' and check == -1:
        print("NO")
        exit()
    if i == '1' and check == 0:
        check += 1
    elif i == '0' and check > 0:
        check = -1

if len(s) != 0:
    print("YES")
else:
    print("NO")
