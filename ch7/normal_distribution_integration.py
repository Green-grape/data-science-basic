import math;
import random;
import matplotlib.pyplot as plt;
import scipy

#정규분포 확률 밀도함수
def gaussian(x, mu, sigma):
    factor1=(1.0/(sigma*math.sqrt(2*math.pi)));
    factor2=math.pow(math.e,-((x-mu)**2)/(2*sigma*sigma**2))
    return factor1*factor2;

def checkEmpirical(numTrials:int):
    for t in range(numTrials):
        mu=random.randint(-10,10)
        sigma=random.randint(1,10);
        print(f' For mu={mu} and sigma={sigma}');
        for numStd in (1,1.96,3): #신뢰도 68%, 95%, 99%
            area=scipy.integrate.quad(gaussian, mu-numStd*sigma, mu+numStd*sigma, (mu,sigma))[0];
            print(f'Fraction within {numStd} std={round(area,4)}');

checkEmpirical(3);