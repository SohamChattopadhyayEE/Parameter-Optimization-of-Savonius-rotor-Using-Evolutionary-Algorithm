import numpy
import math
class function():
  def __init__(self, lb1, ub1, lb2, ub2, lb3, ub3, lb4, ub4, lb5, ub5, dim):
    self.lb1 = lb1
    self.ub1 = ub1
    self.lb2 = lb2
    self.ub2 = ub2
    self.lb3 = lb3
    self.ub3 = ub3
    self.lb4 = lb4
    self.ub4 = ub4
    self.lb5 = lb5
    self.ub5 = ub5
    self.dim = dim
  def F1(self,x):
    s = (8/27)
    for i in range(4):
      if i==3:
          s *= x[i]**3
      else :
          s *= x[i]
    s += (1/2)*x[0]*x[1]*(numpy.pi*((x[2]+x[4])/2)**2-numpy.pi*(x[3]**2)/4)
    return s

  def getFunctionDetails(self, a):
    # [name, lb, ub, dim]
    param = {  0: ["F1",[self.lb1,self.lb2,self.lb3,self.lb4,self.lb5],[self.ub1,self.ub2,self.ub3,self.ub4,self.ub5],self.dim],
              }

    return param.get(a, "nothing")



