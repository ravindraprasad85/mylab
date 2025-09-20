# f = open("myfile.txt", "r")
# data = f.read()
# print(data)

# f.close()
with open("SampleSuperstore.xlsx", "r") as f:
    data = f.read()
    print(data)
