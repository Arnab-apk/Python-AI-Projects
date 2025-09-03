#import libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical

#load the mnistdataset
(train_images, train_labels),(test_images,test_lables)=datasets.mnist.load_data()

#preprovessing: Normalise the pixel value to be between 0 and 1
train_images=train_images/255.0
train_images=test_images/255.0

#reshape the images
