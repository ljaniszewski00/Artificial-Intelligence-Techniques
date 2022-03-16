# Artificial-Intelligence-Techniques

## Table of Content
* [General Info](#setup)
* [Technologies](#technologies)
* [Status](#status)
* [Detailed descriptions and algorithms](#detailed-descriptions-and-algorithms)
* [How To Use](#how-to-use)
* [How It Works](#how-it-works)
* [Examples Of Use](#examples-of-use)

## General info
Implementations of various algorithms used to solve complex problems

## Technologies
Python 3.10

## Status
In Progress

## Detailed descriptions and algorithms
This app consists of three exercices.
The first one is the comparison of PSO (Particle Swarm Optimization) and DE (Differential Evolution) used in order to solve optimization problem with selected function and find it's minimum
The second one is
The third one is

### Particle Swarm Optimization - algorithm
1. For every particle from set:
    1. Assign random starting position from given range
    2. Calculate the current value of function with every particle's position
    3. Save current position of the particle as it's best local solution
    4. If particle's position is better than the global solution, assign it as global one
    5. Assign random starting velocities for all particles
2. If end condition has not been made (max iteration number or given accuracy):    
    For every particle from set:    
        1. Update velocities for every particle with the formula:    
            v = w * v + (c1 * r1) * (Pbest - Pi) + (c2 * r2) * (Gbest - Pi)    
                where:    
                    v - particle's velocity    
                    w - static parameter = 0.72984    
                    c1, c2 - static parameters = 2.05    
                    r1, r2 - weights with random values from set [0, 2]    
                    Pbest - current particle's best solution    
                    Gbest - global best solution    
                    Pi - current solution    
                 additionally, parameters w, c1, c2 can be updated, for better results, over the iterations with formulas:    
                    w = ((0.4 * (t - N)) / N^2) + 0.4    
                    c1 = (-3 * (t / N)) + 3.5    
                    c2 = (3 * (t / N)) + 0.5    
                        where:    
                            t - current iteration    
                            N - all iterations number    
        2. Update positions for every particle with the formula:    
            Pi = Pi + v    
                where:    
                    Pi - particle's position    
                    v - particle's velocity     
        3. If particle's new position is better than local's best solution, assign it as local's best    
        4. If particle's new position is better than global's best solution, assign it as global's best     


### Differential Evolution - algorithm   


## How To Use
After changing directory to `[PROJECT DIR]\Main`
#### The program can be executed like:

`python .\main.py 1 True 1000 1 20 1 100`

or

`python .\main.py 1 True 1000 1 20 1 100`

or

`python .\main.py 1 True 1000 1 20 1 100`
    
#### Scheme:
`python .\main.py [exercise_number] [static_coefficients] [population_number] [function_number] [dimensions_number] [stop_condition_number] [max_iterations_number_or_accuracy]`
    
#### Where:

[exercise_number] is the number (1-3) used to determine which pair of algorithms are to be executed in order to find solutions:

[static_coefficients] is boolean value determining if coefficients have to stay the same for whole time of algorithm execution or changed iteratively

[population_number] is the number of particles used to find a solution

[function_number] is the number (1-3) of the function which is the target of optimization

[dimensions_number] is the number of dimensions each particle has (depending on the choosen function)

[stop_condition_number] is the number of condition which enables algorithm to be stopped (condition no.1 - max iterations number, condition no.2 - achieved accuracy)

[max_iterations_number_or_accuracy] depending on previously choosen number it can be max iterations number or the accuracy to be achieved

#### What's more:
Function number is one of below functions:

Function number 1:    
<img src="https://github.com/ljaniszewski00/Artificial-Intelligence-Techniques/blob/master/Assets/Sphere%20function%20description.png?raw=true" width="750" height="100"> 

Function number 2:    
<img src="https://github.com/ljaniszewski00/Artificial-Intelligence-Techniques/blob/master/Assets/Schwefel%20function%20description.png?raw=true" width="750" height="100"> 

Function number 3:     
<img src="https://github.com/ljaniszewski00/Artificial-Intelligence-Techniques/blob/master/Assets/Rosenbrock%20function%20description.png?raw=true" width="750" height="100"> 

## How It Works


## Examples Of Use

`PS [YOUR DIRECTORY]\Artificial Intelligence Techniques\Main> python .\main.py 1 True 1000 1 20 1 100`

#### Console Output
<img src="https://github.com/ljaniszewski00/Artificial-Intelligence-Techniques/blob/master/Assets/Sphere%20function%20description.png?raw=true" width="750" height="100"> 


