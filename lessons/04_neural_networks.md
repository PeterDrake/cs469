# [Neural Network Playground](https://playground.tensorflow.org)
* Set up no hidden layers, linearly separable problem, run it
  * Repeat with lowest learning rate (0.00001) to slow it down
* Now try xor problem
  * Even with learning rate back up to 0.03, doesn't work
  * Add one hidden layer with two units, learning rate 0.001
    * Sometimes it gets stuck in a local minimum
    * When it does work, it seems to partially solve the problem and then have an "insight"
    * With a third hidden unit, it almost always works
* Experiment with concentric rings
  * How well does it work with two hidden units?
  * How about with three?
* Interlocking spirals, learning rate 0.03
  * How does it do with 2, 4, or 8 neurons?
  * Does a second hidden layer help?
    * Examine outputs of second hidden layer units
  * What if we crank the noise up to 50?

# MNIST
* Open [chapter 2 notebook](https://github.com/fchollet/deep-learning-with-python-notebooks)
* Remember to turn off AI assistance
* Read through the code under "A first look at a neural network" together with warm calls
  * What type of value does `mnist.load_data()` return?
  * Explain the value of `train_images.shape`.
  * Explain the value of `train_labels`.
  * In the definition of `model`, which words are class names?
  * Explain each of the three arguments in the call to `compile`.
  * Why do we call `reshape` and `astype`?
  * What is `fit` doing?
  * Explain the value of predictions[0].
    * Which digit did it predict?
  * What does `argmax` do?
* Add the following after the initial load of the data:
    ```python 
    import matplotlib.pyplot as plt
    plt.imshow(test_images[0])
    ```
  * Why doesn't it run?
    * Fix this by re-running cells
