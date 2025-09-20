#Set is a Method
#Sets method => Union and intersection

#list = []
#dict = {"name": "ravi",}
#tuple = ("a",)
#set = set()


#add, remove, clear, pop
collection = set()
collection.add(1)
collection.add(2)
print(collection)

collection.remove(2)
print(collection)

collection.clear()

#Union and Intersection
list1 = {1,2,3}
list2 = {2,3,4}
print(list1.union(list2))
print(list1.intersection(list2))

