student = {
    "name": "rahul kumar",
    "subject" : {
        "phy": 40,
        "chem": 55,
        "math": 60,
        "hindi": 70
    }
}

teacher = {
    "name": "maurya",
    "coach": ["hindi","english","math","phy"]
}


#print(student["name"])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("subject"))
student.update(teacher)
print(student)