from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

hours = float(input("Enter how many hours studied = "))

result = model.predict([[hours]])[0]

if result == 1:
    print(f"Based on hours {hours} you are likely to PASS ")
else:
    print(f"Based on hours {hours} you are likely to FAIL ")