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