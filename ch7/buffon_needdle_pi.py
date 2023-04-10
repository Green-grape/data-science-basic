#뷔퐁의 바늘을 이용한 pi값 추측
import random;
import math;

def stdDev(vals):
    mean=sum(vals)/len(vals);
    ret=0.0;
    for val in vals:
        ret+=(val-mean)**2;
    return math.sqrt(ret/mean);

def throwNeedles(numNeedles):
    inCircle=0;
    for Needles in range(1, numNeedles+1):
        x=random.random();
        y=random.random();
        if(x**2+y**2<=1.0): inCircle+=1;
    return 4*(inCircle/float(numNeedles));

def getEst(numNeedles, numTrials):
    estimates=[]
    for t in range(numTrials):
        piGuess=throwNeedles(numNeedles);
        estimates.append(piGuess);
    sDev=stdDev(estimates);
    curEst=sum(estimates)/len(estimates);
    print(f'Est={curEst} Std.dev={round(sDev,6)} Needles={numNeedles}');
    return (curEst,sDev);

#오차가 precision내부에 있을 확률이 95%일때 까지 반복
def estPi(precision, numTrials):
    numNeedles=1000;
    sDev=precision;
    while sDev>=precision/2: #신뢰구간 95%이내에 존재
        curEst, sDev=getEst(numNeedles,numTrials);
        numNeedles*=2;
    return curEst;

estPi(0.005, 100);