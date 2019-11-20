# chess-ai

### Tasks Completed:

#### Tim: Alpha-Beta Implementation, Mobility Heuristic
#### Damion: Human Player, Greedy Agent
#### Erich: Random Agent, Transposition Tables
#### Sean: MiniMax Implementation, Parity (Piece-Value) Heuristic

## Advanced Techniques To Be Added:

#### Tim: History Hueristic:
  The history heuristic is a method for move ordering to improve the pruning preformed by algorithms like Alpha-Beta or NegaScout. It is based on the number of cutoffs caused by a given move. Values are added into a table and are used to order the non-capturing moves.
  
  Resources: Chess Programing Wiki, has an indepth description of the algorithm and links to discussion about it
  
  The techinque has in general been used specifically for move ordering and is sometimes used in combination with other heuristics. This is appropriate for out project because the goals we have depend heavily on havinig a solid method of move ordering.
  
#### Damion: Gamestate Identifier:
   This is a system that takes in a chess board and will return an integer representing the current state of the board. 0 = opening, 1 = middlegame, 2 = endgame. This is important for our project because our expert-based agents will need to react differently depending on the state of the game. In the opening we value set up and development of minor pieces, in the middlegame we want to gain clear material advantage, and in the endgame we want to checkmate the king. What makes this difficult is that there are no clear definitions for these different states, they are opinionated and not concrete. This makes it hard to identify exactly what state a board is in.
   
   Resources: I am using various chess theory websites to help determine what exactly can be used to classify boards into these different states.
   
   This kind of thing is probably useful in a lot of intelligent agents, because a lot of systems operate in states, where the agent needs to react differently depending on such.
