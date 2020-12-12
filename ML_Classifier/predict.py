import tensorflow as tf
import pandas as pd
import os


#def pred(string_s):
#
###		print("Train the model first")
#
#	load=tf.saved_model.load("savemodel")
#	infer = load.signatures["serving_default"]
####predict=categories[int(tf.argmax(predict_raw,axis=-1))]
	##PREDICT IS THE FINAL OUTPUT##
	#return(predict)
#=======
def predict(input_sentence):

    categories=list(pd.read_csv('train.csv')['Category'].unique())
    precit_list =[]
    if not(os.path.exists("savemodel")):
          print("Train the model first")

    load=tf.saved_model.load("savemodel")
    infer = load.signatures["serving_default"]

    for i in input_sentence:
	    predict_raw=infer(tf.constant([i]))['dense_4']
	    predict=categories[int(tf.argmax(predict_raw,axis=-1))]
	    precit_list.append(predict)
    return(precit_list)
	

