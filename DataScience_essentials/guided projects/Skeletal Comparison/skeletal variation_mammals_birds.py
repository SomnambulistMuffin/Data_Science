// guided project of adult human skeleton data

//loading the data

import pandas as pd
df = pd.read_csv('adult-human-skeleton.csv')
df #display it

// You might have heard the claim that over half the bones in your body are found in your hands and feet. Is this claim true or is it an urban legend?

//Let's count the bones in each region using the
//method. 
df['region'].value_counts()

Earlier we saw that the entire body has 206 bones. 
//Using python, we can calculate what proportion are in the hands and feet. 
//Run the code below: 

(54 + 52) / 206

//over 51% of bones are in the hands
//Baby bones

//Infants have more bones than adults, but as the baby develops, groups of bones fuse together. This is detailed in the 'fused_from' column of our data.

//Let's
//using the fused_from column. 


df.sort_values(by='fused_from', ascending=False)

//
This shows a wide variety of bone fusion across the body. For example, the sternum is formed from the fusion of 6 bones.

//Before all this fusion takes place, how many bones do infants have? We can answer this by calculating the sum()
//of all the fused_from values. 

df['fused_from'].sum()

=305

//Human infants have 305 bones, many of which fuse together, resulting in 206 bones in the adult body.

//Human neck bones

//Necks are quite flexible. How many bones are in the human neck to allow for that flexibility?

//Let's use the query()
//method to find out. 

df.query('region == "neck"')

​	name	region	subregion	side	fused_from
28	hyoid	neck	throat	center	3
29	c1	neck	vertebra	center	3
30	c2	neck	vertebra	center	5
31	c3	neck	vertebra	center	3
32	c4	neck	vertebra	center	3
33	c5	neck	vertebra	center	3
34	c6	neck	vertebra	center	3
35	c7	neck	vertebra	center	3

//The neck has 1 throat bone, and a stack of 7 neck vertebrae, named C1 through C7.

//The "C" stands for cervical, meaning neck. These 7 cervical vertebrae form the top of the spinal column:
    
//    So, humans have 7 neck vertebrae. What about other mammals?
    
// Mammal neck bones

//This project includes the 'mammal-neck-bones.csv' file. Let's load it so we can explore the necks of other mammals.    

mammals = pd.read_csv('mammal-neck-bones.csv')
mammals #display it

​	species	neck_vertebrae
0	cheetah	7
1	impala	7
2	giant panda	7
3	hartebeest	7
4	moose	7
‧‧‧	‧‧‧	‧‧‧
297	alpaca	7
298	common wombat	7
299	red fox	7
300	fennec fox	7
301	california sea lion	7

302 Rows × 2 Columns


The rows shown above all have 7 neck vertebrae, but is this true for all 302 mammals in this dataset?

Let's use a query()
to find the data for giraffes, which we know have really long necks. 

mammals.query('species == "giraffe"')

​	species	neck_vertebrae
108	giraffe	7

Despite their very long necks, giraffes also have 7 neck vertebrae! So, do all mammals have 7 vertebrae?
 We can use another query() to search for any rows where neck_vertebrae is not 7. 
 
mammals.query('neck_vertebrae != 7')

​	species	neck_vertebrae
27	pale-throated sloth	9
28	brown-throated sloth	9
60	hoffmann's two-toed sloth	6
291	west indian manatee	6

Aha! It looks like the only mammals without 7 vertebrae are manatees and sloths. 

Bird neck bones

While mammals mostly have 7 neck vertebrae, what about birds?
 Let's load in 'bird-neck-bones.csv' to explore. 
 
birds = pd.read_csv('bird-neck-bones.csv')
birds #display it

​	species	neck_vertebrae
0	cinereous vulture	13
1	guineafowl	14
2	red-legged partridge	14
3	blue-cheeked parrot	12
4	northern pintail	15
‧‧‧	‧‧‧	‧‧‧
76	barn owl	12
77	eurasian hoopoe	13
78	murre	13
79	new zealand rockwren	13
80	bushwren	13

81 Rows × 2 Columns
[10]


Birds seem to have many more neck vertebrae than mammals.

Let's use series.plot.bar()
to make a quick auto-labeled bar chart of these value counts to get a sense of the distribution.

We will first sort.index()
to show the bird counts ordered by number of neck vertebrae. 

bird_counts = birds['neck_vertebrae'].value_counts()
bird_counts = bird_counts.sort_index()
bird_counts.plot.bar()

 Birds have more diverse neck skeletons.
The most common number of neck vertebrae is 13, but it looks like 23 is the maximum.

Which bird has the maximum number of neck bones? 


birds.query('neck_vertebrae == neck_vertebrae.max()')

​	species	neck_vertebrae
28	mute swan	23
[12]

The beautiful 🦢 Mute Swan 🦢 takes the prize! 

