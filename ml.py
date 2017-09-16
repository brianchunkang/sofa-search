# Machine Learning Intial Work
from keras.models import Sequential
from keras.layers import Dense, Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
import numpy as np
import random
from PIL import Image

#Returns pixel data as well as width 
def load_image( filename ):
    im = Image.open( filename )
    pixels = np.asarray(im.getdata(), dtype=float)
    pixels = pixels/255.0*2 - 1
    pixels = np.resize(pixels, (im.width, im.height))
    return im, pixels

im, pixels = load_image('sofa-folder/sofa.jpg')
show(im)

img_width = im.width
img_height = im.height
img_depth = 3
threshold = 0.9
lim = 20
 
# Format input data
'''
for img in X_test:
    img = img.reshape(img.shape[0], 1, img_width, img_height)
    img = img.astype('float32')
'''
X_train = X_test[int(len(X_test)*random.random())]

# Model Architecture
model = Sequential()
model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(img_width,img_height,img_depth)))
model.add(Convolution2D(32, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
 
model.add(Flatten())
model.add(Dense(128))
model.add(Dense(1))

# Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
# Fit model on training data
def train(X,Y):
    model.fit(X, Y, batch_size=1, nb_epoch=3, verbose=1)

def display(img):
    new = Image.fromarray(img,'RGB')
    new.save('out.png')
    new.show()
    
def getInput:
    return input('Score: ')

count = 0
overallMax = 0
overallImg = 0

while count<lim:
    display(X_train)
    Y_train = np.empty([1,1])
    np[0][0] = getInput()
    train(X_train,Y_train)
    max_thing = 0
    for img in X_test:
        score = model.evaluate(img, verbose=0)
        if score>max_thing:
            max_thing = score
            X_train = img
        if score>overallMax
            overallMax = score
            overallImg = img
    if score>threshold
        return X_train
return overallImg