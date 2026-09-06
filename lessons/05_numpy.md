# NumPy
* Prounounced "num py", *not* rhyming with "dumpy"
* Python package for dealing with arrays of numbers
* Example
  * `import numpy as np`
  * `a = np.array([[5, 0, 3], [9, 7, 1]])`
* Key differences from lists:
  * Possibly multidimensional (although you could use lists of lists)
  * Array has a specific size that doesn't change
  * All elements have the same data type
* Why?
  * Efficiency
    * Less memory
    * Runs faster
  * Convenience
    * Shorter, clearer code
* Attributes of arrays
  * `a.ndim`
  * `a.shape`
  * `a.size`
  * `a.dtype`
* Accessing elements
  * `a[0, 1]`
  * Slicing
    * This is a view
    * Use `a.copy()` if you want a copy
* Other methods, functions, and operators
  * `a.reshape(3, 2)`
  * `np.concatenate((a, a))`
  * `a * 2`
  * `a + a`
    * Other arithmetic operators are similar
  * Challenge: convert a bunch of Fahrenheit temperatures to Celsius: -40, 0, 32, 100, 212
  * `np.sum(a, axis=0)`
  * `a > 3`
  * `a[a > 3]`
    * Note the reduction in dimensions
  * `a[(a > 3) & (a < 8)]`
* Matrix multiplication
  * How to compute by hand, with example
  * RC mnemonic
  * TPS: What are the constraints on the shapes of the multiplied matrices?
* Work through [chapter 2 notebook](https://github.com/fchollet/deep-learning-with-python-notebooks), "The gears of neural networks: Tensor operations"
