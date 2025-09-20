# f = open("SampleSuperstore.xlsx", "r")
# data = f.read()
# print(data)
# f.close()

f = open("SampleSuperstore.xlsx", "+a")
data = f.write("\nThis is second line")

