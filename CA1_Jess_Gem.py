import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils.np_utils import to_categorical
import random
import requests
from PIL import Image
import cv2
import pickle
import pandas as pd
import csv
import torchvision.datasets as datasets
import torch.utils.data as data

def grayscale(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image

# Brightens the Image
def equalize(image):
    # Only works on grayscaled images
    image = cv2.equalizeHist(image)
    return image

def preprocessing(image):
    image = grayscale(image)
    image = equalize(image)
    #flatten Image
    image = image/255
    return image

DATA = "F:\College\Year 4\Smart Tech\JessicaSavage_GemmaRegan_SmartTech_CA1/tiny-imagenet-200"
VAL_ANNOTATIONS_PATH = "F:\College\Year 4\Smart Tech\JessicaSavage_GemmaRegan_SmartTech_CA1/tiny-imagenet-200/val/val_annotations.txt"
VAL_PATH = "F:/College/Year 4/Smart Tech/JessicaSavage_GemmaRegan_SmartTech_CA1/tiny-imagenet-200/val/images"
TRAIN_PATH = "F:/College/Year 4/Smart Tech/JessicaSavage_GemmaRegan_SmartTech_CA1/tiny-imagenet-200/train"
# TEST_PATH = "F:\College\Year 4\Smart Tech\JessicaSavage_GemmaRegan_SmartTech_CA1/tiny-imagenet-200/test"
WNIDS_PATH = "F:\College\Year 4\Smart Tech\JessicaSavage_GemmaRegan_SmartTech_CA1/tiny-imagenet-200/wnids.txt"
# WORDS_PATH = "F:\College\Year 4\Smart Tech\JessicaSavage_GemmaRegan_SmartTech_CA1/tiny-imagenet-200/words.txt"
# num_classes=200


# LOAD WNIDS INTO ARRAY
WNIDS = open(os.path.join(DATA, 'wnids.txt'), 'r')
WNIDS_file = WNIDS.readlines()
WNIDS_data = []
for line in WNIDS_file:
    words = line.split('\t')
    WNIDS_data.append(words)
WNIDS.close()

# LOAD VALIDATION DATA
val_data = []
for filename in os.listdir(VAL_PATH):
    f = os.path.join(VAL_PATH,filename)
    if os.path.isfile(f):
        val_data.append(f)

#print(val_data[1])
#img = cv2.imread(val_data[4])
#plt.imshow(img)
#plt.show()


# LOAD VALIDATION DATA
#val_dataset = datasets.ImageFolder(VAL_PATH)
#print("VALIDATION DATASET SIZE", len(val_dataset))

#LOAD IN DATA FROM WNIDS TEXT FILE
with open(WNIDS_PATH, "r") as file:
    wnids = file.read()
# Directory to datasets
TRAIN = os.path.join(DATA, 'train')
VAL = os.path.join(DATA, 'val')
TEST = os.path.join(DATA, 'test')

#PAIR EACH WNIDS NUMBER TO AN INTERGER I.E. {n08966554 : 1, n0897856 : 2} etc.
pair = {}
for i, wnid in enumerate(wnids): #Loop through and assign label
    pair[wnid] = i
val_annotations = open(os.path.join(VAL, 'val_annotations.txt'), 'r')
val_file = val_annotations.readlines()

val_data = {}
for line in val_file:
    words = line.split('\t')
    val_data[words[0]] = words[1]
val_annotations.close()

#print(label_data)

#Use words.txt to get names for each class  #not working fully
# with open(WORDS_PATH, 'r') as f:
#     wnid_to_words = dict(line.split('\t') for line in f)
#     for wnid, words in wnid_to_words.items():
#       wnid_to_words[wnid] = [w.strip() for w in words.split(',')]
# class_names = [wnid_to_words[wnid] for wnid in wnids]

