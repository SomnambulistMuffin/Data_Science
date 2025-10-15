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

