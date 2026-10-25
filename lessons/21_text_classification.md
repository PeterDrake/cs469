# Text Classification

## Preparing Text Data
* Text is split into tokens
  * A token might be a character, a word, or (as we'll see) something in between
  * Short story on paying for AI: You're paying for tokens read and generated
* Regular expressions
  * `import regex as re`
  * Use `re.findall`
  * `r'.'` matches any one character
  * `r'[\w]+|[.,!?;]'` matches a word or punctuation mark
    * The `r` makes it a "raw" string literal, so the `\w` isn't interpreted
    * `[...]` means "any one of these"
    * `\w` means "any word character", i.e., letter, digit, or underscore
    * `+` means "one or more of the preceding thing"
    * `|` means "or"
* A *vocabulary* maps tokens to indices
  * There is typically a special token `'[UNK]'`, for "unknown", at index 0
* Text must be standardized
  * Make lower case
  * You could try harder, but it's not worth it
* Preprocessing stages:
  * Standardize
  * Split into tokens
  * Convert to indices
* Tokenization
  * Keeps the most common indices (you choose maximum size)
  * Character produces fewer `'[UNK]'`s, but more tokens overall, than word
* Subword tokenization
  * Idea: have tokens for all characters, plus tokens for common sequences
  * Byte-pair algorithm
    * First generate all character tokens
    * Repeatedly join the most common consecutive pair into a new token
    * The regular expression in Listing 14.6 uses extremely obscure Python regex features; we'll just trust that it works
    * Fascinating book issues:
      * The printed book has callouts in listings which the online book doesn't
      * Listing 14.7 in the printed book is just wrong -- it doesn't match the online book or the Colab notebook!
  * Upshot: This doesn't have to use `'[UNK]'`, but doesn't need as many tokens as character encoding

# Sets vs Sequences
* Idea: Will we pay attention to word order?
* IMDb movie review classification dataset

# Set Models
* One-hot encode all tokens present ("bag of words")
* Simple model gets 88% test accuracy
* Bigrams turn this up to 90%
  * You could do trigrams, but there are too many combinations beyond that

# Sequence Models
* Have to truncate or pad to make all sequences same length
  * Add special `'[PAD]'` token
* Plan A for encoding the sequence: one-hot each word
* Bidirectional LSTM gets 84% test accuracy
* Plan B: Word embeddings
  * TPS: What does "orthogonal" mean in first paragraph of 14.5.2?
  * Idea: Each word (or token) is a point in multidimensional space rather than a one-hot vector
  * [Pimantle](https://semantle.pimanrul.es/)
  * Moving in a direction in this semantic space tends to mean the same thing
    * Pet -> wild animal example in Figure 14.4
    * Gender and plural vectors      
      * king - man + woman = queen
      * Bias problem: doctor - man + woman = nurse
  * An Embedding layer can learn embeddings from data
    * Mask so LSTM doesn't have to remember through a bunch of padding
  * We're still at 84% test accuracy
    * The problem: We have so little data that the model is overfitting
    * Solution: Pretraining (the "P" in "GPT")
      * You can do this on unlabeled data
      * Learn to predict a word from the (unordered) surrounding words
      * As it learns, it finds a decent embedding
      * Then recycle this embedding when training on the classification task
        * Now up to 89%
        * Solution: More data and (next chapter) Transformers