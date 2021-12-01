# -*- coding: utf-8 -*-
"""
Python code of Gravitational Search Algorithm (GSA)
Reference: Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
           Information sciences 179.13 (2009): 2232-2248.	
Coded by: Mukesh Saraswat (saraswatmukesh@gmail.com), Himanshu Mittal (emailid: himanshu.mittal224@gmail.com) and Raju Pal (emailid: raju3131.pal@gmail.com)
The code template used is similar given at link: https://github.com/7ossam81/EvoloPy and matlab version of GSA at mathworks.

Purpose: Main file of Gravitational Search Algorithm(GSA) 
            for minimizing of the Objective Function

Code compatible:
 -- Python: 2.* or 3.*
"""

import random
import numpy
import math
from OAs.GSA.solution import solution
import time
import OAs.GSA.massCalculation as massCalculation
import OAs.GSA.gConstant as gConstant
import OAs.GSA.gField as gField
import OAs.GSA.move as move

        
def GSA(objf,lb,ub,dim,PopSize,iters):
    # GSA parameters
    ElitistCheck =1
    Rpower = 1 
     
    s=solution()
        
    """ Initializations """
    
    vel=numpy.zeros((PopSize,dim))
    fit = numpy.zeros(PopSize)
    M = numpy.zeros(PopSize)
    gBest=numpy.zeros(dim)
    gBestScore=float("inf")
    
    
    #pos=numpy.random.uniform(0,1,(PopSize,dim)) *(ub-lb)+lb
    pos=numpy.random.uniform(0,1,(PopSize,dim)).T# *(ub-lb)+lb
    for i in range (dim):
        pos[i]*(ub[i]-lb[i])+lb[i]
    pos = pos.T
    print('pos:  ', numpy.random.uniform(0,1,(PopSize,dim)).shape)
    
    convergence_curve=numpy.zeros(iters)
    
    print("GSA is optimizing  \""+objf.__name__+"\"")    
    
    timerStart=time.time() 
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    
    for l in range(0,iters):
        for i in range(0,PopSize):
            l1 = [None] * dim
            for k in range(dim):
                l1[k]=numpy.clip(pos[i,:][k], lb[k], ub[k])
            #l1=numpy.clip(pos[i,:], lb, ub)
            #print("l1: ", l1.shape)
            pos[i,:]=l1

            #Calculate objective function for each particle
            fitness=[]
            fitness=objf(l1)
            fit[i]=fitness
    
                
            if(gBestScore>fitness):
                gBestScore=fitness
                gBest=l1           
        
        """ Calculating Mass """
        M = massCalculation.massCalculation(fit,PopSize,M)

        """ Calculating Gravitational Constant """        
        G = gConstant.gConstant(l,iters)        
        
        """ Calculating Gfield """        
        acc = gField.gField(PopSize,dim,pos,M,l,iters,G,ElitistCheck,Rpower)
        
        """ Calculating Position """        
        pos, vel = move.move(PopSize,dim,pos,vel,acc)
        
        convergence_curve[l]=gBestScore
      
        if (l%1==0):
               print(['At iteration '+ str(l+1)+ ' the best fitness is '+ str(gBestScore)])
    timerEnd=time.time()  
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=convergence_curve
    s.Algorithm="GSA"
    s.objectivefunc=objf.__name__
    #s.objectivefunc="Function"

    return s
         
    
