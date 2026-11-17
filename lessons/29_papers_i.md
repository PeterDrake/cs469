# Silver *et al.*, Mastering the game of Go with deep neural networks and tree search
* Games of perfect information include Checkers, Chess, and Go, but not Poker
* $v^*(s)$ is the value of a state of the game: who wins under perfect play, say, 1 for black, -1 for white, 0 if it's a tie
* Minimax search
  * Consider moves, replies, and so on to end of game
  * This is (and always will be) intractable for games like Chess and Go
  * Instead of searching to the end, you can estimate the value of the state, $v(s) \approx v^*(s)$
* Monte Carlo tree search
  * Basic idea of Monte Carlo: sample a space by taking many random points from it
  * MCTS gradually builds a tree by playing many simulated games before actually choosing a move
  * In each simulated game (Figure 3)
    * Choose the most promising path, balancing exploration and exploitation
    * Add a new leaf
    * Finish the "rollout" by playing random moves
    * After many simulations, choose the move that has had the most success
  * Random moves are sampled using a policy $p(a|s)$, the probability of choosing action $a$ from state $s$
* Atari games
* Neural networks used in AlphaGo
  * $p_\sigma$, a policy learned via supervised learning (records of games played by human experts), for initial estimates of children of a leaf
  * Fast policy $p_\pi$ is a much smaller network for completing rollouts
  * $p_\rho$ replaces $p_\sigma$. It is trained using reinforcement learning (self-play)
  * $v_\theta$ predicts value of game, also trained on self-play
* Policy networks
  * $p_\sigma$ uses convolution, rectifier (ReLU), and softmax
    * TPS: What's the softmax doing here?
  * Input is just the raw board state
* Figure 1
* Close read of section "Searching with policy and value networks" through "... most visited move from the root position"
* Result: stronger than all other Go programs and the European human champion 5-0
  * Went on to beat Lee Sedol 4-1 (headline news) and Ke Jie 3-0
  * AlphaGo Zero beat AlphaGo 100-0 without human training
  * Generalized to AlphaZero, which ["achieved within 24 hours a superhuman level of play in the games of chess, shogi, and Go"](https://en.wikipedia.org/wiki/AlphaGo#AlphaGo_Zero_and_AlphaZero)
  * Changed Go strategy for human players; such programs are used for training
* Easter egg in second set of references

# Vaswani *et al.*, Attention Is All You Need
* WC: What was the main contribution of this paper?
* WC: Explain each of
  * Recurrent neural networks
  * Long short-term memory
* What is a "gated recurrent neural network"? (We haven't heard this term, but we can guess.)
* The "inherently sequential nature" of RNNs "precludes parallelization within training examples". TPS: What does this mean and why is it a problem?
* Self-attention already existed -- like all papers, this stands on the shoulders of giants
* Figure 1: We've seen this diagram before!
  * If there are N = 6 copies of each layer, how exactly do the encoder-to-decoder connections work? It's not clear.
* First paragraph under 3.2 attention
* TPS: Why does the dot-product attention need to be scaled?
* Positional encoding function is hand-coded; they tried learning it, but it wasn't any better
* What does the word "desiderata" (end of first paragraph in section 4) mean?
* Last paragraph of section 4
* 5.2: Training time was bigger that what we've done, but much smaller than modern LLMs
* Last sentence, first paragraph of 6.1
  * Verify in Table 2
  * What does BLEU mean?
  * FLOP?
* Table 3: They tried many variations
* Constituency parsing (I had to look it up) appears to be a way of finding the grammatical structure of a sentence (noun, verb, dependent clauses, etc.)
* Figures 3-5
* What is "anaphora resolution"?
  * Okay, how would you find out?
* Suppose you get a job as an intern at an AI company. They tell you to replicate the results in this paper. You have a month and access to plenty of GPUs. What do you do?
