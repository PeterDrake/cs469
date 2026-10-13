# Image Segmentation
* Tasks
  * Image classification (classify image)
  * Image segmentation (classify pixels)
  * Object detection (locate objects)
* Training a model from scratch
  * Conv2D layers with stride 2 shrink the image
  * Conv2DTranspose layers expand it back to original size
    * Discuss: Could we pool and unpool instead?
  * Intersection over Union
  * Can work through code, but training this thing would take over an hour!
    * Could we do it with BLT? Jeremy is working on it.
* Using a pretrained model
  * Start loading the model -- it takes a few minutes
  * Work through this section of notebook
    * Need to import keras, because it was skipped over in from-scratch section
  * Hypothesize and experiment: What if the box is smaller than the mango?
