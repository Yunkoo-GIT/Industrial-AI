from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('IOT_data_2.csv')

print(data)


X = data[["EC1"]]
y = data[["pressure"]]

model = LinearRegression()
model.fit(X, y.values.reshape(-1,1))

print('기울기 =', model.coef_)
print('절편 =', model.intercept_)

y_pred = model.predict(X.values.reshape(-1,1))

plt.xlabel("EC1")
plt.ylabel("pressure")
plt.plot(X, y, 'o')
plt.plot(X, y_pred, color='red')
plt.show()
