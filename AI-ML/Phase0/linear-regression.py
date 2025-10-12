from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [40, 50, 65, 75, 90]

model = LinearRegression()

model.fit(X, y)

#Taking input from User
hours = float(input("Enter how many hours you studied = "))

predicted_marks = model.predict([[hours]])

print(f"Based on hours {hours} you may score around {predicted_marks}")
