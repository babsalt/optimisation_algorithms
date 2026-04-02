# Genetic algorithm

## Vector representation:

uses a 3d vector of bits such that `vector[projectId][staffId]` equals `1` if the staff member is assigned to the project and `0` if not

```
# example with 4 projects and 5 staff members

vector = [
    [0, 1, 0, 0, 0],   # Project 1 -> Staff 2
    [0, 1, 0, 1, 0],   # Project 2 -> Staff 2, Staff 4 (over assigned)
    [1, 0, 0, 0, 0],   # Project 3 -> Staff 1
    [0, 0, 0, 0, 0],   # Project 4 -> (under assigned)
]
```


<!-- ## Files

*docs*
* `README.md` - this file
* `brief.pdf` - copy of assignment brief

*program*
* `main.py` - simple script that runs genetic algorithm
* `genetic.py` - source code for genetic algorithm (evolving, mutation, crossover)
* `vector.py` - vector representation of project-staff assignments (get cost, random vector, print vector)
* `context.py` - context of situation (staff details, project details)
* `simple_timer.py` - simple timer module -->

<!-- *outputs*
* `genetic_graph.png` - graphical output showing the cost over each generation
* `cost_distribution.png` - small graph to show distribution of random assignment vectors -->

<!-- *misc*
* .gitignore - git ignore file -->


## Running this script
1. Ensure all files are downloaded
2. Navigate to base directory
3. Run `python main.py`
4. See output and note that now `genetic_graph.png` is now generated