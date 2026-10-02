# Image Classification
* [Slides](https://docs.google.com/presentation/d/1UlTo1dktFEWkQ34bmw6rmkyDhEUiWpGDLT8x_CdDcZM/edit?usp=sharing) (starting at slide 13)
  * After first slide: [grandmother cell / Jennifer Aniston neuron](https://en.wikipedia.org/wiki/Grandmother_cell)
  * Challenge after second "convolution" slide: Given a NumPy input array, a kernel, and coordinates, find the output of the convolution at that point
      * This should not require a loop!
      * Bonus: Apply the convolution across the entire input array, producing an output array instead of a single number; this does require a loop
      * Bonus bonus after explaining padding: Allow for "same" padding
* Other key concepts from chapter (discussion of each)
  * Direct training
  * Data augmentation
  * Using a pretrained model
    * Feature extraction
    * Fine-tuning (including partial)
* If excess time, work through notebook
  * This requires logging into Kaggle *and* joining the competition
  * ... and save `convnet_from_scratch_with_augnentation.keras` for later