import pandas as pd
pd.DataFrame()

//putting data in a data frame

df = pd.DataFrame()
df['color'] = ['blue','red','yellow','green']
df['radius'] = [2,4,3,5]
df #show result

//displaying diameter of a circle

df['diameter'] = df['radius'] * 2
df #output result

// small radius
df['radius'].min( )

// add all diameter
df['diameter'].sum( )

//average radius
df['radius'].mean( )

//column as a series
2
df['color']

// rows as series
df.iloc[0]      // iloc stands for integer location and the [0] is for the first row
df.iloc[1]  //second row
df.iloc[2]  //third row
df.iloc[-1] //last row

// negative integers let you count backwards from last row

df.index // row labels
df.columns  //column names
df.shape // size of rows and columns 

// reading data from .csv textfiles 

layers = pd.read_csv('earth-layers.csv')        // access file and instantiate it 
layers      //display file contents

//adding up the values of the dataframe layers of earth's thickness to display totals 
layers['thickness'].sum()



