# Overview
For the first time, this exercise has you processing text. Specifically, you will be building a system to determine whether an SMS text message is spam or not.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Spam Detection

The data come from https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset.

**NOTE: These are unfiltered texts from actual people. Some content may be offensive. Let me know if you need to avoid this.**

Your task is to build a bag-of-words model to classify each text as spam or ham.

As always, start by shuffling the data and dividing it into training (60%), validation (20%), and test (20%) sets.

A simple model like the one in the book gets around 97% accuracy!

## Hints
You can do this one on your own machine, on BLT, or in a Jupyter (Google Colab) notebook. I used a notebook.

Here is some code to read the data from the .csv file:
```python
import csv

with open('spam.csv', errors='ignore') as file:
  data = list(csv.DictReader(file))
  texts = [line['v2'] for line in data]
  labels = [line['v1'] == 'spam' for line in data]
```

Thanks to `keras.layers.TextVectorization`, you don't have to do the tokenization yourself. (I wasted some time before I realized this.)

The dataset is small enough that you don't need to specify `max_tokens` as in the book, but you'll have to look at the shape of your vectorized training data to know how many different words the model recognizes. (It's in the thousands.)

# Optional Challenge Problems
Which texts does the model misclassify?

Does a bigram or recurrent model do better?

# What to Hand In
Hand in your .py and output files (if running from a .py file) or your notebook (if you did it that way).
