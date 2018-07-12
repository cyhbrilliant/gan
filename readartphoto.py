# import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import h5py

Input =[]
for i in range(806):
    print(i)
    tempimg = cv2.imread('Artphoto/'+str(i)+'.jpg')
    tempimg=cv2.resize(tempimg,(64,64))
    tempimg=cv2.cvtColor(tempimg,cv2.COLOR_BGR2RGB)
    tempimg=(tempimg/255.)*2.-1.
    # plt.imshow(tempimg)
    # plt.show()
    Input.append(tempimg)
Input=np.array(Input)
print('OK')
file = h5py.File('art806.h5','w')
file.create_dataset('Input', data = Input)