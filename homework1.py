inputSTR = input("enter a word:")
x = len(inputSTR) 
k = []
n = 0

while n < x:
    k.append(inputSTR[n])
    t = 1
    while n + 1 < x and inputSTR[n] == inputSTR[n+1]:
        t = t + 1
        n = n + 1
    k.append(t)
    n = n + 1

print(k)