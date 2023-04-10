import math;
import random;
import matplotlib.pyplot as plt;

class Location(object):
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    
    def move(self, deltaX, deltaY):
        return Location(self.x+deltaX, self.y+deltaY);

    def getX(self):
        return self.x;

    def getY(self):
        return self.y;

    def distFrom(self,other):
        xDist=self.x-other.getX();
        yDist=self.y-other.getY();
        return math.sqrt((math.pow(xDist,2)+math.pow(yDist,2)));

    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>';


class Drunk(object):
    def __init__(self, name=None):
        self.name=name;

    def __str__(self):
        if self !=None:
            return self.name;
        return 'Anonymous';

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0,1),(0,-1),(1,0),(-1,0)];
        return random.choice(stepChoices);

#북쪽으로 약간 편향됨
class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0,1.1),(0,-0.9),(1,0),(-1,0)];
        return random.choice(stepChoices);


class Field(object):
    def __init__(self) -> None:
        self.drunks={};

    def addDrunk(self,drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Drunk not in field');
        else: self.drunks[drunk]=loc;

    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field');
        return self.drunks[drunk]
    
    #한 번 움직임
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field');
        xDist, yDist=drunk.takeStep();
        self.drunks[drunk]=self.drunks[drunk].move(xDist,yDist);

class OddField(Field):
    def __init__(self, numHoles=1000, xRange=100, yRange=100) -> None:
        Field.__init__(self);
        self.wormholes={};
        for w in range(numHoles):
            x=random.randint(-xRange,xRange);
            y=random.randint(-yRange,yRange);
            newX=random.randint(-xRange,xRange);
            newY=random.randint(-yRange,yRange);
            newLoc=Location(newX, newY);
            self.wormholes[(x,y)]=newLoc;
    
    def moveDrunk(self, drunk):
        Field.moveDrunk(self,drunk);
        x=self.drunks[drunk].getX();
        y=self.drunks[drunk].getY();
        if (x,y) in self.wormholes:
            self.drunks[drunk]=self.wormholes[(x,y)];

#한번 시뮬레이션
def walk(field:Field, drunk:Drunk, numSteps:int):
    '''
    field: Field 클래스, drunk: Drunk 클래스, numSteps: 움직인 횟수
    '''
    start=field.getLoc(drunk);
    for step in range(numSteps):
        field.moveDrunk(drunk);
    return start.distFrom(field.getLoc(drunk));

#n번 시뮬레이션
def simWalks(numSteps:int, numTrials:int, drunkClass:Drunk, fieldClass:Field):
    tester=drunkClass();
    origin=Location(0,0);
    distances=[];
    for t in range(numTrials):
        f=fieldClass();
        f.addDrunk(tester,origin);
        distances.append(round(walk(f,tester,numSteps),1));
    return distances;

class StyleIterator(object):
    def __init__(self,styles) -> None:
        self.index=0;
        self.styles=styles;

    def nextStyle(self):
        result=self.styles[self.index];
        if self.index==len(self.styles)-1: self.index=0;
        else :self.index+=1;
        return result;


def drunkTest(walkLengths:list, numTrials:int, drunkClass:Drunk,fieldClass:Field):
    for numSteps in walkLengths:
        distances=simWalks(numSteps,numTrials,drunkClass,fieldClass);
        print(drunkClass.__name__+'random walk of', numSteps,'steps');
        print('Mean = ',round(sum(distances)/len(distances),4));
        print('Max =', max(distances), 'Min = ', min(distances));

# def simDrunk(numTrials, drunkClass, walkLengths):
#     meanDistances=[]
#     for numSteps in walkLengths:
#         trials=simWalks(numSteps, numTrials,drunkClass, Field);
#         mean=sum(trials)/len(trials);
#         meanDistances.append(mean);
#     return meanDistances;

# def simAll(drunkKinds, walkLengths, numTrials):
#     styleChoice=StyleIterator(('m-','b--','g--'));
#     for dClass in drunkKinds:
#         curStyle=styleChoice.nextStyle();
#         print('Starting simulation of', dClass.__name__);
#         means=simDrunk(numTrials,dClass,walkLengths);
#         plt.plot(walkLengths,means,curStyle,label=dClass.__name__);
#     plt.title('Mean Distance from Origin ('+str(numTrials)+')');
#     plt.xlabel('Number of Steps');
#     plt.ylabel('Distance from Origin');
#     plt.legend(loc='best');
#     plt.show();

#simAll([UsualDrunk, MasochistDrunk], list(range(1000)),100);


def walkCoord(field:Field, drunk:Drunk, numStep:int):
    '''
    field: Field 클래스, drunk: Drunk 클래스, numSteps: 움직인 횟수
    '''
    start=field.getLoc(drunk);
    for step in range(numStep):
        field.moveDrunk(drunk);
    return field.getLoc(drunk);

def simDrunk(numStep:int, numTrials:int, drunkClass:Drunk, fieldClass:Field):
    tester=drunkClass();
    origin=Location(0,0);
    locations=[];
    for t in range(numTrials):
        f=fieldClass();
        f.addDrunk(tester,origin);
        locations.append(walkCoord(f,tester,numStep));
    return locations;

def simAll(drunkKinds, numStep, numTrials):
    styleChoice=StyleIterator(('r^','k+'));
    for dClass in drunkKinds:
        curStyle=styleChoice.nextStyle();
        print('Starting simulation of', dClass.__name__);
        locations=simDrunk(numStep,numTrials, dClass,Field);
        locationsX=[];locationsY=[];
        for loc in locations:
            locationsX.append(loc.getX());
            locationsY.append(loc.getY());
        plt.plot(locationsX,locationsY,curStyle,label=dClass.__name__);
    plt.title('Location at End of walks ('+str(numStep)+')');
    plt.xlabel('Steps East/West of Origin');
    plt.ylabel('Steps North/South of Origin');
    plt.legend(loc='best');
    plt.show();


simAll([UsualDrunk, MasochistDrunk],10000,1000);

