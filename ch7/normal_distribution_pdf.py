#정규 분포의 확률 밀도 함수

import math;
import matplotlib.pyplot as plt;

#정규분포 확률 밀도함수
def gaussian(x, mu, sigma):
    factor1=(1.0/(sigma*math.sqrt(2*math.pi)));
    factor2=math.pow(math.e,-((x-mu)**2)/(2*sigma*sigma**2))
    return factor1*factor2;

xVals, yVals=[],[];
mu, sigma=0,1
x=-4
while x<=4:
    xVals.append(x)
    yVals.append(gaussian(x,mu,sigma))
    x+=0.05

plt.plot(xVals,yVals);
plt.title(f'Normal Distribution, mu={mu}, sigma={sigma}');
plt.show();

