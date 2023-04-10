import random;
from matplotlib import pyplot as plt;

dist, numSamples=[],1000000

for i in range(numSamples):
    dist.append(random.gauss(0,100)); #평균 0, 표준 편차 100

v=plt.hist(dist,bins=100,weights=[1/numSamples]*len(dist));
plt.xlabel('x')
plt.ylabel('Relative Frequency');
plt.show();

print("Fraction within ~200 of mean =", sum(v[0][30:70]));