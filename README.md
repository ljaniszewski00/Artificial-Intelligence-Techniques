# Artificial-Intelligence-Techniques

## Table of Content
* [General Info](#setup)
* [Technologies](#technologies)
* [Status](#status)
* [Detailed descriptions](#detailed-descriptions)
* [Set 1 - PSO & DE](#exercise-1-pso-&-de) 
* [Set 2 - ](#set-2-)
* [Set 3 - ](#set-3-)

## General info
Implementations of various algorithms used to solve complex problems

## Technologies
Python 3.10

## Status
In Progress

## Detailed descriptions
This app consists of three sets.
The first one consists of PSO (Particle Swarm Optimization) and DE (Differential Evolution) and uses them in order to solve optimization problem with selected function and find it's minimum.
The second one is
The third one is

## Set 1 - PSO & DE    
Particle Swarm Optimization - algorithm can be found in `PSO.py` file      
Differential Evolution - algorithm can be found in `DE.py` file              

### How To Use
After changing directory to `[PROJECT DIR]\Main`, the program can be executed like:

`python .\main.py 1 True 1000 1 20 1 100`

or

`python .\main.py 1 True 1000 1 20 1 100`

or

`python .\main.py 1 True 1000 1 20 1 100`
    
#### Scheme:
`python .\main.py [exercise_number] [static_coefficients] [population_number] [function_number] [dimensions_number] [stop_condition_number] [max_iterations_number_or_accuracy]`
    
#### Where:

**exercise_number** is the number (1-3) used to determine which pair of algorithms are to be executed in order to find solutions:

**static_coefficients** is boolean value determining if coefficients have to stay the same for whole time of algorithm execution or changed iteratively

**population_number** is the number of particles used to find a solution

**function_number** is the number (1-3) of the function which is the target of optimization

**dimensions_number** is the number of dimensions each particle has (depending on the choosen function)

**stop_condition_number** is the number of condition which enables algorithm to be stopped (condition no.1 - max iterations number, condition no.2 - achieved accuracy)

**max_iterations_number_or_accuracy** depending on previously choosen number it can be max iterations number or the accuracy to be achieved

#### What's more:
Function number is one of below:

Function number 1:    
<img src="https://github.com/ljaniszewski00/Artificial-Intelligence-Techniques/blob/master/Assets/Sphere%20function%20description.png?raw=true" width="850" height="80"> 

Function number 2:    
<img src="https://github.com/ljaniszewski00/Artificial-Intelligence-Techniques/blob/master/Assets/Schwefel%20function%20description.png?raw=true" width="850" height="80"> 

Function number 3:     
<img src="https://github.com/ljaniszewski00/Artificial-Intelligence-Techniques/blob/master/Assets/Rosenbrock%20function%20description.png?raw=true" width="850" height="80"> 



## Set 2 -    
 - algorithm can be found in `.py` file      
 - algorithm can be found in `.py` file              

### How To Use

    
#### Scheme:

    
#### Where:


#### What's more:


## Set 3 -    
 - algorithm can be found in `.py` file      
 - algorithm can be found in `.py` file              

### How To Use

    
#### Scheme:

    
#### Where:


#### What's more:

