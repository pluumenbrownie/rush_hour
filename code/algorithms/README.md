# algorithms
This folder contains all of the algorithms 

- algorithm.py: our random and greedy inherit functions from this file. It includes functions for general things, such as choosing a random direction, choosing a random car and finding a blocking vehicle. 
- beam_search.py: this algorithm is based on breadth first, but has a different build children function and different run function. In this implementation of beam search, after building the children and checking if the game hasn't already been there, sorts the children based on a heuristic and then only keeps the ones at the front of the queue.
- branch_and_bound.py
- breadth_first.py: this algorithm is based on depth first, but uses a queue instead of a stack
- depth_first.py
- greedy.py: this implementation of greedy checks to see if it can move the car first. If that's not possible, it checks to see if it can move a vehicle that's blocking the red car. If that's also not possible, it chooses a random car.
- random.py: this algorithm randomly chooses a vehicle and a car and checks to see if that move is valid. If so, it performs the move 