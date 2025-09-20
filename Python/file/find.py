# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")

def check_for_word():
    word = "learning"
    line_no = 1
    data = True
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(word, "is found in line num: ", line_no)
                return
            line_no += 1
    return -1
check_for_word()