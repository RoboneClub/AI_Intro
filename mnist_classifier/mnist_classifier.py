import numpy as np
import tensorflow as tf
import tensorflow.keras.layers as layers
import tensorflow.keras.models as models

## Dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0
x_train, x_test = np.expand_dims(x_train, axis=-1), np.expand_dims(x_test, axis=-1)


try:
    model = models.load_model("mnist_classifier.h5")

except:
    ## Model
    inputs = layers.Input(shape=(28, 28, 1))
    conv1 = layers.Conv2D(32, (3, 3), padding="valid", activation=tf.nn.relu)(inputs)
    pool1 = layers.MaxPool2D((2, 2), (2, 2))(conv1)
    conv2 = layers.Conv2D(64, (3, 3), padding="valid", activation=tf.nn.relu)(pool1)
    pool2 = layers.MaxPool2D((2, 2), (2, 2))(conv2)
    conv3 = layers.Conv2D(128, (3, 3), padding="valid", activation=tf.nn.relu)(pool2)
    pool3 = layers.MaxPool2D((2, 2), (2, 2))(conv3)
    flat = layers.Flatten()(pool3)
    output = layers.Dense(10, activation=tf.nn.softmax)(flat)

    model = models.Model(inputs, output)
    model.summary()
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    model.fit(x_train, y_train, epochs=10)
    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"Test Loss: {test_loss} - Test Acc: {test_acc}")

    model.save("mnist_classifier.h5")

model.evaluate(x_test, y_test)