# Universal Workflow of Machine Learning
* Roleplaying exercise
  * Each team: Come up with three product ideas (things you'd want or imagine others would want)
  * Swap, then for each one:
    * What are you trying to predict?
    * What kind of task is this?
    * How would you get data?
* "You don't start from a dataset; you start from a problem."
* Defining the task
  * A "business" might be a government or nonprofit organization
  * Framing the problem
    * What are you trying to predict?
      * Do you have labeled data for that?
    * What kind of task is this?
      * TPS: When might deep learning not be the right tool for the job?
    * What's the current solution?
    * What constraints are there?
    * Is it ethical?
      * Discussion
        * What projects would be unethical?
        * What would you do if your boss asked you to do such a thing?
  * Collecting a dataset
    * Discussion:
      * Should people be asked to train their own replacement?
      * What about [people underpaid to look at graphic content](https://www.404media.co/ai-is-african-intelligence-the-workers-who-train-ai-are-fighting-back/)?
    * Beware of nonrepresentative data
      * "If possible, collect data directly from the environment where your model will be used."
      * WC: What is concept drift?
    * Understand (explore) your data
      * WC: What is target leaking?
    * Choose a measure of success
      * False positives and false negatives
        * Which is worse depends on the task
      * Precision: TP / (TP + FP)
        * How often were you right when you said yes?
      * Recall: TP / (TP + FN)
        * How often did you say yes when you should have?
      * Other, fancier metrics (F-score, AUC, ROC) exist
* Developing a model
  * Seems like the biggest thing in class, but "The hardest things in machine learning are framing problems and collecting, annotating, and cleaning data."
  * Preparing the data
    * Vectorization
    * Scaling
      * Normalization: scale each variable in 0-1 range
        * Could be a problem if you have outliers
      * Standardization: Rescale each variable to have mean 0, standard deviation 1
    * Discussion: What can you do about missing values?
  * Don't forget validation
  * Beating a baseline
    * Table of loss functions (6.1, p. 182)
  * Overfitting
    * "To figure out where this border lies, you must first cross it."
  * Regularizing and tuning
    * Only at the end, once the model is frozen, try it on the test data
* Deploying your model
  * Setting expectations
    * "The expectations of nonspecialists toward AI systems are often unrealistic."
    * Demonstrate failure modes
  * Shipping an inference model
    * REST API
      * Can anyone explain what that means?
    * On device
    * In browser
      * "Given a trained deep learning model, it is usually possible to recover some information about the training data."
  * Inference model optimization
    * Weight pruning
    * Weight quantization
  * Monitoring your model in the wild
  * Maintaining your model
