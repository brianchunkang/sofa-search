# Image import and preprocessing

from PIL import Image
import numpy as np

def load_image( filename ) :
    im = Image.open( filename )
    #img.load()
    #img.show()
    pixels = np.asarray(im.getdata(), dtype=float)
    pixels = pixels/255.0*2 - 1
    pixels = np.resize(pixels, (im.width, im.height))
    #data = (data*2.0/255.0)-1
    return pixels, im.width, im.height

pixels, width, height = load_image('sofa.jpg')