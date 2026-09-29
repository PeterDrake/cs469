# Modularity
* Figure 9.2
  * Note information flows *downward*
  * Repeated blocks
  * TPS: As you proceed through the network:
    * Does the number of pixels increase, decrease, or stay the same?
    * How about the number of features?

# Residual connections
* TPS: Explain the vanishing gradients problem
* Getting around this with residual connection, Figure 9.3
* Work through this part of notebook, having people take turns explaining it line by line
  * Note special techniques used to deal with:
    * Increasing numbers of filters
    * Decreased image size due to convolution
    * Decreased image size due to max pooling

# Batch normalization
* Idea: normalize the output of each layer (not just the data)
* Why does it work? Nobody knows!
* Technicalities
  * Generally put it after each Dense or Conv2D layer
  * You don't need bias in layers
  * Author recomments putting it between the convolution and the activation

# Depthwise separable convolutions
* Idea: process each channel separately
* Read last sentence in first paragraph in section 9.4
* Discuss pros and cons
* Read first paragraph after Figure 9.5
