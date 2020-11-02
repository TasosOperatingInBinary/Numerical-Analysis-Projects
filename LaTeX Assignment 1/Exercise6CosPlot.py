import matplotlib.pyplot as plt
import numpy as np

#Creating the x values and y values of cos(x) functions 
xValues = np.arange(-np.pi,np.pi,0.1)
yValues = np.cos(x)

#Setting the plot's size to 10x10 inches 
plt.figure(figsize=(10,10))

#Setting the step of the values of each axis
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
plt.yticks(np.arange(-1,1.1,0.2))

#Annotating a specific point, in this case ( -pi/4,cos(-pi/4) )
# xytext are the description's string coordinates
plt.scatter(-np.pi/4,np.cos(-np.pi/4))
plt.annotate("cos(-pi/4)", xy=(-np.pi/4,np.cos(-np.pi/4)),  xycoords='data',
            xytext=(0.6, 0.843), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.01),
            horizontalalignment='right', verticalalignment='top',
            )

#Setting labels to the x and y axes and a title to the graph 
plt.xlabel("Θ",fontsize="xx-large")
plt.ylabel("cos(Θ)",fontsize="xx-large")
plt.title("Plot of cos(Θ)",fontsize="xx-large")

#Plotting the two functions
plt.plot(xValues,yValues)