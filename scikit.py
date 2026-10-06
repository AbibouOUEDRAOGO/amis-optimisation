from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [8, 10, 12, 15, 17]
modele = LinearRegression()

modele.fit(X, y)

resultat = modele.predict([[6]])
print(resultat)