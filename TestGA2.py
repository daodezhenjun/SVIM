#!/usr/bin/python
# coding=utf-8

import array,random
from deap import creator,base,tools,algorithms
#导入用到的许多包文件
creator.create("FitnessMax",base.Fitness,weights=(1.0,))
creator.create("Individual",array.array,typecode="d",fitness=creator.FitnessMax)#疑似typecode=b 为bool =d为float
#创建一个类FitnessMax，基类是base.Fitness，属性是weights=(1.0,)，注意：单目标的遗传算法是多目标的遗传算法的特例
#创建一个类Individual，基类是array.array，属性带有两个，分别是typecode和fitness
toolbox=base.Toolbox()

toolbox.register("attr_bool",random.randint,0,1)
toolbox.register("attr_float", random.random)
toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attr_float,5)

ind1=toolbox.individual()

toolbox.register("population",tools.initRepeat,list,toolbox.individual)

def evalOneMax(individual):
    return sum(individual),

toolbox.register("evaluate",evalOneMax)
toolbox.register("mate",tools.cxTwoPoint)
toolbox.register("mutate",tools.mutFlipBit,indpb=0.05)
toolbox.register("select",tools.selTournament,tournsize=3)

population = toolbox.population(n=300)

NGEN=4000
for gen in range(NGEN):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = offspring

print max([ind.fitness for ind in population])