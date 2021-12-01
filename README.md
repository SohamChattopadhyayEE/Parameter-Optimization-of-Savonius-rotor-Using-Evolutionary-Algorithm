# Parameter Optimization of Savonius rotor Using Evolutionary Algorithm
For some other similar implementation check out : https://github.com/7ossam81/EvoloPy/tree/master/optimizers

## Dependencies
    pip install -r requirements.py

## Arguments
    *\directory> python optimizer.py -h
    usage: optimizer.py [-h] [-is_GSA] [-is_f] [-lb1 LB1] [-ub1 UB1] [-lb2 LB2] [-ub2 UB2] [-lb3 LB3] [-ub3 UB3] [-lb4 LB4] [-ub4 UB4] [-dm DIM] [-is_exp]
                        [-p POP_SIZE] [-i ITER] [-r RUN]

    Minimization of 20 benchmark functions

    optional arguments:
      -h, --help            show this help message and exit
      -is_GSA, --GSA        If GSA is to be used
      -is_f, --function     The function to be optimized
      -lb1 LB1, --lb1 LB1   Lower bound of rho
      -ub1 UB1, --ub1 UB1   Upper bound of rho
      -lb2 LB2, --lb2 LB2   Lower bound of h
      -ub2 UB2, --ub2 UB2   Upper bound of h
      -lb3 LB3, --lb3 LB3   Lower bound of d
      -ub3 UB3, --ub3 UB3   Upper bound of d
      -lb4 LB4, --lb4 LB4   Lower bound of v
      -ub4 UB4, --ub4 UB4   Upper bound of v
      -dm DIM, --dim DIM    Dimension/Number of variables
      -is_exp, --export     Whether output .csv to be exported
      -p POP_SIZE, --pop_size POP_SIZE
                            Population size
      -i ITER, --iter ITER  Number of iterations
      -r RUN, --run RUN     Number of runs
## Execute
    *\directory> python optimizer.py -lb1 0.5 -ub1 2 -lb2 4 -ub2 8 -dim 4
