# Language Models and the Transformer

## The Language Model
* Key idea: predict the next token based on the tokens seen so far
* Each token emitted is added to the sequence of past tokens
* Shakespeare example

## Sequence-to-Sequence Learning
* Sequence in, sequence out
* Useful for translation and sequence ordering
* Figure 15.1
* English-to-Spanish translation
* You can't just translate word-by-word, because word order differs between languages (second full paragraph, 15.2.2)
* Figure 15.2
* The encoder produces a representation of the entire sentence, so it can use a bidirectional layer

## The Transformer Architecture
* Problem: RNNs don't do well at remembering the distance past, because they have to cram the entire past into the state.
  * People deal with this by paying attention to the relevant parts of the past.
* Einsum notation
* Dot-product attention
  * Multiply (element-wise) sources with scores, indicating how important each word is
  * How to compute scores? Dot-product similarity between target and source
  * You can do this per input and output token (Figure 15.5)
  * `sum(score(target, source) * source)` restated as `sum(score(query, key) * value)`
* Multi-head attention
  * One head might keep track of subject, another to verb
* Transformer encoder block
  * Self-attention: Use the source as query, key, and value!
  * There are various other little details
  * Compare listing 15.14 to the left side of Figure 15.8
* Transformer decoder block
  * Similar idea, again using self-attention
  * Combines output of encoder with sequence output so far, as in Figure 15.2
  * "Causal" mask prevents self-attention from attending to the future
  * Examine right side of Figure 15.8
  * WC: What does "Nx" mean in this figure?
* Sequence-to-sequence learning with the Transformer
  * So far, it's worse than the RNN model, because it doesn't know about position
* Embedding positional information
  * Add another vector representing position to the word embedding vector
    * The position vector is learned
    * Finally, it's outperforming the RNN version!
      * ... and with less memory and computation

## Classification With a Pretrained Transformer
* BERT is pretrained to predict tokens from surrounding tokens
  * Uses subword tokenization
  * This model (just the "backbone", not specialized to a particular task) is huge!
  * Attaching a classifier, we can get 90% on the IMDb review classification task
    * A larger model gets over 95%

## What Makes the Transformer Effective?
* Word2Vec learned an embedding that placed frequently co-occurring words together
* Read paragraph beginning "Attention is, by far"
* Transformers have more sophisticated vector directions ("programs") than Word2Vec, like "write in the style of Shakespeare" rather than "plural"
* A Transformer is like a continuous database of both facts and programs
  * It's still just interpolating, thus the hallucinations and lack of "genuine, human-level intelligence"