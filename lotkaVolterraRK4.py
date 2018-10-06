
from numpy import *
import pylab as p
from scipy import integrate

# Definition of parameters
a = 0.1
b = 0.02
c = 3
d = 0.01
def dX_dt(X, t=0):
    """ Return the growth rate of fox and rabbit populations. """
    return array([ a*X[0] -   b*X[0]*X[1] ,
                  -c*X[1] + d*b*X[0]*X[1] ])



t = linspace(0,200,40)
  
X0 = array([40,9])                     

X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
infodict['message']                     # >>> 'Integration successful.'

rabbits, foxes = X.T
f1 = p.figure()
p.plot(t, rabbits, 'r-', label='Conejos')
p.plot(t, foxes  , 'b-', label='Zorros')
p.grid()
p.legend(loc='best')
p.xlabel('tiempo')
p.ylabel('poblacion')
p.title('Evolucion de la poblacion de zorros y conejos')
p.show()
#f1.savefig('loktaVolterra.png')