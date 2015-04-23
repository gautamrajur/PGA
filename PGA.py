# -*- coding: utf-8 -*-
"""
Partition Genetic Algorithm -
"""
import numpy as np

class Organism:
    def __init__(self, partition_length):
        self.partition = np.random.randint(2, size=(partition_length))     
        self.fitness = None

class Population(Organism):
    """
    Creates a class population that has the attributes of:
            Population Size  - Population of Genetic Algorithm
            partition Length - How many "things" are in the partition
            organism         - A list of organism that have inharitance from 
                               Class Organism
    """
    def __init__(self, population_size, partition_length):
        self.population_size = population_size
        self.partition_length = partition_length
        self.organism = [Organism(self.partition_length) for i in range(self.population_size)]


def Fitness(population,parition ):
    for ii in range(population.population_size):
        Bin1 = 0
        Bin2 = 0
        for jj in range(population.partition_length):
            if population.organism[ii].partition[jj] == 0:
                Bin1 = Bin1 + 1
            else:
                Bin2 = Bin2 + 1
        population.organism[ii].fitness =  abs(Bin1-Bin2)
                

            
        
        

NPRTL = 10
POPULATION_SIZE = 15
particle_weight = np.random.randint(2, size=NPRTL)+1
pop = Population(POPULATION_SIZE, NPRTL)
Fitness(pop,particle_weight)
print(pop.organism[4].fitness)




