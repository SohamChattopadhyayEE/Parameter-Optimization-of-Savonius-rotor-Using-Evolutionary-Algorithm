# Parameter Optimization of Savonius rotor Using Evolutionary Algorithm
Refer to https://github.com/7ossam81/EvoloPy/tree/master/optimizers for using some other OAs similar to that of GSA. Using GSA following function is optimized 

![function](https://github.com/SohamChattopadhyayEE/Parameter-Optimization-of-Savonius-rotor-Using-Evolutionary-Algorithm/blob/main/images/WhatsApp%20Image%202021-11-24%20at%2013.46.26.jpeg)
## Dependencies
    pip inatall -r requirements.txt
## Arguments
    *\Gravitational-Search-Algorithm> python optimizer.py -h
    usage: optimizer.py [-h] [-is_GSA] [-is_f] [-lb1 LB1] [-ub1 UB1] [-lb2 LB2] [-ub2 UB2] [-lb3 LB3] [-ub3 UB3] [-lb4 LB4] [-ub4 UB4]
                        [-lb5 LB5] [-ub5 UB5] [-lb6 LB6] [-ub6 UB6] [-dm DIM] [-is_exp] [-p POP_SIZE] [-i ITER] [-r RUN]

    Minimization of 20 benchmark functions

    optional arguments:
      -h, --help            show this help message and exit
      -is_GSA, --GSA        If GSA is to be used
      -is_f, --function     The function to be optimized
      -lb1 LB1, --lb1 LB1   Lower bound of rho air
      -ub1 UB1, --ub1 UB1   Upper bound of rho air
      -lb2 LB2, --lb2 LB2   Lower bound of h
      -ub2 UB2, --ub2 UB2   Upper bound of h
      -lb3 LB3, --lb3 LB3   Lower bound of D
      -ub3 UB3, --ub3 UB3   Upper bound of D
      -lb4 LB4, --lb4 LB4   Lower bound of v
      -ub4 UB4, --ub4 UB4   Upper bound of v
      -lb5 LB5, --lb5 LB5   Lower bound of t
      -ub5 UB5, --ub5 UB5   Upper bound of t
      -lb6 LB6, --lb6 LB6   Lower bound of d
      -ub6 UB6, --ub6 UB6   Upper bound of d
      -dm DIM, --dim DIM    Dimension/Number of variables
      -is_exp, --export     Whether output .csv to be exported
      -p POP_SIZE, --pop_size POP_SIZE
                            Population size
      -i ITER, --iter ITER  Number of iterations
      -r RUN, --run RUN     Number of runs
## Execution
    *\Gravitational-Search-Algorithm> python optimizer.py -lb1 0.5 -ub1 20 -lb3 21 -ub3 41 -dim 4 
