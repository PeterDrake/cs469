# Classification and Regression

## IMDb: Binary Classification
* Encoding
  * Integers for words
  * Padding sequences (foreshadowing)
  * Multi-hot encoding
    * Warm call: What information do we lose with this encoding?
* Loss function: `binary_crossentropy`
* Validation
  * Early stopping
* Activity: Try the experiments in 4.1.6

## Newswires: Multiclass Classification
* WC: What does "mutually exclusive" mean?
* One-hot encoding (with joke about encoding 8)
* Softmax: $f(x_i) = \frac{e^{x_i}}{\sum_{j=1}^K{e^{x_j}}}$
* Loss function: `categorical_crossentropy`
  * ... or `sparse_categorical_crossentropy` if correct answers are encoded as ints instead of vectors
* Top-k accuracy
* Accuracy of a random model
  * TPS: What would it be if all the classes were equally common in the training data?
  * Discuss:
    * Why is it different empirically?
    * Would we do even better if we always guessed the most common class?

## House Prices: Regression
* Normalization
  * Have someone read the paragraph under Listing 2.5 on p. 128 (section 4.3.2)
  * [A cautionary tale about data snooping](https://www.youtube.com/watch?v=EZBUDG12Nr0&t=3102s) 51:42-58:48
* Scaling outputs
* Building the model
  * A small model mitigates overfitting (but risks underfitting)
  * Linear output layer
* Loss: `mean_squared_error`
* K-fold cross-validation
  * The `sklearn` package contains functions to make this easier
