import numpy as np
import matplotlib.pyplot as plt


levelBreakpoints = [
  2000, 5000, 12000, 25000, 42000, 64000, 100000, 150000,
]


level = 1
totalXp = []
nextLevelXp = 0
currentLevelUpXp = 0


for levelRange in np.arange(0, len(levelBreakpoints)):
  currentBreakpoint = levelBreakpoints[levelRange]
  prevBreakpoint = levelBreakpoints[levelRange - 1] if levelRange >= 1 else 0 
  
  for levelScale in np.arange(2 if level == 1 else 1, 11):
    currentLevelUpXp = nextLevelXp
    nextLevelXp = (pow(levelScale, 2) * (currentBreakpoint - prevBreakpoint)) / 100 + prevBreakpoint
    
    totalXp.append(nextLevelXp)
    print(level, currentLevelUpXp, nextLevelXp - currentLevelUpXp)
    
    level += 1


x = np.arange(1, 80)
xt = np.arange(0, 150000, 15000)
yt = np.arange(0, 80, 5)


plt.plot(x, totalXp)
plt.yticks(xt)
plt.xticks(yt)
plt.show()
