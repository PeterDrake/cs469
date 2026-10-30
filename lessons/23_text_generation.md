# Text Generation
* Discussion: What do we think of the author's take on AI art and writing?

## Training a Mini-GPT
* Colossal Clean Crawled Corpus
* Note the huge compute cost!
* `SentencePieceTokenizer`
* WC: Many documents will be far too long to fit into one vector of tokens. How does the book handle this?
* Only uses the decoder
  * Question and answer are put together in one sequence, making data curation much easier
* Unembedding can be done by transposing the embedding weights
* "Training a large Transformer is famously finicky"
* In deep or recurrent networks, gradients can vanish (if units can saturate, like sigmoid) or explode (if they can't, like ReLU)
  * Learning rate warms up over course of pretraining to prevent exploding gradients
* Logits are the "unnormalized log probabilities" before applying softmax
* When generating text, the input has to be padded (so it's always the same length) to allow for compiling and therefore efficiency
* Cached generation: save state rather than re-reading entier input sequence for each token generated
* Sampling strategies
  * Greedy
  * Top-k
  * Random (with temperature)

## Using a Pretrained LLM
* Environmental costs (first two paragraphs of 16.3)
* "The Gemma terms of uses prohibit using the model for things like generating spam or hate speech."
* We've got spicy autocorrect!
  * You can do better with more elaborate prompts
  * Hallucination
* Instruction fine-tuning
  * Train further on handcrafted instruction-response pairs
  * Will need a special technique to train
* Low-Rank Adaptation (LoRA)
  * Because optimizer needs to keep track of gradients and momentum, it can run out of memory
  * You can save memory by freezing some of the weights
  * LoRA replaces a linear layer with a frozen version plus a smaller trainable approximation
  * With that, we can do the instruction fine-tuning
    * Much better at answering questions
    * Still hallucinates
      * ... but you could train it with pairs where the "correct" response is "I don't know"

## Going Further With LLMs
* Reinforcement learning with human feedback
  * Have humans rank various responses
  * Train another, smaller model to produce these ratings
  * Use this to train the main model using reinforcement learning
    * Listing 16.15
  * With other tricks, is less prone to hallucinations
    * But read last paragraph before 16.4.2
* Multimodal LLMs
  * A separate image encoder can encode an image as a sequence of "soft tokens"
    * WC: In what sense are they "soft"?
* Foundation models (second paragraph on p. 501, before 16.4.3)
* Retrieval augmented generation (RAG)
  * LLMs have a cutoff date in their knowledge
    * Compare how humans know the music and other pop culture from when they were in college
    * Add extra information into the prompt
      * Perhaps from a vector database: a bunch of documents embedded as vectors
    * Bulleted list before 16.4.4
* "Reasoning" models
  * Classical vs connectionist AI
  * Chain-of-thought prompting: "Show your work"
  * By checking final answers, you can use reinforcement learning to fine-tune the "reasoning" generation
* Where Are LLMs Heading Next?
  * Recently companies have been seeking more data rather than larger models
  * Figure 16.8 (note logarithmic scales)
  * We're running out of data!