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

# A Brief Peek at Matplotlib
*
  ```python
  import matplotlib.pyplot as plt
    
  x = np.linspace(1, 10, 10)
  y = x ** 2
  plt.plot(x, y)
  ```
* Nice to add `None` on the last line
* Second data set?
  ```python
  y2 = x * 2
  plt.plot(x, y2)
  ```
* Experiment: `scatter` instead of `plot`
* Challenge: Using the cheat sheet and web searching, add title and legend

# Numpy Art Contest
* Create a 256x256x3 tensor, data type uint8
* Using loops, change some of the values
* Using `plt.imshow`, display the image
