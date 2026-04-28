import random

# -------- Parameters --------
POP_SIZE = 20
GENES = 16  # bits per individual
GENERATIONS = 50
MUTATION_RATE = 0.01

# -------- Functions --------

# Create binary individual
def create_individual():
    return [random.randint(0, 1) for _ in range(GENES)]

# Decode binary to real value in [-10, 10]
def decode(individual):
    binary = "".join(map(str, individual))
    integer = int(binary, 2)
    return -10 + (integer / (2**GENES - 1)) * 20

# Objective function
def fitness(individual):
    x = decode(individual)
    return x**2

# Tournament selection
def selection(population):
    i1, i2 = random.sample(population, 2)
    return i1 if fitness(i1) > fitness(i2) else i2

# Junction/crossing (1 point)
def crossover(parent1, parent2):
    point = random.randint(1, GENES - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation
def mutate(individual):
    return [
        bit if random.random() > MUTATION_RATE else 1 - bit
        for bit in individual
    ]

# -------- Initialization --------
population = [create_individual() for _ in range(POP_SIZE)]

# -------- Evolution --------
for gen in range(GENERATIONS):
    new_population = []

    for _ in range(POP_SIZE // 2):
        parent1 = selection(population)
        parent2 = selection(population)

        child1, child2 = crossover(parent1, parent2)

        child1 = mutate(child1)
        child2 = mutate(child2)

        new_population.extend([child1, child2])

    population = new_population

    # Best individual
    best = max(population, key=fitness)
    print(f"Gen {gen}: x = {decode(best):.4f}, f(x) = {fitness(best):.4f}")

# -------- Final result --------
best = max(population, key=fitness)
print("\nBest solution found:")
print(f"x = {decode(best):.4f}, f(x) = {fitness(best):.4f}")
