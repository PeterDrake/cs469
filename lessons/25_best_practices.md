# Best Practices in the Real World

## Getting the Most out of Your Models
* Hyperparameter optimization
  * General idea: Try a set of hyperparameters (by training the model), then pick another
  * Options include:
    * Grid search (infeasible except on very small grids)
    * Simple random search
    * Genetic algorithms (random, but keep and "breed" the best results in each generation)
    * Bayesian optimization (make initial guess, then update based on evidence)
  * Potentially extremely time- and compute-intensive, as you have to train the model for each set!
  * KerasTuner can manage this for you
  * Intuition and expertise can help!
* Model ensembling
  * Build several models and combine their guesses
    * Potentially weighted average
  * Diverse teams perform better, both with humans and machine learning models

## Multiple Devices
* Data parallelism
* Model parallelism
* How do we monitor GPU usage on BLT?
  * From BLT, ssh sprouts -t nvtop
  * It looks like we have to do something special to use multiple GPUs, and the line in the book (under Using Data Parallelism With JAX, p. 551) throws an error. Still working with Jeremy on this.

## Lower Precision
* Floating point precision
* Speed up inference by using 16-bit floats
* Very small gradient *updates* can't be represented in 16 bits, so
  * Use mixed precision, where most computations are 16-bit, but weights are stored in 32-bit
* Scaling up the loss function prevents underflow when using 16 bits
* Quantization for inference: convert weights to uint18
  * Be sure to scale before casting to int!
