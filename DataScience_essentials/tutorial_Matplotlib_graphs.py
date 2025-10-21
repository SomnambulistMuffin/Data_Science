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

//basic plotting methods

//line plot methods
a = [1,2,3,4]
b = [1,4,3,4]

plt.plot(a,b)

//bar charts
a = ['A','B','C']
b = [4,1,2]
plt.bar(a,b)

//horizontal bar chart
a= ['A','B','C']
b= [4,1,2]
plt.barh(a,b)

//scatterplot chart
a= [1,2,3,4]
b= [1,4,3,4]
plt.scatter(a,b)

//plotting dataframes
//matplotlib integrates seamlessly with pandas so it's easy to plot graphs from dataframes 

import pandas as pd         //import pandas

df = pd.read_csv('earth-layers.csv')        //load earth-layers.csv into var df

df      //display

x= df['layer']      //define x as layer name
y= df['thickness']  //define y as the thickness

plt.bar(x,y)        //bar chart creation

//Labels and titles
// matplot lib gives methods to add labels to graphs  on x and y axis

plt.bar(df['layer'],df['thickness'])
plt.ylabel('Thickness(km)')
plt.title('Layers of the Earth')
