#!/usr/bin/env python

import os
import urllib.request
import matplotlib.pyplot as plt
import numpy as np

celeba = '/Users/ericliu/Developer/MachineLearning/img_align_celeba'
if not os.path.exists(celeba):
    os.mkdir(celeba)

for img_i in range(1, 11):
    f = '000%03d.jpg' % img_i
    url = 'https://s3.amazonaws.com/cadl/celeb-align/' + f
    # print(url, end='\r')
    filename = os.path.join(celeba, f)
    if not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)


files = [os.path.join(celeba, file_i)
 for file_i in os.listdir(celeba)
 if '.jpg' in file_i]

img = plt.imread(files[np.random.randint(0, len(files))])
plt.imshow(img)
plt.show()

plt.imshow(img[:,:,0])
plt.show()