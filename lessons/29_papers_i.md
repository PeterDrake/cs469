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

# Vaswani *et al.*, Attention Is All You Need
