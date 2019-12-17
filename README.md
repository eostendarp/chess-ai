# Chess AI

This project is a joint effort between [Erich Ostendarp](https://github.com/eostendarp), [Sean McQuillan](https://github.com/mcquill99), [Tim Clerico](https://github.com/tclerico), and [Damion Lance](https://github.com/damionlance) to create an AI that could perform reasonably well in the game of chess. We focused on an expert driven approach, splitting up responsibilities between the four of us. This project was part of an AI course taken Fall semester 2019.

# Features:

### Tim: 

#### History Hueristic:

  The history heuristic is a method for move ordering to improve the pruning preformed by algorithms like Alpha-Beta or NegaScout. It is based on the number of cutoffs caused by a given move. Values are added into a table and are used to order the non-capturing moves.
  
  Resources: Chess Programing Wiki, has an indepth description of the algorithm and links to discussion about it. See: [History Heuristic](https://www.chessprogramming.org/History_Heuristic) and [Relative History Heuristic](https://www.chessprogramming.org/Relative_History_Heuristic)
  
  The techinque has in general been used specifically for move ordering and is sometimes used in combination with other heuristics. This is appropriate for out project because the goals we have depend heavily on havinig a solid method of move ordering.

#### Capture Moves:

  Sorting of possible capture moves for each possible move is done to improve move ordering and the efficiency of our search algorithm. All capture moves are found and then categorized as a winning, neutral, or losing capture relative to the values of the pieces involved. Winning captures are sorted by the difference in value of victim and attacker following the idea of [Most Valuable Victim Least Valuable Attacker](https://www.chessprogramming.org/MVV-LVA). Neutral captures are sorted in descending order by value of the victim, and losing captures are sorted in descending order of attackers.
  
  
### Sean: 

#### Principal Variation Line:

  Principal Variation in chess is the sequence of moves that the agent finds that leads to the best possible move at that game state. The goal is to have a list as a property of our agent that stores the best move for each layer of the game tree, so that when we order moves, it prioritizes exploring those moves first for each depth of the tree. According to the Chess Programming Wiki Page, it is considered the "most important move ordering consideration" for an iterative deepening agent like the alpha-beta we're using. 
  
  Resources: The Chess Programming Wiki page is a great resource for this. I found out about this technique on the Move Ordering Page, and there is an entire page dedicated to Principal Variation as a topic. It can be explored much more deeply than just a PV-Line implementation, but for the sake of time this is the implementaiton I am going for
  
  https://www.chessprogramming.org/Principal_Variation The implementation I'm specifically going for is referred to as "PV-List on the stack"
  https://www.chessprogramming.org/Move_Ordering This is where I saw the idea of the Principal Variation. Since it is considered one of the most important move ordering techniques I decided it would be a good place to start for our AI agent
  
  It is really useful for turn based games like chess, but can be applied to any turn based game with a good heuristic, So it can be used to efficiently move order in checkers or connect 4, for example. Finding the actual PV-Line is not an expensive move either, as it stores the moves as it iterates through the move list
  
  
### Damion: 

#### Gamestate Identifier:

   This is a system that takes in a chess board and will return an integer representing the current state of the board. 0 = opening, 1 = middlegame, 2 = endgame. This is important for our project because our expert-based agents will need to react differently depending on the state of the game. In the opening we value set up and development of minor pieces, in the middlegame we want to gain clear material advantage, and in the endgame we want to checkmate the king. What makes this difficult is that there are no clear definitions for these different states, they are opinionated and not concrete. This makes it hard to identify exactly what state a board is in.
   
   Resources: I am using various chess theory websites to help determine what exactly can be used to classify boards into these different states.
   
   This kind of thing is probably useful in a lot of intelligent agents, because a lot of systems operate in states, where the agent needs to react differently depending on such.
   
   
### Erich: 

##### Transposition and Piece-Square Tables:

  Both Transposition and Piece-Square Tables are datastructures used to speed up evaluation by storing and incrementally updating evaluation scores as moves are made. By storing board and piece-square scores, we are able to lower the number of times we need to call heuristic functions. In addition, using Zobrist Hashing techniques, board hashes can be calculated in O(1) time as opposed to O(n) time, by taking advantage of the properties of the bitwise XOR operator.
  
  Resourses:
    The Chess Programming Wiki for definitions on Piece-Square Tables
    https://web.archive.org/web/20070822204038/http://www.seanet.com/~brucemo/topics/zobrist.htm for implementation details on Transposition Tables using Zobrist Hashing
    
   Both of these datastructures are useful in speeding up board evaluation of turn based games, but the underlying concept of using a hash table to cache calculated values for later access and incremental update can be used in almost any intelligent agent 


# Environment:

  The chess game environment that we worked in is all thanks to the [python-chess](https://python-chess.readthedocs.io/en/latest/) library and is required for the code to run.
  
  
# Data:

![a2va2t](https://github.com/eostendarp/chess-ai/blob/master/data/Rplots/A2vA2T.jpeg)

![a2va3](https://github.com/eostendarp/chess-ai/blob/master/data/Rplots/grouped_A2vA3.jpeg)
  
  
# Run Yourself:

  Clone the repository, setup you virtual envionment and **pip install python-chess**
  
  Then run the **run()** function in *chess_game.py* to have two agents play against eachother. To change the agents that compete, import an agent fom the *agents* directory and replace either agent1 or agent2 in the **run()** function
