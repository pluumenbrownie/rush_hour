import random as rd
from vehicle import *
from models import RushHour

class Algorithm():
    """ Solves the rushhour game by selecing random cars and moves. """
    
    def __init__(self, game: RushHour):
        self.game = game
        self.vehicles = game.get_vehicles()
        self.vehicle_ids = [id for id in self.vehicles.keys()]
        self.directions = [1, -1]
        
    def random_algorithm(self):
        while not self.game.is_won():
            # Choose a random move
            move = rd.choice(self.directions)
            # choose a random car
            vehicle = rd.choice(self.vehicle_ids) 
            # move the car in the game
            self.game.process_turn(vehicle, move)
        # Print the output of the game in output.csv
        self.game.export_solution()

if __name__ == '__main__': 
    board_file = "gameboards/Rushhour6x6_1.csv"
    game =  RushHour(6, board_file)
    solver = Algorithm(game)
    solver.random_algorithm()

    
