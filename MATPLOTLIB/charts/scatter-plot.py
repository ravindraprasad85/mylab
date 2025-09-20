#When we have to analyse the co-relations between values the we use scatter plot pattern
import matplotlib.pyplot as plt
Hours_study = [1,2,3,4,5,6,7,8,9]
marks = [50,70,80, 90, 110, 120, 140, 160, 180]
plt.scatter(Hours_study, marks, color='r', marker='d', label='Marks against Study Hours')
plt.xlabel("Hours Studied")
plt.ylabel("Exam score")
plt.title("Relationship between study and marks")
plt.grid(True)
plt.legend()
plt.show() 