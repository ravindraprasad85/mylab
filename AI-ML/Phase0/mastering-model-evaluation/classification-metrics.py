from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
#True Answers
y_true = [0, 1, 1, 1, 0, 1, 0, 1]

#Models Predections
y_pred = [0, 1, 1, 0, 1, 1, 1, 0]

#Evaluation
print("Accuracy: ", accuracy_score(y_true, y_pred))
print("Precesion: ", precision_score(y_true, y_pred))
print("Recall: ", recall_score(y_true, y_pred))
print("F1Score: ", f1_score(y_true, y_pred))
