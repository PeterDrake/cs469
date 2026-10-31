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
* Autoencoders are good for denoising and image super-resolution
  * Moon photo hallucinations
  * Reverse diffusion: start with pure noise and iteratively enhance
* U-Net
  * Downsampling followed by upsampling, with residual connections
  * Gradually changes from low signal, high noise to vice versa
    * Weirdly, diffusion time seems to progress from 1 to 0 (because 0 is the fully denoised image)
  * Training logic before 17.2.5 "the generation process"
  * Generation process: start with random noise and repeatedly denoise
  * Results (Figure 17.12)
    * If you trained longer, you'd get better results

## Text-to-Image Models
* Both noisy image and text embedding are fed to denoiser
* Training is very expensive, so the book downloads the Stable Diffusion model
  * TPS: How would we modify this to generate video instead of still images
* Discuss: What properties of Figures 17.13 and 17.14 seem AI-generated to you? Why would AI tend to do that?
* Task for 17.3.1: Morphing between images for two text prompts
* Motivation for slerping, after Listing 17.10

* Discuss: I've got a few key frames for a 2D character in a video game.
  * How could I interpolate between them using techniques from this chapter?
  * How might I do it without using deep learning?
