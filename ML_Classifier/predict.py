import tensorflow as tf
import pandas as pd
import numpy as np
import os
def predict2(input_sentence):
	categories=list(pd.read_csv('train.csv')['Category'].unique())
	if not(os.path.exists("savemodel")):
		print("Train the model first")

	predict_list =[]
	load = tf.saved_model.load('savemodel')
	infer = load.signatures["serving_default"]

	#for i in input_sentence:
	print(input_sentence)
	for i in input_sentence:
		predict_raw=infer(tf.constant([i]))['dense_1']
		predict=categories[int(tf.argmax(predict_raw,axis=-1))]
		print(predict)
		predict_list.append(predict)
	return predict_list
