import csv
import numpy
import time
import argparse
import warnings

import OAs.GSA.GSA as gsa
from functions.benchmarks import function as benchmark_function

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description="Minimization of 20 benchmark functions")

# Optimization algorithm
parser.add_argument('-is_GSA','--GSA',
                    help="If GSA is to be used",action='store_false')

# Function details
parser.add_argument('-is_f','--function',
                    help="The function to be optimized",action='store_false')
parser.add_argument('-lb1','--lb1',type=int,default=5,
                    help="Lower bound of rho")  
parser.add_argument('-ub1','--ub1',type=int,default=10,
                    help="Upper bound of rho") 
parser.add_argument('-lb2','--lb2',type=int,default=10,
                    help="Lower bound of h")
parser.add_argument('-ub2','--ub2',type=int,default=10,
                    help="Upper bound of h")  
parser.add_argument('-lb3','--lb3',type=int,default=5,
                    help="Lower bound of d")  
parser.add_argument('-ub3','--ub3',type=int,default=10,
                    help="Upper bound of d") 
parser.add_argument('-lb4','--lb4',type=int,default=10,
                    help="Lower bound of v")
parser.add_argument('-ub4','--ub4',type=int,default=10,
                    help="Upper bound of v")                    
parser.add_argument('-dm','--dim',type=int,default=4,
                    help="Dimension/Number of variables")  

# OA parameters
parser.add_argument('-is_exp','--export',help="Whether output .csv to be exported",action='store_false')
parser.add_argument('-p','--pop_size',type=int,default=50,
                    help="Population size")
parser.add_argument('-i','--iter',type=int,default=100,
                    help="Number of iterations")
parser.add_argument('-r','--run',type=int,default=1,
                    help="Number of runs")
args = parser.parse_args()

func = benchmark_function(args.lb1,args.ub1,args.lb2,args.ub2,args.lb3,args.ub3,args.lb4,args.ub4,args.dim)

def selector(algo,func_details,popSize,Iter):
    function_name=func_details[0]
    lb=func_details[1]
    ub=func_details[2]
    dim=func_details[3]
    

    if(algo==0):
        x=gsa.GSA(getattr(func, function_name),lb,ub,dim,popSize,Iter)  
    return x
    
    
# Select optimizers
GSA= args.GSA



# Select benchmark function
F1=args.function # If the function is to be optimized

Algorithm=[GSA]
objectivefunc=[F1]

print(objectivefunc)
        
# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs 
# are executed for each algorithm.
Runs=args.run

# Select general parameters for all optimizers (population size, number of iterations)
PopSize = args.pop_size
iterations= args.iter

#Export results ?
Export=args.export


#ExportToFile="YourResultsAreHere.csv"
#Automaticly generated name by date and time
ExportToFile="experiment"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv" 

# Check if it works at least once
atLeastOneIteration=False


# CSV Header for for the cinvergence 
CnvgHeader=[]

for l in range(0,iterations):
	CnvgHeader.append("Iter"+str(l+1))


for i in range (0, len(Algorithm)):
    for j in range (0, len(objectivefunc)):
        if((Algorithm[i]==True) and (objectivefunc[j]==True)): # start experiment if an Algorithm and an objective function is selected
            for k in range (0,Runs):
                func_details=func.getFunctionDetails(j)
                x=selector(i,func_details,PopSize,iterations)
                if(Export==True):
                    with open(ExportToFile, 'a') as out:
                        writer = csv.writer(out,delimiter=',')
                        if (atLeastOneIteration==False): # just one time to write the header of the CSV file
                            header= numpy.concatenate([["Optimizer","objfname","startTime","EndTime","ExecutionTime"],CnvgHeader])
                            writer.writerow(header)
                        a=numpy.concatenate([[x.Algorithm,x.objectivefunc,x.startTime,x.endTime,x.executionTime],x.convergence])
                        writer.writerow(a)
                    out.close()
                atLeastOneIteration=True # at least one experiment
                
if (atLeastOneIteration==False): # Faild to run at least one experiment
    print("No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions") 
        
        
