from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('IOT_data_2.csv')

print(data)


plt.xlabel("pressure")
plt.ylabel("id")

#train data 및 test data 나누기
x = data[["pressure"]]
y = data[["id"]]
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8, test_size=0.2)

#예측 모델 생성
lr = LinearRegression()
lr.fit(x_train,y_train)

#정확도 측정
accuracy = lr.score(x_train,y_train)
print(accuracy)

#예측값 구하기
y_predicted = lr.predict(x_test)
mse = mean_squared_error(y_test, y_predicted)
print(mse)
print('w : ',lr.coef_,lr.intercept_)

#산포도 구해보기
plt.scatter(y_test,y_predicted, alpha=0.5)
plt.show()
