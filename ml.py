# Machine Learning Intial Work
from keras.models import Sequential
from keras.layers import Dense, Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
import numpy as np
import random
from PIL import Image
import glob

path = "sofa-folder/*.jpg"
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

im, X_test = load_image('sofa-folder/sofa.jpg')

img_width = im.width
img_height = im.height
print(img_width)
print(img_height)
img_depth = 3
threshold = 0.9
lim = 20
numImages = 0

def display(img):
	#img = (1+img)*255/2
	print(img.shape)    
	new = Image.fromarray(img.squeeze().astype('uint8'), 'RGB')
	new.save('out.png')
	new.show()

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
model.add(Dense(1))

# Compile model
model.compile(loss='mean_squared_error',
			  optimizer='adam',
			  metrics=['accuracy'])
 
# Fit model on training data
def train(X,Y):
	model.fit(X, Y, batch_size=1, nb_epoch=100)

count = 0
overallMax = 0
overallImg = 0

while count<lim:
	display(X_train)
	Y_train = np.full((1,1),input('Score: '))
	train(X_train[np.newaxis,...],Y_train)
	max_thing = 0
	for i in range(0,X_test.shape[3]):
		img = X_test[:,:,:,i]
		print(img.shape)
		score = model.evaluate(img[np.newaxis,...], np.zeros((1,1)), verbose=1)
		if score>max_thing:
			max_thing = score
			X_train = img
		if score>overallMax:
			overallMax = score
			overallImg = img
	if score>threshold:
		display(X_train)

display(overallImg)