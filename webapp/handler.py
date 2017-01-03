"""
Request Handlers
"""

import tornado.web
from tornado import concurrent
from tornado import gen
from concurrent.futures import ThreadPoolExecutor

import json
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Activation, Dropout, Flatten, Dense
import cv2
import os
import uuid

with open('app/model/dog_recommendations.json', 'rb') as infile:
    dog_recommendations = json.load(infile)

with open('app/static/adoptable_info/city_df.json', 'rb') as infile:
    city_info = json.load(infile)

with open('app/static/adoptable_info/source_df.json', 'rb') as infile:
    source_info = json.load(infile)

base_model = load_model('app/model/base_model.h5')
top_model = load_model('app/model/top_model.h5')

train_data = np.load(open('app/model/bottleneck_features_train.npy'))
test_model = Sequential()
test_model.add(Flatten(input_shape=train_data.shape[1:]))
test_model.add(Dense(256, activation='sigmoid', weights=top_model.layers[1].get_weights()))

adoptable_array = np.load("app/model/adoptable_array.npy")
from sklearn.neighbors import NearestNeighbors
neigh = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='cosine')
neigh.fit(adoptable_array)
print "done"

def recommend_pets(filename):
    
    activation_vectors = []
    ADOPT_PATH = "app/static/img/"
    images = []
    
    img = cv2.resize(cv2.imread(ADOPT_PATH + filename), (150, 150)).astype(np.float32)
    img[:,:,0] -= 103.939
    img[:,:,1] -= 116.779
    img[:,:,2] -= 123.68
    img = img.transpose((2,0,1))
    images.append(img)
    
    images = np.array(images)
    print images.shape
    bottleneck_features_test = base_model.predict(images)
    activation_vectors = test_model.predict(bottleneck_features_test)
    
    adoptable_cos = []
    dist_cos, ind_cos = neigh.kneighbors(activation_vectors, n_neighbors = 6)
    adoptable_cos.extend(ind_cos)
    
    import json
    dog_vectors = [list(dog_vec) for dog_vec in adoptable_cos]
    
    recs = []
    
    for num in dog_vectors[0]:
        recs.append(int(num) + 1)
    

    recommend_images = []
    for pic in recs:
        pic_name = str(pic) + '.png'
        pic_city = city_info.get(str(pic), "")
        pic_source = source_info.get(str(pic), "")
        recommend_images.append((pic_name, pic_city, pic_source))
    
    return recommend_images

class IndexHandler(tornado.web.RequestHandler):
    """APP is live"""

    def get(self):
        images = [
            ["1.png", "2.png", "3.png", "4.png"],
            ["5.png", "6.png", "7.png", "8.png"],
            ["9.png", "10.png", "11.png", "12.png"],
            ["13.png", "14.png", "15.png", "16.png"],
            ["17.png", "18.png", "19.png", "20.png"]
        ]
        self.render("templates/index.html", images=images)

    def post(self):
        fileinfo = self.request.files["photo"][0]
        fname = fileinfo["filename"]
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        with open("app/static/img/" + cname, "wb") as fh:
            fh.write(fileinfo["body"])

        upload_recs = recommend_pets(cname)
        print(upload_recs)
        return self.render("templates/recommended-pets.html", images=[upload_recs])

    def head(self):
        self.finish()

class RecommendHandler(tornado.web.RequestHandler):
    """APP is live"""

    def post(self):
        images = json.loads(self.get_argument("images"))
        images_idx = []
        for image in images:
            image_filename = image.split("/")[-1]
            image_idx = image_filename.split(".")[0]
            images_idx.append(int(image_idx))
        recs = []
        for image_idx in images_idx:
                recs.append(dog_recommendations[image_idx - 1])
        ranked_recs = zip(*recs)
        flattened_recs = []
        for items in ranked_recs:
            for item in items:
                temp = item + 1
                flattened_recs.append(temp)
        recommend_images = []
        for pic in flattened_recs:
            pic_name = str(pic) + '.png'
            pic_city = city_info.get(str(pic), "")
            pic_source = source_info.get(str(pic), "")
            recommend_images.append((pic_name, pic_city, pic_source))

        print(recommend_images)
        rec_images_2d = []
        rec_row = []
        for idx, image in enumerate(recommend_images):
            if idx % 6 == 0 and idx > 0:
                rec_images_2d.append(rec_row)
                rec_row = []
            elif idx == len(recommend_images)-1:
                rec_row.append(image)
                rec_images_2d.append(rec_row)
                rec_row = []
            else:
                rec_row.append(image)
        return self.render("templates/recommended-pets.html", images=rec_images_2d)
