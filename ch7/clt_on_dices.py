#중심극한정리를 주사위에 적용한것
import random;
import numpy as np;
import matplotlib.pyplot as plt;
import math;

def getMeanAndStd(vals):
    mean=sum(vals)/len(vals);
    variance=0;
    for val in vals:
        variance+=(mean-val)**2;
    variance/=mean;
    return mean, math.sqrt(variance);

#numBins=가로축 구간 개수
def plotMeans(numDice, numRolls, numBins, legend, color,style='bar'):
    means=[]
    for i in range(numRolls//numDice):
        vals=0;
        for j in range(numDice):
            vals+=6*random.random()
        means.append(vals/float(numDice));
    plt.hist(means, numBins, color=color, label=legend, weights=np.array(len(means)*[1])/len(means),histtype=style);
    return getMeanAndStd(means);

mean,std=plotMeans(1,1000000,19, '1dice','b');
print(f'Mean of rolling 1dice mean={mean}, std={mean}')
mean,std=plotMeans(200,1000000,19, '50dice','r');
print(f'Mean of rolling 50dice mean={mean}, std={mean}')
plt.title('Rolling Continuous Dice');
plt.xlabel('Value')
plt.ylabel('Probability')
plt.show();