import random, matplotlib.pyplot as plt
from chromosome import Chromosome, tournament_selection


def genetic_algorithm(generations:int, pop_size:int, mutation_prob:float=0.05, graph:str='genetic_graph.png', quickFinish=True):
    '''
    to disable graphing set the graph parameter to None or ''
    quickFinish flag denotes whether this function should return the optimal answer once it is found or if it should go to n-generations even after the optimal solution is found
    '''
    population = [Chromosome() for i in range(generations)]
    
    avg_costs = []
    best_costs = []

    generation = 0
    finish = False
    while generation < generations and not finish:
        if graph != None and graph != '':
            costs = [i.getCost() for i in population]
            avg_costs += [sum(costs) / len(costs)]
            best_costs += [min(costs)]
        
        new_population = []

        # ensure the best solution still goes on
        best = min(population, key=lambda x: x.getCost())

        if best.getCost() == 0 and quickFinish:
            finish = True

        
        new_population += [best.clone()]

        for _ in range(pop_size - 1):
            p_a, p_b = tournament_selection(population)
            child = Chromosome.crossoverChild(p_a, p_b)

            if random.random() <= mutation_prob:
                child.mutate()

            new_population += [child]

        
        population = new_population
        generation += 1


    if graph != None and graph != '':
        plt.figure(figsize=(9, 5), dpi=400)
        plt.plot(avg_costs, label="avg cost")
        plt.plot(best_costs, label="best cost")
        plt.title("Genetic algorithm")
        plt.xlabel("generation")
        plt.ylabel("cost")
        plt.legend()
        plt.figtext(0.01, 0.015, f"({pop_size=}, {generation=})", fontsize=8, fontstyle="italic", color="dimgrey")
        plt.savefig(graph)

    return min(population, key=lambda x: x.getCost())


if __name__ == '__main__':
    import time

    start = time.time()
    answer = genetic_algorithm(500, 100)
    end = time.time()

    print(answer)
    print(answer.getCost())


    print(end-start)