import cv2, os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
#import sys
#from keras.models import Sequential
#from keras.models import Model
#from keras.layers import Dense, Activation, Dropout, Flatten,Conv2D, MaxPooling2D, Input

dir_data = "dataset1/"
#dir_seg = dir_data + "/annotations_prepped_train/"
#dir_img = dir_data + "/images_prepped_train/"

dir_seg = dir_data + "/labels_train/"
dir_img = dir_data + "/images_train/"

dir_test_seg = dir_data + "/labels_test/"
dir_test_img = dir_data+"/images_test/"

## seaborn has white grid by default so I will get rid of this.
sns.set_style("whitegrid", {'axes.grid' : False})

ldseg = np.array(os.listdir(dir_seg))
## pick the first image file
fnm = ldseg[66]
print(fnm)
## read in the original image and segmentation labels
seg = cv2.imread(dir_seg + fnm ) # (360, 480, 3)
img_is = cv2.imread(dir_img + fnm )
print("seg.shape={}, img_is.shape={}".format(seg.shape,img_is.shape))

## Check the number of labels
mi, ma = np.min(seg), np.max(seg)
n_classes = 5
print("minimum seg = {}, maximum seg = {}, Total number of segmentation classes = {}".format(mi,ma, n_classes))

#fig = plt.figure(figsize=(5,5))
#ax = fig.add_subplot(1,1,1)
#ax.imshow(img_is)
#ax.set_title("original image")
#plt.show()

#fig = plt.figure(figsize=(15,10))
#for k in range(mi,ma+1):
#    ax = fig.add_subplot(1,n_classes/1,k+1)
#    ax.imshow((seg == k)*1.0)
#    ax.set_title("label = {}".format(k))
#
#
#plt.show()

import random
def give_color_to_seg_img(seg,n_classes):
    '''
    seg : (input_width,input_height,3)
    '''
    if len(seg.shape)==3:
        seg = seg[:,:,0]
    seg_img = np.zeros( (seg.shape[0],seg.shape[1],3) ).astype('float')
    colors = sns.color_palette("hls", n_classes)
   
    for c in range(n_classes):
        segc = (seg == c)
        seg_img[:,:,0] += (segc*( colors[c][0] ))
        seg_img[:,:,1] += (segc*( colors[c][1] ))
        seg_img[:,:,2] += (segc*( colors[c][2] ))

    return(seg_img)

input_height , input_width = 224 , 224
output_height , output_width = 224 , 224


ldseg = np.array(os.listdir(dir_seg))
#for fnm in ldseg[np.random.choice(len(ldseg),3,replace=False)]:
#    fnm = fnm.split(".")[0]
#    seg = cv2.imread(dir_seg + fnm + ".png") # (360, 480, 3)
#    img_is = cv2.imread(dir_img + fnm + ".png")
#    seg_img = give_color_to_seg_img(seg,n_classes)
#
#    fig = plt.figure(figsize=(20,40))
#    ax = fig.add_subplot(1,4,1)
#    ax.imshow(seg_img)
#    
#    ax = fig.add_subplot(1,4,2)
#    ax.imshow(img_is/255.0)
#    ax.set_title("original image {}".format(img_is.shape[:2]))
#    
#    ax = fig.add_subplot(1,4,3)
#    ax.imshow(cv2.resize(seg_img,(input_height , input_width)))
#    
#    ax = fig.add_subplot(1,4,4)
#    ax.imshow(cv2.resize(img_is,(output_height , output_width))/255.0)
#    ax.set_title("resized to {}".format((output_height , output_width)))
#    plt.show()

def getImageArr( path , width , height ):
        img = cv2.imread(path, 1)
        img = np.float32(cv2.resize(img, ( width , height ))) / 127.5 - 1
        return img
    
    
def getSegmentationArr( path , nClasses ,  width , height  ):

    seg_labels = np.zeros((  height , width  , nClasses ))
    img = cv2.imread(path, 1)
    img = cv2.resize(img, ( width , height ))
    img = img[:, : , 0]

    for c in range(nClasses):
        seg_labels[: , : , c ] = (img == c ).astype(int)
    ##seg_labels = np.reshape(seg_labels, ( width*height,nClasses  ))
    return seg_labels

images = os.listdir(dir_img)
images.sort()
segmentations  = os.listdir(dir_seg)
segmentations.sort()

testimages = os.listdir(dir_test_img)
testimages.sort()
testsegmentation = os.listdir(dir_test_seg)
testsegmentation.sort()

#X = []
#Y = []

P = []
Q = []



for im , seg in zip(testimages, testsegmentation):
    P.append(getImageArr(dir_test_img + im , input_width , input_height ))
    Q.append(getSegmentationArr( dir_test_seg + seg , n_classes , output_width , output_height))

P, Q = np.array(P) , np.array(Q)
print(P.shape,Q.shape)


## Import usual libraries
#from keras.layers.merge import concatenate, Add
#from keras.layers.convolutional import Conv2D, Conv2DTranspose
import sys
import tensorflow as tf
from tensorflow import keras
from keras.backend.tensorflow_backend import set_session
import keras, warnings
from keras.models import *
from keras.layers import *
from keras.callbacks import EarlyStopping
import pandas as pd 
warnings.filterwarnings("ignore")

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" 
config = tf.ConfigProto(device_count = {'CPU': 20,'GPU':1000})
config.gpu_options.per_process_gpu_memory_fraction = 0.95
config.gpu_options.visible_device_list = "0" 
set_session(tf.Session(config=config)) 
#
print("python {}".format(sys.version))
print("keras version {}".format(keras.__version__)); del keras
print("tensorflow version {}".format(tf.__version__))

#VGG_Weights_path = "./vgg_weights/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5"
#Alexnet_Weights_path = "./alexnet_weight/alexnet_weights.h5"

import keras
from keras.layers import ELU
from keras.preprocessing.image import ImageDataGenerator

def FCN8( nClasses ,  input_height=224, input_width=224):
    ## input_height and width must be devisible by 32 because maxpooling with filter size = (2,2) is operated 5 times,
    ## which makes the input_height and width 2^5 = 32 times smaller
    assert input_height%32 == 0
    assert input_width%32 == 0
    IMAGE_ORDERING =  "channels_last" 
    elu = keras.layers.ELU(alpha=1.0)

    img_input = Input(shape=(input_height,input_width, 3)) ## Assume 224,224,3

    ## Block 1
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv1', data_format=IMAGE_ORDERING )(img_input)
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv2', data_format=IMAGE_ORDERING )(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool', data_format=IMAGE_ORDERING )(x)
   # x = Dropout(0.1)(x)
    f1 = x
    
    # Block 2
    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv1', data_format=IMAGE_ORDERING )(x)
    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv2', data_format=IMAGE_ORDERING )(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool', data_format=IMAGE_ORDERING )(x)
   # x = Dropout(0.1)(x)
    f2 = x

    # Block 3
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv1', data_format=IMAGE_ORDERING )(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv2', data_format=IMAGE_ORDERING )(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv3', data_format=IMAGE_ORDERING )(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool', data_format=IMAGE_ORDERING )(x)
    #x = Dropout(0.1)(x)
    pool3 = x

    # Block 4
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv1', data_format=IMAGE_ORDERING )(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv2', data_format=IMAGE_ORDERING )(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv3', data_format=IMAGE_ORDERING )(x)
    pool4 = MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool', data_format=IMAGE_ORDERING )(x)## (None, 14, 14, 512)
    #pool4 = Dropout(0.1)(pool4) 

    # Block 5
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv1', data_format=IMAGE_ORDERING )(pool4)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv2', data_format=IMAGE_ORDERING )(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv3', data_format=IMAGE_ORDERING )(x)
    pool5 = MaxPooling2D((2, 2), strides=(2, 2), name='block5_pool', data_format=IMAGE_ORDERING )(x)## (None, 7, 7, 512)
    #pool5 = Dropout(0.1)(pool5)

    #x = Flatten(name='flatten')(x)
    #x = Dense(4096, activation='relu', name='fc1')(x)
    # <--> o = ( Conv2D( 4096 , ( 7 , 7 ) , activation='relu' , padding='same', data_format=IMAGE_ORDERING))(o)
    # assuming that the input_height = input_width = 224 as in VGG data
    
    #x = Dense(4096, activation='relu', name='fc2')(x)
    # <--> o = ( Conv2D( 4096 , ( 1 , 1 ) , activation='relu' , padding='same', data_format=IMAGE_ORDERING))(o)   
    # assuming that the input_height = input_width = 224 as in VGG data
    
    #x = Dense(1000 , activation='softmax', name='predictions')(x)
    # <--> o = ( Conv2D( nClasses ,  ( 1 , 1 ) ,kernel_initializer='he_normal' , data_format=IMAGE_ORDERING))(o)
    # assuming that the input_height = input_width = 224 as in VGG data
    
    
    vgg  = Model( img_input , pool5  )
    vgg.load_weights(VGG_Weights_path) ## loading VGG weights for the encoder parts of FCN8
    
    n = 4096
    o = ( Conv2D( n , ( 7 , 7 ) , activation='relu' , padding='same', name="conv6", data_format=IMAGE_ORDERING))(pool5)
    conv7 = ( Conv2D( n , ( 1 , 1 ) , activation='relu' , padding='same', name="conv7", data_format=IMAGE_ORDERING))(o)
    
    
    ## 4 times upsamping for pool4 layer
    conv7_4 = Conv2DTranspose( nClasses , kernel_size=(4,4) ,  strides=(4,4), use_bias=False, data_format=IMAGE_ORDERING )(conv7)
     ## (None, 224, 224, 10)
    ## 2 times upsampling for pool411
    pool411 = ( Conv2D( nClasses , ( 1 , 1 ) , activation='relu' , padding='same', name="pool4_11", data_format=IMAGE_ORDERING))(pool4)
    #changeing this layer
    pool411_2 = (Conv2DTranspose( nClasses , kernel_size=(2,2) ,  strides=(2,2), use_bias=False, data_format=IMAGE_ORDERING ))(pool411) 
    
    pool311 = ( Conv2D( nClasses , ( 1 , 1 ) , activation='relu' , padding='same', name="pool3_11", data_format=IMAGE_ORDERING))(pool3)
        
    o = Add(name="add")([pool411_2, pool311, conv7_4 ])
    o = Conv2DTranspose( nClasses , kernel_size=(8,8) ,  strides=(8,8) , use_bias=False, data_format=IMAGE_ORDERING )(o)
    o = (Activation('softmax'))(o)
    
    model = Model(img_input, o)

    return model


#model = FCN8(nClasses = n_classes, input_height = 224, input_width  = 224)
#print(model.summary())

#keras.utils.plot_model(model, './modelArchitecture.png', show_shapes=True)

import sys


from sklearn.utils import shuffle
#train_rate = 0.85
#index_train = np.random.choice(X.shape[0],int(X.shape[0]*train_rate),replace=False)
#index_test  = list(set(range(X.shape[0])) - set(index_train))
                            
#X, Y = shuffle(X,Y)
#X_train, y_train = X[index_train],Y[index_train]
#X_val, y_val = X[index_test],Y[index_test]
#print(X_train.shape, y_train.shape)
#print(X_val.shape, y_val.shape)


from keras import optimizers
from keras.callbacks import LearningRateScheduler
from keras.models import load_model
#from tensorflow.python.keras.optimizer_v2 import rmsprop


#bayasian = rmsprop.RMSProp(learning_rate=lr)
# learning rate schedule
#def step_decay(epoch):
#	initial_lrate = 0.1
#	drop = 0.5
#	epochs_drop = 10.0
#	lrate = initial_lrate * math.pow(drop, math.floor((1+epoch)/epochs_drop))
#	return lrate



#adam = optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False)
sgd = optimizers.SGD(lr=0.14,clipnorm=1., decay=5**(-4), momentum=0.9, nesterov=True)

#adagard = optimizers.Adagrad(lr=0.01)
#adadelta = optimizers.Adadelta(lr=0.2, rho=0.95, epsilon=1e-6)
#adamax = optimizers.Adamax(lr=0.004, beta_1=0.9, beta_2=0.999)
#adam = optimizers.Adam(lr=0.001)



# learning schedule callback
#lrate = LearningRateScheduler(step_decay)
#callbacks_list = [lrate]

#datagen.fit(X_train)



#for e in range(epochs):
#    batches = 0
#    for x_batch, y_batch in datagen.flow(X_train, y_train, batch_size=batch_size):
        #x_batch = np.reshape(x_batch, [-1, input_height])
#        hist1 = model.fit(x_batch, y_batch,validation_data=(X_val,y_val), verbose=2)
        #loss.append(hist1.history['loss'])
        #val_loss.append(hist1.history['val_loss'])
#        batches += 1
#        print("Epoch %d/%d, Batch %d/%d" % (e+1, epochs, batches, max_batches))
#        if batches >= max_batches:
            # we need to break the loop by hand because
            # the generator loops indefinitely
#            break
#    loss.append(hist1.history['loss'])
#    val_loss.append(hist1.history['val_loss'])
#    acc.append(hist1.history['accuracy'])
#    val_acc.append(hist1.history['val_accuracy'])


#es = EarlyStopping(monitor='val_loss', mode='min', verbose=1,patience=100)

#training_start_time = time.time()

#hist1 = model.fit(X_train,y_train,
#                  validation_data=(X_val,y_val),
#                  batch_size=64,epochs=200,verbose=2,use_multiprocessing=True,workers=80,callbacks=[es])

#training_end_time = time.time()

#model.save('model_sgd_64_lr_014.h5') 
model = load_model('model_sgd_64_lr_014.h5',compile=False)

model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

#print("Loss list ",loss)
#print("val_loss ",val_loss)


#f = open('acclossresult.txt', 'w')
#sys.stdout = f
#print("Loss list ",loss)
#print("val_loss ",val_loss)
#print("\n")
#print("Accuracy list ",acc)
#print("val_accuracy ",val_acc)
#sys.stdout = orig_stdout
#f.close()

start_tt = time.time() 
scores = model.evaluate(P, Q, verbose=1)
end_tt = time.time()
orig_stdout = sys.stdout
f = open('PredTime.txt', 'a')
#sys.stdout = f
#print('Test loss:', scores[0])
#print('Test accuracy:', scores[1])
f.write('{0}\n'.format(end_tt-start_tt))
#sys.stdout = orig_stdout
f.close()

#hist1 = model.fit(X_train,y_train,
#                  validation_data=(X_val,y_val),
#                  batch_size=32,epochs=200,verbose=2)


#import sys
#sys.exit()


#orig_stdout = sys.stdout
#f = open('ModelEvalTrain.txt', 'w')
#sys.stdout = f
#print(model.evaluate(X_train,y_train,batch_size=32,verbose=1))
#sys.stdout = orig_stdout
#f.close()


#orig_stdout = sys.stdout
#f = open('ModelEvalTest.txt', 'w')
#sys.stdout = f
#print(model.evaluate(P,Q,batch_size=32,verbose=1))
#sys.stdout = orig_stdout
#f.close()

#print(hist1.history.keys())


#for key in ['loss', 'val_loss']:
#    plt.plot(hist1.history[key],label=key)
#plt.legend()
#plt.xlabel('epoch' ,fontsize=14)
#plt.ylabel('loss',fontsize=14)
#plt.show()
#plt.savefig("loss.pdf")


#calculate intersection over union for each segmentation class
X_test = P
y_test = Q
y_pred = model.predict(X_test)
#print(" Predict result : ",y_pred)
y_predi = np.argmax(y_pred, axis=3)
y_testi = np.argmax(y_test, axis=3)

#print(y_testi.shape,y_predi.shape)

f = open("ResultFCN8.txt", "a")
def IoU(Yi,y_predi):
    ## mean Intersection over Union
    ## Mean IoU = TP/(FN + TP + FP)

    IoUs = []
    #PixAcc = []
    Nclass = int(np.max(Yi)) + 1
    for c in range(Nclass):
        TP = np.sum( (Yi == c)&(y_predi==c) )
        FP = np.sum( (Yi != c)&(y_predi==c) )
        FN = np.sum( (Yi == c)&(y_predi != c))
        TN = np.sum( (Yi != c)&(y_predi !=c)) 
        IoU = TP/float(TP + FP + FN)
        PixAcc = (TP+TN)/float(TP + TN + FP + FN)
        print("class {:02.0f}: #TP={:6.0f}, #FP={:6.0f}, #FN={:5.0f}, IoU={:4.3f}, PixelAccuracy = {:4.3f}".format(c,TP,FP,FN,IoU,PixAcc))
        f.write("class {:02.0f}: #TP={:6.0f}, #FP={:6.0f}, #FN={:5.0f}, IoU={:4.3f}, PixelAccuray={:4.3f}\n".format(c,TP,FP,FN,IoU,PixAcc)) 
        IoUs.append(IoU)
        #PixAcc.append(PixAcc)
    mIoU = np.mean(IoUs)
    #mPA = np.mean(PixAcc)
    print("_________________")
    f.write("_________________")
    print("Mean IoU: {:4.3f} ".format(mIoU))
    f.write("Mean IoU: {:4.3f}".format(mIoU))
    #f.write("Training Time :{0}\n".format(training_end_time-training_start_time ))

IoU(y_testi,y_predi)



