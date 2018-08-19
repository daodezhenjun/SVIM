# coding=utf-8


from myglobal import *
import random
from deap import tools,algorithms
from deap import base, creator


class GaProcess:

    IND_SIZE = 5  # 个体属性数量
    MAXGEN = 4000 # 最大进化代数
    MUTPB = 0.5  # 变异率
    CXPB = 0.5  # 交叉率
    POPSIZE = 300  # 种群大小

    svim = None
    toolbox = base.Toolbox()
    tools.HallOfFame
    def setSVIM(self,arg):
        self.svim = arg

    def __evalution(self,individual):
        if len(individual) == 5:
            return self.svim.fitting(Svi_param(individual[0], individual[1], individual[2], individual[3], individual[4])),
        else:
            print "evalution error: len(individual) is ", len(individual)
            exit(0)

    def init(self):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)
        # self.toolbox.register("attr_bool",random.randint,0,1)
        self.toolbox.register("attr_float", random.uniform,-1.0,1.0)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_float, 5)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.toolbox.register("evaluate", self.__evalution)
        self.toolbox.register("mate", tools.cxUniform,indpb=self.CXPB)
        self.toolbox.register("mutate", tools.mutGaussian, mu = 0, sigma = 0.3, indpb=self.MUTPB)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

        #self.toolbox.register("select", tools.selRandom)

    def save_best_ind(self, population, nbest = 1):
        best_ind = tools.selBest(population, nbest)[0:nbest]
        population = self.toolbox.select(population, k=len(population))
        if nbest<len(population):
            r = random.randint(0, len(population)-nbest)
            population[r:r+nbest] = best_ind
            return population
        else:
            print "arg error : nBest>=length(pop)",nbest,",",len(population)
            exit(0)


    def run_evaluate(self):
        population = self.toolbox.population(n=self.POPSIZE)
        #halloffame = tools.HallOfFame(maxsize=1)
        count=0
        for gen in range(self.MAXGEN):

            population = algorithms.varAnd(population, self.toolbox, cxpb=self.CXPB, mutpb=self.MUTPB)
            invalid_ind = [ind for ind in population if not ind.fitness.valid]
            fits = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
            for fit, ind in zip(fits, invalid_ind):
                ind.fitness.values = fit

            #halloffame.update(population)
            #save best individual
            population = self.save_best_ind(population)
            best_ind = tools.selBest(population,1)[0]
           # print "best indivdual is ", best_ind, " best fitness is ", best_ind.fitness.values
        '''
        for ii in population:
            print ii
        '''
        print max([ind.fitness for ind in population])
        return tools.selBest(population, 1)[0]





