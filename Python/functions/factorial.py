# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print(fact)

factorial(5)