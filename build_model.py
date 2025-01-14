import numpy as np 
import pandas as pd
import os
import keras
from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPool2D,Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_df=pd.read_csv("Resources/train.csv")
test_df=pd.read_csv("Resources/test.csv")

train_label=train_df['label']
trainset=train_df.drop(['label'],axis=1)
X_train = trainset.values
X_train = trainset.values.reshape(-1,28,28,1)

test_label=test_df['label']
X_test=test_df.drop(['label'],axis=1)

from sklearn.preprocessing import LabelBinarizer
lb=LabelBinarizer()
y_train=lb.fit_transform(train_label)
y_test=lb.fit_transform(test_label)

X_test=X_test.values.reshape(-1,28,28,1)

train_datagen = ImageDataGenerator(rescale = 1./255, rotation_range = 0, height_shift_range=0.2, width_shift_range=0.2, shear_range=0, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest')

X_test=X_test/255

model=Sequential()
model.add(Conv2D(128,kernel_size=(5,5), strides=1,padding='same',activation='relu',input_shape=(28,28,1)))
model.add(MaxPool2D(pool_size=(3,3),strides=2,padding='same'))
model.add(Conv2D(64,kernel_size=(2,2), strides=1,activation='relu',padding='same'))
model.add(MaxPool2D((2,2),2,padding='same'))
model.add(Conv2D(32,kernel_size=(2,2), strides=1,activation='relu',padding='same'))
model.add(MaxPool2D((2,2),2,padding='same'))          
model.add(Flatten())
model.add(Dense(units=512,activation='relu'))
model.add(Dropout(rate=0.25))
model.add(Dense(units=24,activation='softmax'))
print(model.summary())
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(train_datagen.flow(X_train,y_train,batch_size=200),epochs = 35,validation_data=(X_test,y_test),shuffle=1)
(ls,acc)=model.evaluate(x=X_test,y=y_test)
print(f"Model Accuracy: {acc*100}")
model.save("Resources/SLmodel.keras")