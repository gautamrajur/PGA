# -*- coding: utf-8 -*-
"""
Partition Genetic Algorithm -
"""
import numpy as np
import operator
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
        self.min_fitness = None

        
def Min_Fitness(population):
    """
    Calculates Min Fitness of that generation of the population    
    """
    min_fitness = population.organism[1].fitness    
    for ii in range(population.population_size):
        if (population.organism[ii].fitness != None):
            if (population.organism[ii].fitness < min_fitness):
                min_fitness = population.organism[ii].fitness
    return min_fitness
#    population.min_fitness = min_fitness
#    return 

def Fitness(population, partition ):
    '''
    Fitness Function of the Genetic Algorithm
    If Checks partition array and adds up total value in each bin 
    Difference in the Bin number is the partition array 
    '''
    for ii in range(population.population_size):
        Bin1 = 0
        Bin2 = 0
        for jj in range(population.partition_length):
            if population.organism[ii].partition[jj] == 0:
                Bin1 = Bin1 + partition[jj]
            else:
                Bin2 = Bin2 + partition[jj]
        population.organism[ii].fitness =  abs(Bin1-Bin2)
                
def Natrual_Selection(population, NUM2KILL):
    '''
    "kills" the lowest two performing organism by making their
    fitness and partition None    
    '''
    population.organism.sort(key=operator.attrgetter('fitness'))
    for ii in range(NUM2KILL):
        population.organism[-ii-1].fitness = None
        population.organism[-ii-1].partition = None

def Mating(population):
    '''
    Mates two 'successful' genes by taking the first half of genes from one parent
    and the second half from the second parent
    '''
    parent1 = 1
    parent2 = 2
    if (population.population_size % 2 == 0):#Even Population Size
        lower_bounds = population.population_size/2
        upper_bounds = population.population_size
    else: #odd population size
        lower_bounds = (population.popuilation_size + 1)/2
        upper_bounds = population.population_size         
    for ii in range(population.population_size):
        if population.organism[ii].fitness == None:
            population.organism[ii].partition = population.organism[parent1].partition
            population.organism[ii].partition[lower_bounds:upper_bounds] = population.organism[parent2].partition[lower_bounds:upper_bounds]
            parent1 = parent1 + 1
            parent2 = parent2 + 1
        
def Mutation(population):
    '''
    Randomly will mutate a gene from a parents offspring before their fitness is tested
    '''
    for ii in range(population.population_size):
        if (population.organism[ii].fitness == None)&(np.random.rand(1) > 0.9):
            rand_index = int(np.random.rand(1)*population.partition_length)
            population.organism[ii].partition[rand_index] = int(np.random.rand(1))

NPRTL = 10
POPULATION_SIZE = 10
particle_weight = np.random.randint(2, size=NPRTL)+1
print(particle_weight)
pop = Population(POPULATION_SIZE, NPRTL)
#for ii in range(1):
for jj in range(10000):
    Fitness(pop,particle_weight)
    pop_min_fitness = Min_Fitness(pop)    
    print(Min_Fitness(pop))
    if pop_min_fitness == 0:
        print('Program Optimal')
        break
    Natrual_Selection(pop,2)
    Mating(pop)
    Mutation(pop)
    



