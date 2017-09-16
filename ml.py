# Machine Learning Intial Work

from keras.models import Sequential
from keras.layers import Dense, Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
import numpy as np

img_width = 128
img_height = 128
 
# Format input data
X_train = X_train.reshape(X_train.shape[0], 1, img_width, img_height)
X_train = X_train.astype('float32')
 
# Model Architecture
model = Sequential()

model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(1,img_width,img_height)))
model.add(Convolution2D(32, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
 
model.add(Flatten())
model.add(Dense(128))
model.add(Dense(128))

# Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
# Fit model on training data
model.fit(X_train, Y_train, 
          batch_size=1, nb_epoch=3, verbose=1)
 
# Evaluate model on test data
score = model.evaluate(X_test, Y_test, verbose=0)
