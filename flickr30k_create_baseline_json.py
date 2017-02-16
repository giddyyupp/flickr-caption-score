# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:22:23 2017

@author: samhi

find test images in the flickr8k dataset, and create a baseline json file.
"""


import json
import codecs
from random import randint

TOTAL_CAPTIONS_FOR_AN_IMAGE = 5 # total captions for an image in the dataset

# ARRANGE BELOW PATHS ACCORDINGLY
flicker8kTestImages = '/home/samhi/Vision/Datasets/flickr8k/Flickr8k_text/Flickr_8k.testImages.txt'
fileNameCaps = '/home/samhi/Vision/Datasets/flickr30k/flicker30k_text/flicker30k_caps.txt'
flicker30kImageNames = '/home/samhi/Vision/Datasets/flickr30k/flicker30k_text/flicker30k_file_names.txt' 
output_path = '/home/samhi/Vision/Datasets/flickr8k/'

#pprint(len(data["annotations"]))
f = codecs.open(flicker30kImageNames, "r", "utf-8")
file_names = f.read().splitlines()

f = codecs.open(flicker8kTestImages, "r", "utf-8")
file_names_test = f.read().splitlines()


file_names_test_duzgun = []
for test_file in file_names_test:
    xxx = test_file.split("_")
    file_names_test_duzgun.append(xxx[0] + '.jpg')

# now load captions. we will use en captions to get index which ll 
# in turn used to match images and captions
f = codecs.open(fileNameCaps, "r", "utf-8")
caps_tr = f.read().splitlines()

total_images = len(caps_tr)

# lets give fixed values to mandatory fields
license_ = 3
url_ = 'asdasdsda.com'
width_ = 640
height_ = 480
date_captured = 14

out_json_tr = []
captions_tr = []
ims = []
anns = []
#captions_en = []
current_converted = int(total_images / 5)
offset = 0
found = 0
id_ = 0
index_ = 0

for i in range(current_converted): #for i in range(total_images_en):
    
    im_file_name_flicker30k = file_names[offset]   
    
    # now search the current image in the test images  
    for j in range(len(file_names_test_duzgun)):
        if file_names_test_duzgun[j] == im_file_name_flicker30k:
            found = 1
            break
            
    # if we found a test image in the flicker test images
    if found == 1:
        ims_elem = str(license_) + ',' + str(url_) + ',' + str(file_names_test_duzgun[j]) + ',' +str(id_) + ',' +str(width_) + ',' +str(date_captured) + ',' +str(height_)
        ims.append(ims_elem)
        for k in range(TOTAL_CAPTIONS_FOR_AN_IMAGE):
            anns_elem = str(j) + ',' + str(randint(4000,9000)) + ',' + str(caps_tr[offset + k])
            anns.append(anns_elem)
        
        id_ +=1
            
    found = 0
    offset += 5
    print offset

d = {"images":[{'license':elem.split(',')[0],"url":elem.split(',')[1],"file_name":elem.split(',')[2],"id":str(elem.split(',')[3]),"width":elem.split(',')[4],"date_captured":elem.split(',')[5],"height":elem.split(',')[6]} for elem in ims],
      "annotations": [{'image_id':str(elem.split(',')[0]),"id":elem.split(',')[1],"caption":elem.split(',')[2]} for elem in anns] }
      
# actually it is the test baseline
json.dump(d, open(output_path + './flickr30k_val_baseline.json', 'w'))