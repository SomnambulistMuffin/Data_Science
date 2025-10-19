//Matplotlib.pyplot is Python's go-to library for
// data visualization. Ready to turn data into charts and graphs? Let's dive in and start plotting! 

//Importing matplotlib pyplot 
import matplotlib.plyplot as plt

//Most of the plotting methods take x and y values as their first two arguments.
// To illustrate, let's plot a simple up/down zig-zag pattern

x = [1,2,3,4,5,6]
y=[1,8,1,8,1,8]				// define x and y values 

plt.plot(x,y)				// plotting values on the graphs
plt.show()					// showing plotted values on a grapho

// the matplot lib aotomatically calls plt.show() after each python script so even if we omit it
// it will still display the plot values

x = [0, 50, 100]
y = [10, 1, 4]
plt.plot(x, y, color = 'red')