# Importing libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as lr
from sklearn.metrics import mean_squared_error as mse, r2_score as r2

apartments = pd.read_csv('BakuApartmentData.csv', index_col='Unnamed: 0')
apartments.rename_axis('No')
apartments['floor'] = apartments['floor'].str.split('/').str[0]
apartments['floor'].head()
apartments['floor'] = apartments['floor'].astype('int64')

# Target variable (y) = Price
# Independent variables (x) = rooms, floor, new_building
x = apartments[['rooms','floor','new_building']]
y = apartments['price']
# Spliting data for training and testing
x_train, x_test, y_train, y_test = tts(x,y,test_size=0.2)
# creating the model
model = lr()
# fitting the training data to teach the model
model.fit(x_train, y_train)

predictions = model.predict(x_test)
r2 = r2(y_test,predictions)
r2
coef = model.coef_
coef
intercep = model.intercept_
intercep

# This tells you how far off, on average, your model's predictions are from the actual values. A lower MAE is better.
from sklearn.metrics import mean_absolute_error as mae
mae = mae(y_test,predictions)
mae
# MSE is another common evaluation metric. It squares the differences between the actual and predicted values, making larger errors more significant.
mse = mse(y_test,predictions)
mse

# visualizing
import matplotlib.pyplot as plt
plt.scatter(y_test,predictions)
plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()])
plt.xlabel('Actual prices')
plt.ylabel('Predicted prices')
plt.show()

scaled_actual = y_test/100000
scaled_predictions = predictions/100000
plt.scatter(scaled_actual,scaled_predictions,color='green', alpha=0.5)
plt.plot([scaled_actual.min(),scaled_actual.max()],[scaled_predictions.min(),scaled_predictions.max()], color='red', alpha=1)
plt.xlabel('Actual prices (in hundred thounsands)')
plt.ylabel('Predicted prices (in hundred thousands)')
plt.show()
