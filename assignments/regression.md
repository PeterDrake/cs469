# Overview
This exercise gives you an opportunity to train a neural network to perform regression on some data about life
expectancy. It's also a chance to work with less scaffolding than you've had before, getting you closer to a real-world
scenario.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Life Expectancy
You'll need to get the [life expectancy dataset](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/)
from Kaggle. For various countries (in various years), it gives live expectancy and a number of related variables.
The regression task is to predict life expectancy from some of these, as specified in the [sample file](../src/life_expectancy.py).

First, train a linear classifier (that is, a network with a single unit with no activation function) on the data. You'll need to complete all of the sections after
`TODO` in the sample file. You should get a training (and validation) mean square error
of around 0.0036.

Now add a hidden layer. This should significantly improve your mean squared error. I was able to get the MSE down to
about 0.0017 on the training set and 0.0022 on the validation set. (I was not able to get the network to overfit in the
sense of the validation MSE increasing.)

# Optional Challenge Problems
To go above and beyond, try some of the following. They may require additional internet research.

* Run your network on BLT. (You may choose to do this from the start to get faster runs.)
* Plot a learning curve. If you do this on BLT, you'll have to find out how to get matplotlib to write to a file
instead of opening a GUI window.
* Include more of the variables. Can you get better accuracy?
* Try k-fold cross-validation. Does it help?

# What to Hand in
Hand in a link to your .py file and the output of your final run (including testing).
