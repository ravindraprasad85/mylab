cities = ["delhi", "mumbai", "gurgaon", "kanpur", "Bangalore"]
heroes = ["ram", "hanuman", "shyam", "krishna", "bhole"]

def print_length(list):
    print(len(list))

#print_length(cities)
#print_length(heroes)


def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(cities)