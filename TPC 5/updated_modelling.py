import numpy as np

# Constants
S1BR = 0; S2br = 1; S2bR = 2; S2BR = 3; S3br = 4; S3bR = 5; S3BR = 6;
S4br = 7; S4bR = 8; S4BR = 9; S5br = 10; S5bR = 11; S5BR = 12;
S6BR = 13; S7bR = 14; S7BR = 15
UP = 0; DOWN = 1; LEFT = 2; RIGHT = 3
GAMMA = 0.99

X = ("1BR", "2br", "2bR", "2BR", "3br", "3bR", "3BR", "4br",
     "4bR", "4BR", "5br", "5bR", "5BR", "6BR", "7bR", "7BR")
print("States: {}\n".format(X))

A = ("U", "D", "L", "R")
print("Actions: {}\n".format(A))

# Action U(p)
PU = np.zeros((len(X), (len(X))))
PU[S1BR, S1BR] = 1
PU[S2br, S2br] = 1
PU[S2bR, S2bR] = 1
PU[S2BR, S2BR] = 1
PU[S3br, S3br] = 1
PU[S3bR, S3bR] = 1
PU[S3BR, S3BR] = 1
PU[S4br, S2br] = 0.8
PU[S4bR, S2bR] = 0.8
PU[S4BR, S2BR] = 0.8
PU[S4br, S4br] = 0.2
PU[S4bR, S4bR] = 0.2
PU[S4BR, S4BR] = 0.2
PU[S5br, S3br] = 0.8                                                                                                                                                                         
PU[S5bR, S3bR] = 0.8                                                                                                                                                                         
PU[S5BR, S3BR] = 0.8                                                                                                                                                                         
PU[S5br, S5br] = 0.2                                                                                                                                                                         
PU[S5bR, S5bR] = 0.2                                                                                                                                                                         
PU[S5BR, S5BR] = 0.2                                                                                                                                                                         
PU[S6BR, S6BR] = 1                                                                                                                                                                           
PU[S7bR, S4bR] = 0.8                                                                                                                                                                         
PU[S7BR, S4BR] = 0.8                                                                                                                                                                         
PU[S7bR, S7bR] = 0.2                                                                                                                                                                         
PU[S7BR, S7BR] = 0.2

print("Transition Probability Matrix for Up action: \n{}\n".format(PU))

# Action D(own)
PD = np.zeros((len(X), (len(X))))
PD[S1BR, S1BR] = 1
PD[S2br, S2br] = 0.2
PD[S2bR, S2bR] = 0.2
PD[S2BR, S2BR] = 0.2
PD[S2br, S4br] = 0.8
PD[S2bR, S4bR] = 0.8
PD[S2BR, S4BR] = 0.8
PD[S3br, S3br] = 0.2
PD[S3bR, S3bR] = 0.2
PD[S3BR, S3BR] = 0.2
PD[S3br, S5br] = 0.8
PD[S3bR, S5bR] = 0.8
PD[S3BR, S5BR] = 0.8
PD[S4br, S4br] = 0.2
PD[S4bR, S4bR] = 0.2
PD[S4BR, S4BR] = 0.2
PD[S4br, S7bR] = 0.8
PD[S4bR, S7bR] = 0.8
PD[S4BR, S7BR] = 0.8
PD[S5br, S5br] = 1
PD[S5bR, S5bR] = 1
PD[S5BR, S5BR] = 1
PD[S6BR, S6BR] = 1
PD[S7bR, S7bR] = 1
PD[S7BR, S7BR] = 1
print("Transition Probability Matrix for Down action: \n{}\n".format(PD))

# Action L(eft)
PL = np.zeros((len(X), (len(X))))
PL[S1BR, S1BR] = 1
PL[S2bR, S1BR] = 0.8
PL[S2BR, S1BR] = 0.8
PL[S2bR, S2bR] = 0.2
PL[S2BR, S2BR] = 0.2
PL[S2br, S2br] = 1
PL[S3br, S2br] = 0.8
PL[S3bR, S2bR] = 0.8
PL[S3BR, S2BR] = 0.8
PL[S3br, S3br] = 0.2
PL[S3bR, S3bR] = 0.2
PL[S3BR, S3BR] = 0.2
PL[S4br, S4br] = 1
PL[S4bR, S4bR] = 1
PL[S4BR, S4BR] = 1
PL[S5br, S4br] = 0.8
PL[S5bR, S4bR] = 0.8
PL[S5BR, S4BR] = 0.8
PL[S5br, S5br] = 0.2
PL[S5bR, S5bR] = 0.2
PL[S5BR, S5BR] = 0.2
PL[S6BR, S5BR] = 0.8
PL[S6BR, S6BR] = 0.2
PL[S7bR, S7bR] = 1
PL[S7BR, S7BR] = 1
print("Transition Probability Matrix for Left action: \n{}\n".format(PL))

# Action R(ight)
PR = np.zeros((len(X), (len(X))))
PR[S1BR, S1BR] = 0.2
PR[S1BR, S2BR] = 0.8
PR[S2br, S2br] = 0.2
PR[S2bR, S2bR] = 0.2
PR[S2BR, S2BR] = 0.2
PR[S2br, S3br] = 0.8
PR[S2bR, S3bR] = 0.8
PR[S2BR, S3BR] = 0.8
PR[S3br, S3br] = 1
PR[S3bR, S3bR] = 1
PR[S3BR, S3BR] = 1
PR[S4br, S4br] = 0.2
PR[S4bR, S4bR] = 0.2
PR[S4BR, S4BR] = 0.2
PR[S4br, S5br] = 0.8
PR[S4bR, S5bR] = 0.8
PR[S4BR, S5BR] = 0.8
PR[S5BR, S5BR] = 0.2
PR[S5br, S5br] = 1
PR[S5bR, S5bR] = 1
PR[S5BR, S6BR] = 0.8
PR[S6BR, S6BR] = 1
PR[S7bR, S7bR] = 1
PR[S7BR, S7BR] = 1
print("Transition Probability Matrix for Right action: \n{}\n".format(PR))

Ps = np.array([PU, PD, PL, PR])

# Cost
C = np.ones((len(X), len(A)))
C[S6BR, :] = 0
print("Cost Function: \n{}\n".format(C))
