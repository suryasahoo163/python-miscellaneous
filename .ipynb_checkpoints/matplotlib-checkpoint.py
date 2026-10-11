import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")
plt.scatter([1,2,3,4],[1,8,0,4],label="first")
plt.title("my plot")
plt.ylabel("this is y axis")
plt.xlabel("this is x axis")
plt.bar([1,2,3,4],[2,4,3,1],color="red",label="second",width=0.01)
plt.legend()
plt.show()