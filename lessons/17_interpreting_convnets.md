# Interpreting what ConvNets learn
* Visualizing intermediate activations
  * Idea: For a given image, where does a single filter on a later level "light up"?
  * Complication: Before running the ch 10 notebook, a file is needed from the ch 8 notebook
    * ... which requires logging into Kaggle *and* joining the competition
    * I've got the file saved in in-class code
  * Look at a filter from the first layer, discuss what it might be detecting
  * Look at all filters
    * Does there seem to be an eye detector? What would that look like?
  * Notion of information distillation pipeline
* Visualizing ConvNet filters
  * Idea: Use gradient *ascent* to find the image that would most activate a given filter
  * Look at one filter
  * Class challenge: Generate all of the images for a later layer
* Visualizing heatmaps of class activation
  * Idea: Have someone read third paragraph in section 10.3, p. 299
  * Run elephant example