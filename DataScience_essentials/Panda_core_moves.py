//** The following three methods are central to dataframe workflows used throughout this course:

    df.eval(): Does calculations.
    df.query(): Finds rows.
    df.groupby(): Builds groups of rows.

We'll first explore each core move on its own, then combine them to tackle multistep tasks.**//

//DataFrame.eval()
//Does calculations
//efficient way to create new columns from a formula

import pandas as pd

df = pd.read_csv('right-triangles.csv')

df

// Let's use eval() to calculate the area for each triangle. Recall that the area formula for a triangle is:

Area = 1/2 × Base × Height

Using the * symbol for multiplication, evaluate this formula to create a new area column. **//

df['area'] = df.eval('0.5*base*height')

df // display dataframe

//DataFrame.query()

//** The query() method finds rows for a given condition.
 It's an efficient way to filter a dataframe and get the rows you want. **//
 
 months  = pd.read_csv('days-per-month.csv')
 months
 
 this data is about the number of days in each month
 let's find months with more than 30 days
 
 months.query('days>30')
 
 query for the months with the fewest days
 months.query('days == days.min()')
 
 //DataFrame.groupby()
 //**The groupby() method groups rows that share a common value.
 Once grouped, we can perform aggregation calculations, such as min(), max(), mean() and sum(). **//
 
 df = pd.read_csv('fruit-weights.csv')
 df
 
 //Let's calculate the average weight for each type of fruit.
 We first group the rows by the 'fruit' column using the groupby() method. **//
 
 groups = df.groupby('fruit')
 groups
 
 //**
The groupby() method formed 3 groups for the 3 types of fruit

This structure allows us to perform grouped calculations on column values.

Let's calculate the mean for the weight column of each group. **//
groups['weight].mean()

//This gave us a series object where the index is the fruit. 
//We can turn the index into a column using reset_index(). 
This will convert the series into a dataframe. **//

groups = df.groupby('fruit')
series = groups['weight'].mean()
series.reset_index()

// Now we have a dataframe 🎉.

This entire groupby calculation is often done as a single line of code, like this: **//

df.groupby('fruit')['weight'].mean().rest_index()


