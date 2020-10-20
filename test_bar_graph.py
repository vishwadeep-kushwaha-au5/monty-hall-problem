import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
pos = [1,2,3]
counts = [0,0,0]

def liveG(i):
    gData = open('example.txt','r').read()
    lines = gData.split('\n')

    current_random_selection = random.randint(1,3)
    if(current_random_selection == 1):
        counts[0]+=1
    elif(current_random_selection == 2):
        counts[1]+=1
    else:
        counts[2]+=1
    ax1.clear()
    ax1.bar(pos, counts)
    
    print("Total:"+str(counts[0]+counts[1]+counts[2])+" | "+"1:"+str(counts[0])
                       +" | "+"2:"+str(counts[1])+" | "+"3:"+str(counts[2]))


ani = animation.FuncAnimation(fig, liveG, interval=150)
plt.title('OOG')
plt.show()

