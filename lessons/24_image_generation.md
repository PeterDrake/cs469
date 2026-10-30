# Image Generation

## Deep Learning for Image Generation
* Sampling from a latent space (Figures 17.1, 17.2)
* Generative adversarial models (GANs)
  * TLDR: One model creates believable images while another tries to spot the fakes; they give each other pressure to improve
  * The book skips these because they have "fallen out of fashion"
* Variational autoencoders
  * Autoencoder (Figure 17.3)
    * Trained by using the same image as input and output
  * VAE converts image into mean and variation of a distribution
    * To generate an image, a new point is sampled from this distribution and decoded into an image
    * Loss is reconstruction (reproducing input image) + regularization (to prevent overfitting)
    * TPS: What would happen if there was overfitting in a system like this?
    * Figure 7.5
      * WC: What are the axes of this figure?
      * Discussion: The book talks about 1s and 4s, but there don't seem to be any here. Ideas?

## Diffusion Models
