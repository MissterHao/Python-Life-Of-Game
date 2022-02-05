# Python-Life-Of-Game

## What is **"Life-Of-Game"**?

Game-of-Life which stands for ["Conway's Game of Life"](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).  

> Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970.[1] It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine. 
> 
> -- <cite>[wikipedia.org](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)</cite>

## What is this Repository?

Using python 3.6, implementing this algorithm.

## How to run this code?

To start an generation, there's only two steps.
1. Import `Generations` from Game_of_life.py file.
2. Run the code below. That's it!
  `max_iter` is the parameter to restrict the max generations.
  ```python
  g = Generations(max_iter=100)
  g.start()
  ```

This game is infinite, therefore we need to set a `max_iter` parameter to restrict whole program.

<!-- ## What I learn from making this? -->

## LICENSE
GNU General Public License v3.0


