import os
from ml import *
from flask import Flask, render_template
# Machine Learning Intial Work
from keras.models import Sequential
from keras.layers import Dense, Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
import numpy as np
import random
from PIL import Image
import glob
app = Flask(__name__)

path = "sofa-folder/*"
target_width = 64
target_height = 64

#Returns pixel data as well as width 
def load_image( filename ):
	im = Image.open( filename )
	im = im.resize((target_width,target_height),Image.ANTIALIAS)
	pixels = np.asarray(im.getdata())
	#pixels = pixels/255.0*2 - 1
	pixels = np.resize(pixels, (im.height, im.width, 3, 1)) #need the extra dimension to stack later
	return im, pixels

im,_ = load_image('sofa-folder/sofa.jpg')

img_width = im.width
img_height = im.height
img_depth = 3
threshold = 0.9
lim = 5
numImages = 0

def display(img):   
	return Image.fromarray(img.squeeze().astype('uint8'), 'RGB')

X_test = np.empty(shape=(target_width,target_height,3,0)) #needs optimization
for fname in glob.glob(path):
	im, pixels = load_image(fname)
	X_test = np.append(X_test, pixels, axis=3)
	numImages = numImages + 1

X_train = X_test[:,:,:,int(numImages*random.random())]

# Model Architecture
model = Sequential()
model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(img_width,img_height,img_depth)))
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
 
model.add(Flatten())
model.add(Dense(128))
model.add(Dense(2))

# Compile model
model.compile(loss='mean_squared_error',
			  optimizer='adam',
			  metrics=['accuracy'])
 
# Fit model on training data
def train(X,Y, e):
	model.fit(X, Y, batch_size=1, nb_epoch=e)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST':
	else:
        return render_template('sofa.html')

@app.route('/submission/<num>', methods=['POST'])
def rating(num=-1):
	if num == -1:
		break
		
	count = 0
	overallMax = 0
	overallImg = 0
	list = [None]*lim

	while count<lim:
		display(X_train)
		Y_train = zeros((1, 2))
		Y_train[0, round(num/10)]
		train(X_train[np.newaxis,...],Y_train)
		max_thing = 0
		ind = 0
		for i in range(0,X_test.shape[3]):
			if i not in list:
				img = X_test[:,:,:,i]
				score = model.evaluate(img[np.newaxis,...], np.zeros((1,2)), verbose=1)
				if score > max_thing:
					max_thing = score
					X_train = img
					ind = i
				if score>overallMax:
					overallMax = score
					overallImg = img
		if score>threshold:
			return display(X_train)
		list[count] = ind
		count = count+1

	return display(overallImg)
	

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
