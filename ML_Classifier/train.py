import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import os
import tarfile

#Reading dataset
df=pd.read_csv("train.csv")
categories=list(df['Category'].unique())
df.dropna()
cat_dict={categories[i]:i for i in range(39)}
df["Cat_num"]=df['Category'].map(cat_dict)

#Preprocessing
features=df["Descript"]
labels=df["Cat_num"]
datass=tf.data.Dataset.from_tensor_slices((features[:50000], labels[:50000]))

if not(os.path.exists("nnlm_model")):
	my_file=tarfile.open("nnlm-en-dim128-with-normalization_2.tar.gz")
    my_file.extractall("nnlm_model")
    my_file.close()

#Creating model

embedding=tf.saved_model.load("nnlm_model")
hub_layer = hub.KerasLayer(embedding, input_shape=[], 
                           dtype=tf.string, trainable=True)

model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dense(39, activation="softmax"))
model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(datass.shuffle(10000).batch(512),
                    epochs=10,
                    verbose=1)

tf.saved_model.save(model,"savemodel")