import keras
import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation, Dense

training_data = np.array([[0,0], [0,1], [1,0], [1,1]])

target_data = np.array([[0], [1], [1], [0]])

model = Sequential()

#Create the Deep Neural Network
num_layers = 100
model.add(Dense(num_layers, input_dim=2, activation="relu"))
model.add(Dense(1))
model.compile(loss="mean_squared_error", optimizer="adam")

#Train and evaluate the data
num_epochs = 1000
model.fit(training_data, target_data, epochs=num_epochs)
model.evaluate(training_data, target_data)

#Output results
print(model.predict(np.array([[0,0]])))
