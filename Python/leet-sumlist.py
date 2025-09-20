#num = [1, 3, 4, 5, 7, 8, 9, 12, 14, 16, 18, 20, 25, 30]
num = [3, 1, 2, 10, 1]
newnum = []
sum = 0
for i in range(len(num)):
    sum += num[i]
    newnum.append(sum)

print(newnum)