#When we have to analyse the co-relations between values the we use scatter plot pattern
import matplotlib.pyplot as plt

Hours_study_A = [1,2,3,4,5,6,7,8,9]
marks_obtained_A = [50,70,80, 90, 110, 120, 140, 160, 180]

Hours_study_B = [1,2,3,4,5,6,7,8,9]
marks_obtained_B = [30,40,50, 60, 70, 80, 90, 100, 110]

plt.scatter(Hours_study_A, marks_obtained_A, color='r', marker='d', label='Class-A')
plt.scatter(Hours_study_B, marks_obtained_B, color='g', marker='o', label='Class-B')

plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

plt.title("Comparison beteen two Classes")
plt.grid(True)
plt.legend()
plt.show() 