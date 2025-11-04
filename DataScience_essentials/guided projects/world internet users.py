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

100 million is a lot of people, but what percentage of the world's population does that represent?
 To answer this, we need to load in some global population data. 