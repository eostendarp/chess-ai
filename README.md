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
