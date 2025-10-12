from sklearn.tree import DecisionTreeClassifier


X = [
    [7, 2], #Apple
    [8, 3], #Apple
    [9, 8], #Orange
    [10, 9], #Orange
]

y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

size = float(input("Enter the size in cm: "))
shade = float(input("Enter the color shade (1-10): "))

result = model.predict([[size, shade]])[0]
if result == 0:
    print("This is likely to be an Apple")
else:
    print("This is likely to be an Orange")