# Overview
This exercise has you training a model to classify images of butterflies. I've taken off even more training wheels this time!

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Butterflies
The dataset involves images of butterflies, to be classified into one of 50 species. To get it, I:

1. Downloaded a zip file from https://images.cv/dataset/butterfly-image-classification-dataset. I chose 32x32, color, no augmentation.
2. Unzipped it.
3. Digging into the directories, removed the directories `animal butterfly` and (from `val`) `vehicle car car_model butterfly car_mazda`. The first was a higher-level category from a larger dataset whence this one was derived. The second was an unrelated category in the larger dataset whose name happened to contain the word 'butterfly'.

If you run on BLT, these files are in `/home/drake/butterfly/images/data`, so you can use them without having to retrieve them.

# Image Classification
Using a convolutional network, train a model to classify these images.

For comparison, I was able to get about 8% validation accuracy using a simple net with no convolutional layers and 71% using a model lifted fairly directly from chapter 8.

# Hints
Use TensorFlow dataset object, as explained in subsection 8.2.4. The data directories are already arranged correctly for this.

# Optional Challenge Problems
To go above and beyond, try some of the following. They may require additional internet research.

* Use fancier techniques, like data augmentation, to improve the accuracy of the network. Can you get 90% accuracy? 95% 98%? (I don't know -- I haven't tried it yet!)
* Try loading a pretrained network. Can it be trained to do even better on this task?
* Can you get more accuracy with higher-resolution images?

# What to Hand in
Hand in your .py file and the output of your run. Don't forget to evaluate the model on the test set after you have stopped making hyperparameter decisions.