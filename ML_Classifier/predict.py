<<<<<<< HEAD:ML_Classifier/predict.py
import tensorflow as tf
import pandas as pd
import os


def pred(string_s):

	categories=list(pd.read_csv('train.csv')['Category'].unique())
	if not(os.path.exists("savemodel")):
		print("Train the model first")

	load=tf.saved_model.load("savemodel")
	infer = load.signatures["serving_default"]
	input_sentence=string_s

	predict_raw=infer(tf.constant([input_sentence]))['dense_4']
	predict=categories[int(tf.argmax(predict_raw,axis=-1))]
	##PREDICT IS THE FINAL OUTPUT##
	return(predict)
=======
import tensorflow as tf
import pandas as pd
import os

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
	return precit_list
>>>>>>> 9733d38a951e3b808e16958801ec8c69d754a721:ML Classifier/predict.py
