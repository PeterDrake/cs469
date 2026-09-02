# Overview
This exercise gives your first taste of training a neural network using Keras.

# Fashion MNIST
The [Fashion-MNIST]([https://en.wikipedia.org/wiki/Fashion-MNIST](https://keras.io/api/datasets/fashion_mnist/)) dataset is very similar to the MNIST dataset introduced on p. 17 of the textbook, but the images to be classified are low-resolution photos of clothing items rather than handwritten digits.

Your task is to train a neural network on this dataset (which, like MNIST, is built in to the `keras.datasets` module). Create a Google Colab notebook, copy *only the necessary parts* from [Chollet's notebook](https://colab.research.google.com/github/fchollet/deep-learning-with-python-notebooks/blob/master/chapter02_mathematical-building-blocks.ipynb), and modify it to use `fashion_mnist` instead.

You should get a final test accuracy of a little under 88%.

You hardly need to write any code for this assignment. If you understand the existing code, it should go very quickly.

# Optional Challenge Problems
To go above and beyond, try some of the following. They may require additional internet research.

* Improve the network's accuracy with a larger network (more units in the first Dense layer or additional layers).
* Display the first ten images and which categories the network thinks they belong in.
* Display a confusion matrix showing the degree to which the model confuses different classes of images.

# What to Hand in
Hand in a link to your Colab notebook.
