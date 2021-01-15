import numpy as np

fn = 2.196
q = 1.226
wc = 2*np.pi*56.8*np.power(10, 3)*fn
ho = 2

c1 = 22 * 10**-9  #/ np.power(10, 12)
c2 = 1 * 10**-9 #/ np.power(10, 12)
n = 22

under = 1- (4*q*q*(1+ho))/n
R3 = (1 + np.sqrt(under)) / (2*wc*q*c2)

R3_S = R3
R1 = R3_S / ho

R2 = 1 / (wc*wc*R3_S*c1*c2)

print("R3 = "+str(R3))
print("R1 = "+str(R1))
print("R2 = "+str(R2))