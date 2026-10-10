inputStr = input("enter code str:")
k = []
l = len(inputStr)
n = 1
t = 0
while n < l:
    c = int(inputStr[n])
    while t < c:
        k.append(inputStr[n - 1])
        t += 1
    t = 0
    n += 2
print(k)