import numpy as np;
import matplotlib.pyplot as plt;

def gradient_descent(xVaLs, yVals, epochs, lr):
    #init
    a=0;b=0;
    for i in range(epochs):
        L=np.mean((yVals-(a*xVaLs+b))**2);
        da=-2*np.mean(xVaLs*(yVals-(a*xVaLs+b))); #dL/da
        db=-2*np.mean((yVals-(a*xVaLs+b))); #dL/db
        a-=da*lr;
        b-=db*lr;
    return a,b;