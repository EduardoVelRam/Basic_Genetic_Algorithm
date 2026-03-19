# 🧬 Genetic Algorithm for Function Optimization

This project implements a simple **Genetic Algorithm (GA)** to optimize a mathematical function using binary-encoded individuals. The objective is to find the value of a variable that maximizes a given function within a defined range.

The algorithm represents each candidate solution as a binary string, which is then decoded into a real number. Through iterative evolution, the population improves over time by applying biologically inspired operators such as selection, crossover, and mutation.

---

## 🎯 Objective

The goal of the algorithm is to optimize a function defined over a continuous domain. Each individual encodes a value within a fixed interval, and its fitness is determined by evaluating the function at that point. Over multiple generations, the population evolves toward better solutions.

---

## ⚙️ How It Works

The process begins by generating a population of random binary individuals. Each individual represents a potential solution encoded as a fixed-length bit string. These binary values are mapped to real numbers within a predefined range.

The evolutionary loop consists of the following steps:

- **Selection**: Individuals are chosen using a tournament strategy, where better-performing candidates are more likely to be selected.
- **Crossover**: Pairs of individuals exchange parts of their binary representation, producing new offspring that combine traits from both parents.
- **Mutation**: Random bit flips introduce variability, helping the algorithm explore new regions of the search space.

After each generation, the best individual is identified and tracked, allowing observation of the optimization process.

---

## 🚀 Features

- Binary encoding of real-valued solutions  
- Tournament-based selection  
- Single-point crossover  
- Probabilistic mutation  
- Iterative improvement across generations  

---

## 📈 Outcome

As the algorithm progresses, the population converges toward an optimal or near-optimal solution. The final result represents the best candidate found after all generations, demonstrating how evolutionary strategies can effectively solve optimization problems.
