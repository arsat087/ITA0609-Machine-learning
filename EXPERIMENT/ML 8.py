from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 5, 4, 5]

model = LinearRegression()

model.fit(X, y)

pred = model.predict(X)

print("Actual Values:", y)
print("Predicted Values:", pred)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
