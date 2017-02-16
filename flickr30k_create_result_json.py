# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 00:23:50 2017

@author: samhi

Create result json to measure the scores
"""

import json
import sys, os
from pprint import pprint
import codecs
from random import randint

sys.path.append('/home/samhi/Desktop/coco_helpers/')

fileNameJson = 'vis.json'
TOTAL_TEST_FILES = 1000 # flicker = 1000 
BASELINE_CAPTION_COUNT = 5 # 

# ARRANGE BELOW PATHS ACCORDINGLY
main_path = '/home/samhi/Vision/Datasets/flickr8k/' # path to flickr8k test image names
res_json_path = '/home/samhi/neuraltalk2-master/coco-caption/coco-caption-master/results/' # path to output folder
main_res_path = '/home/samhi/Vision/results/test_results/'  # path to vis.json folder


# read json file, karpathy's result vis.json
with open(main_res_path + fileNameJson) as data_file:    
    data = json.load(data_file)
    
# read test file names
f = codecs.open(main_path + 'Flickr_8k.testImages.txt', "r", "utf-8") # for flicker
#f = codecs.open(main_path + 'val_file_names.txt', "r", "utf-8") # for mscoco
file_names_test = f.read().splitlines()

file_names_test_duzgun = []
for test_file in file_names_test:
    xxx = test_file.split("_")
    file_names_test_duzgun.append(xxx[0] + '.jpg')


# bazi degerleri sabit verelim, bunlar ise yaramayanlar olsun.
license_ = 3
url_ = 'asdasdsda.com'
width_ = 640
height_ = 480
date_captured = 14

ims = []
anns = []

id_ = 0

for i in range(TOTAL_TEST_FILES): #for i in range(total_images_en):
    
    # first find the index
    f_name_ = data[i]['file_name'].split('/')[-1]
    #print f_name_
    id_ = (file_names_test_duzgun.index(f_name_))
    anns_elem = str(id_) + ',' + str(data[i]['caption'])
    anns.append(anns_elem)    
    
   
d = [{'image_id':elem.split(',')[0],"caption":elem.split(',')[1]} for elem in anns]
      

json.dump(d, open(res_json_path + 'flicker_val_res.json', 'w'))