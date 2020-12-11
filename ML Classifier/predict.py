import tensorflow as tf
import pandas as pd
import os

categories=list(pd.read_csv('train.csv')['Category'].unique())



if not(os.path.exists("savemodel")):
	print("Train the model first")

load=tf.saved_model.load("savemodel")
infer = load.signatures["serving_default"]
input_sentence=input()

predict_raw=infer(tf.constant([input_sentence]))['dense_1']
predict=categories[int(tf.argmax(predict_raw,axis=-1))]

