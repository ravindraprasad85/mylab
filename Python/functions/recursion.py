# def show(num):
#     if(num == 0):
#         return
#     print(num)
#     show(num-1)

# show(5)



# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))


def print_item(list, idx=0):
    if (len(list) == idx):
        return
    print(list[idx])
    print_item(list, idx+1)





cities = ["delhi", "mumbai", "gurgaon", "kanpur", "Bangalore"]
heroes = ["ram", "hanuman", "shyam", "krishna", "bhole"]

print_item(cities)