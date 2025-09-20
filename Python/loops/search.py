num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
x = 5

i = 0
while i < len(num):
    if(num[i] == x):
        print(x, "Found at index", i)
        break
    else:
        print("Finding...")
    i+=1
print("===END===")
