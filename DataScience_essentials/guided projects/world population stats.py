//World internet users

//The file 'world-internet-users.csv' provides the number of Internet users by year. 
//Here, a user is defined as someone who has accessed the Internet within the last three months. 

import pandas as pd
import matplotlib.pyplot as plt
internet = pd.read_csv('world-internet-users.csv')
internet #display the dataframe

​	year	internet_users
0	1990	3000000
1	1991	4000000
2	1992	7000000
‧‧‧	‧‧‧	‧‧‧
32	2022	5300000000
33	2023	5400000000
34	2024	5450000000

35 Rows × 2 Columns


There are 35 rows of data, representing the years from 1990 to 2024.

In 1990, there were only 3 million Internet users. 

In what year did the number of Internet users exceed 100 million? We can answer this question using a
query(). 

exceeds_100M = internet.query('internet_users > 100e6')
exceeds_100M.head(1)

​	year	internet_users
7	1997	120000000


Internet users went from 3 million in 1990, to over 100 million in 1997.

//100 million is a lot of people, but what percentage of the world's population does that represent?
 //To answer this, we need to load in some global population data. 

World population data

//The file 'historical-world-population.csv' contains world population estimates going back thousands of years.
// load
//in the data and let's see how far back it goes. 

population = pd.read_csv('historical-world-population.csv')
population #display it

​	year	population
0	-10000	4501152
1	-9000	5687125
2	-8000	7314623
‧‧‧	‧‧‧	‧‧‧
122	2020	7887001284
123	2021	7954448405
124	2022	8021407170

125 Rows × 2 Columns


The population estimates go back to the year 10,000 BCE!

Wow, ancient times! 🤯 

Let's merge
these dataframes together so we have the columns from both population and internet_users in one structure. 

Merge the data

There are multiple ways to combine dataframes. When bringing together columns, we suggest using a
left merge
. 

 The merge() method allows you to specify the column to align on. In this case, we want to align on the 'year' column.

//**This left merge will start with all years in the left dataframe,
 and ignore any extra years from the right dataFrame.
 This is useful here because we are not interested in all the years before 1990.
 Especially not all the way back to 10,000 BCE!** //

df = internet.merge(population, on='year', how='left')
df #display


	year	internet_users	population
0	1990	3000000	5327803075
1	1991	4000000	5418735879
2	1992	7000000	5505989821
‧‧‧	‧‧‧	‧‧‧	‧‧‧
32	2022	5300000000	8021407170
33	2023	5400000000	NaN
34	2024	5450000000	NaN

35 Rows × 3 Columns
[4]

Notice how we kept all 35 years of internet_user data, but the last two rows have population values of NaN. 


Here NaN stands for Not a Number, and indicates that no matching population data was found for the years 2023 and 2024. Those last two years were not in the right DataFrame.

Let's drop these incomplete rows using the dropna()
method. This way the NaN values won't interfere with our analysis. 

df = df.dropna()
df #display it


​	year	internet_users	population
0	1990	3000000	5327803075
1	1991	4000000	5418735879
2	1992	7000000	5505989821
‧‧‧	‧‧‧	‧‧‧	‧‧‧
30	2020	4700000000	7887001284
31	2021	4901000000	7954448405
32	2022	5300000000	8021407170

33 Rows × 3 Columns
Looks like it worked. The updated df now has only 33 rows