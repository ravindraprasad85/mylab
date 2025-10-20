

#Comparing between Predections and actual results
from sklearn.metrics import confusion_matrix 
#True Answers
y_true = [0, 1, 1, 1, 0, 1, 0, 1]

#Models Predections
y_pred = [0, 1, 1, 0, 1, 1, 1, 0]

cm = confusion_matrix(y_true, y_pred)
#Evaluation
print("Confussion: ", cm)

