import os
from flask import Flask, render_template
# Machine Learning Intial Work
from keras.models import Sequential
from keras.layers import Dense, Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
import numpy as np
import random
import json
from PIL import Image
import glob
app = Flask(__name__)

# constants
path = "scraped-sofas/*"
target_width = 64
target_height = 64

img_depth = 3
threshold = 0.9
lim = 5

imageData = ''
with open('Sofa Dictionary.txt','r') as file:
	imageData=json.loads(file.read().replace('\n',''))

# Returns pixel data as well as width
def load_image(filename):
	im = Image.open(filename)
	pixels = im.resize((target_width,target_height),Image.ANTIALIAS)
	pixels = np.asarray(im.getdata())
	pixels = pixels/255.0*2 - 1
	pixels = np.resize(pixels, (target_height, target_width, 3, 1)) #need the extra dimension to stack later
	return im, pixels

def display(n):
	return imageData[n]
 
# Fit model on training data
def train(X,Y, e):
	model.fit(X, Y, batch_size=1, nb_epoch=e)

@app.route('/',methods=['GET','POST'])
def index():
	# Machine Learning Witchcraft
	
	# grab file dimensions
	im,_ = load_image('scraped-sofas/sofa_0.jpg')

	numImages = 0

	X_test = np.empty(shape=(target_width,target_height,3,0)) #needs optimization
	for fname in glob.glob(path):
		im, pixels = load_image(fname)
		X_test = np.append(X_test, pixels, axis=3)
		numImages = numImages + 1

	X_train = X_test[:,:,:,int(numImages*random.random())]

	# Model Architecture
	model = Sequential()
	model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(target_width,target_height,img_depth)))
	model.add(Convolution2D(32, (3, 3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2,2)))

	model.add(Flatten())
	model.add(Dense(128))
	model.add(Dense(2))

	# Compile model
	model.compile(loss='mean_squared_error',
				  optimizer='adam',
				  metrics=['accuracy'])

	count = 0
	overallMax = 0
	overallImg = 0
	overallInd = 0
	list = [None]*lim
	return render_template('sofa.html')

@app.route('/submission/<num>', methods=['POST'])
def rating():
	if count<lim:
		return display(i)
		Y_train = np.full((1,1),num)
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
					overallInd = i
		if score>threshold:
			return display(i)
		list[count] = ind
		count = count+1
	else:
		return display(overallInd)
	
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
