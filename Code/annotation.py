# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:12:24 2019

@author: Sonu
"""

import pandas as pd
from collections import OrderedDict
import os


#Function to create a new csv file with the images,bbox coordinate and total bboxes in that image
def create_new_csv(filename):
    df= pd.read_csv(filename)
    
    #Creating a dictionary out of the image as key and the total bboxes in it as value
    unordered_dictionary=dict(df['Name'].value_counts())
    #print(unordered_dictionary)
    
    #Creating a ordered dicctionary using the name of the image as the key
    dictionary=OrderedDict(sorted(unordered_dictionary.items()), key=lambda x:x[0])
    dictionary.popitem()
    
    #print(dictionary)
    
    #Appending head count to a list
    count=list()
    for k,v in dictionary.items():
        for i in range(v):
            count.append(v)
        
    df['headcount']=count   
    
    #Creating a new csv file with the images,bboxes and labels
    df.to_csv('image_bbox_label.csv', index=False)
    
    
create_new_csv(r'bbox_train.csv')   

df= pd.read_csv('image_bbox_label.csv')

data = pd.DataFrame()
data['format'] = df['Name']

df['xmin']=df['xmin'].astype(str)
df['ymin']=df['ymin'].astype(str)
df['xmax']=df['xmax'].astype(str)
df['ymax']=df['ymax'].astype(str)
df['headcount']=df['headcount'].astype(str)
print(df.dtypes)

# as the images are in train_images folder, add train_images before the image name
for i in range(data.shape[0]):
    data['format'][i] = r'image_data/{}'.format(data['format'][i])

# add xmin, ymin, xmax, ymax and class as per the format required
for i in range(data.shape[0]):
    data['format'][i] = data['format'][i] + ',' + df['xmin'][i] + ',' + df['ymin'][i] + ',' + df['xmax'][i] + ',' + df['ymax'][i] + ',' + df['headcount'][i]

data.to_csv('annotate.txt', header=None, index=None, sep=' ')

