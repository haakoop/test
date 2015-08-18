
from numpy import *
from math import *
import matplotlib.pyplot as plt

a0 = 1.0
t0 = 13.5
H0 = 70
Om = 0.3
Ol = 1 - Om
a_ml = a0*(Om/(1-Om))**(1.0/3)

print a_ml

A = a0*(Om/Ol)**(1.0/3)
B = 1.5*sqrt(Ol)
C = sqrt(1-Om)

a_EdS   = linspace(0,1,101)
a_dS    = linspace(0,1,101)
a_lcdm  = linspace(0,1,101)
t       = linspace(0,14,101)

for i in range(len(t)):
    a_dS[i] = 10e-10 + a0*exp((t[i]-t0))

for i in range(len(t)):
    a_EdS[i] = a0*(t[i]/t0)**(2.0/3)

#for i in range(len(t)):
    #a_lcdm[i] = A*(sinh(B*t[i]))**(2.0/3)

for i in range(len(t)):
    if a_lcdm[i-1] < a_ml:
        a_lcdm[i] = a_ml*(1.5*sqrt(1-Om)*H0*t[i])**(2.0/3)
    else:
        a_lcdm[i] = 2**(-2.0/3)*a_ml*exp(C)
    
    

plt.plot(t, a_EdS, label="EdS")
plt.plot(t, a_dS, label="dS")
plt.plot(t, a_lcdm, label="lcdm")
plt.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

plt.title("Universe models")
plt.yscale('log')
#plt.axis((0, 15 , 0.0001 , 1))
plt.show()
