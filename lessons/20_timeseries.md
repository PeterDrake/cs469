# Timeseries Forecasting
* Tasks
  * Forecasting
  * Anomaly detection
  * Classification
  * Event detection
* Example: weather prediction
  * Given 5 days of data, predict the temperature in 24 hours
  * WC: Explain the samples shape at the end of Listing 13.8 on p. 359
  * Baseline: Assume the temperature will be the same as it is now!
    * Mean absolute error is 2.44C on validation set
    * Discuss: Should we be looking at testing error here?
  * Basic model
    * Just take in the whole 5-day history as a vector
    * TPS: Is it overfitting?
    * WC: Why does this do worse than the baseline when it has more information?
  * 1D convolutional model
    * Even worse!
    * Weather data isn't translation invariant (mornings don't look like evenings)
    * Order matters for weather data
* Recurrent neural networks
  * It works better (Figure 13.5, p. 365)
  * Figures 13.6, 13.7
  * Long Short-Term Memory (LSTM)
    * Unusually, Chollet and Watson's explanation is absolutely opaque
    * Instead, look at pp. 568-571 of Géron, *Hands-On Machine Learning With Scikit-Learn, Keras & TensorFlow*.
      * Figure 15-12
        * Inputs
          * x is the regular input
          * h is the short-term state
          * c is the long-term state
        * Outputs
          * y is the prediction
          * h is the short-term state
          * c is the long-term state
      * Read from right below figure through "and more" halfway down next page
  * Additional techniques
    * Recurrent dropout
      * Works well -- Figure 13.11
        * Any ideas why it's doing *better* on validation set than training set?
    * Stacking layers
      * Even better
    * Bidirectional RNNs
      * Read through the sequence on both directions
      * Useless for weather, but very good for language