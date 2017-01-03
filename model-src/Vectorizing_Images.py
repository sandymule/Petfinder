
# coding: utf-8

# # Obtaining Vectors for Test Set

# In[1]:

import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Activation, Dropout, Flatten, Dense
import cv2
import os

base_model = load_model('./VGG/base_model.h5')
top_model = load_model('./VGG/top_model.h5')


import os


ADOPT_PATH = "./AdoptionPictures/Everything/"


# In[45]:

activation_vectors = []

images = []
for idx, filename in enumerate(os.listdir(ADOPT_PATH)):
    if idx > 3000:
        break
    img = cv2.resize(cv2.imread(ADOPT_PATH + str(idx+1) + '.png'), (150, 150)).astype(np.float32)

    img[:,:,0] -= 103.939
    img[:,:,1] -= 116.779
    img[:,:,2] -= 123.68
    img = img.transpose((2,0,1))
    images.append(img)
    
images = np.array(images)
bottleneck_features_test = base_model.predict(images)

train_data = np.load(open('./VGG/bottleneck_features_train.npy'))
test_model = Sequential()
test_model.add(Flatten(input_shape=train_data.shape[1:]))
test_model.add(Dense(256, activation='sigmoid', weights=top_model.layers[1].get_weights()))

activation_vectors = test_model.predict(bottleneck_features_test)


np.save("adoptable_array1", activation_vectors)



