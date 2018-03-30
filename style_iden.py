#coding=UTF-8
import matlab.engine
import cPickle as pickle
import numpy as np
import argparse


class_str = ['casual', 'chic', 'classic', 'clear', 'coolCasual', 'dandy',
       'dynamic', 'elegant', 'gorgeous', 'modern', 'natural', 'pretty',
       'romantic']


def get_lab_hist(img_file , out_file = "out.txt"):
    eng = matlab.engine.start_matlab()
    img_list = list()
    img_list.append(img_file)
    res = eng.lab_hist(img_list , out_file)
    res = np.array(res)
    return res

def classify(clf , feat):
    pred = clf.predict(feat)
    return class_str[pred[0]]


ap = argparse.ArgumentParser()
ap.add_argument("-i" , "--image" , required = True , help = "Path to the target image")
ap.add_argument("-m" , "--model" , required = True , default = "./svm_model.dat" ,help = "Path to the trained model")
args = vars(ap.parse_args())


clf = pickle.load(open(args["model"] , "rb"))
feat = get_lab_hist(args["image"])
print classify(clf , feat)