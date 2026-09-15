# Fundamentals of Machine Learning
* Generalization
  * Optimization vs generalization
  * Underfitting and overfitting
    * Underfitting can result from a model that is too simple or too little training
  * Models will fit noise
    * Figure 5.6 on p. 142
  * Manifold hypothesis
    * TPS: What is the hypothesis?
    * Interlocking spiral problem where the spiral is the manifold
  * Interpolation
    * Has to be along the manifold, not just in the "parent space"
    * Works for "intuition", but not for "reasoning"
  * More data always helps
* Evaluation
  * TPS: What's the difference between a parameter and a hyperparameter?
  * Information shouldn't leak from the test set
  * WC: Why is it important to shuffle the data before slicing off a test set?
  * WC: What's the difference between simple hold-out validation and K-fold validation?
  * Activity: What are common-sense baselines for the following tasks?
    * Play *Chess*
    * Predict someone's lifespan based on their genome
    * Predict the age of a painting based on an image of it
    * Predict the running time of a program based on its code
  * A common-sense (or much simpler) model might be fine!
* Improving fit
  * TPS: Why should you overfit first?
  * TPS: What should you change if the model isn't learning at all?
  * TPS: What is likely the problem if the model learns but won't overfit?
* Improving generalization
  * Feature engineering
    * Clock example, p. 159
      * Discussion: How would you write a program to extract the angles of the hands?
  * Early stopping
  * Regularization
    * Smaller network
    * Weight regularization
    * Dropout
      * TPS: Why do we rescale the output (p. 167)?
      * Another explanation: you're training the powerset of the model