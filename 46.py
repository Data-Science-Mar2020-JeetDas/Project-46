# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/46.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project - 46 ");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available country

country = df.groupby(['Location'])[['Period']].count()
print("---------------------------------")
print("\tAvailable country names : ")
print("-------------------------------")
print(country)
print("-------------------------------")
count = 0
for row in range(len(country)): 
        count = count+1
print("total no. of country = ",count)        
print("-----------------------------\n")


# Question - D : Available years data for which data is available

years = df.groupby(['Period'])[['Location']].count()
print("---------------------------------")
print("\tAvailable years data : ")
print("-------------------------------")
print(years)
print("-------------------------------")
count = 0
for row in range(len(years)): 
        count = count+1
print("total no. of years = ",count)        
print("-----------------------------\n")



# Question - E :Types of available indicators

indicator = df.groupby(['Indicator'])[['Period']].count()
print("---------------------------------")
print("\tAvailable types of indicators : ")
print("-------------------------------")
print(indicator)
print("-------------------------------")
count = 0
for row in range(len(indicator)): 
        count = count+1
print("total no. of indicators = ",count)        
print("-----------------------------\n")




#******************* Question - :plot-4: 12-15 (2007-2010) :  ********************



df2 = df[df.Period == 2008]
print("\n\n--------------[ OUTPUT for 2008 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == 2009]
print("\n\n--------------[ OUTPUT for 2009 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])

df4 = df[df.Period == 2010]
print("\n\n--------------[ OUTPUT for 2010 ]----------------------\n\n")
print(df4[['Location','Period','First Tooltip']])



i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)

i3 = np.arange(len(df4['Location']))
print(i3)

#--------------- plot ----------------------

plt.title('Question - : slot-4 : 2008-2010')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2008")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2009")

plt.plot(i3,df4['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2010")

plt.legend()
plt.show()

#******************* Question - :plot-5: 16-19 (2011-2014) :  ********************


df1 = df[df.Period == 2011]
print("\n\n--------------[ OUTPUT for 2011 ]----------------------\n\n")
print(df1[['Location','Period','First Tooltip']])

df2 = df[df.Period == 2012]
print("\n\n--------------[ OUTPUT for 2012 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == 2013]
print("\n\n--------------[ OUTPUT for 2013 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])

df4 = df[df.Period == 2014]
print("\n\n--------------[ OUTPUT for 2014 ]----------------------\n\n")
print(df4[['Location','Period','First Tooltip']])

i = np.arange(len(df1['Location']))
print(i)

i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)

i3 = np.arange(len(df4['Location']))
print(i3)

#--------------- plot ----------------------

plt.title('Question - : slot-5 : 2011-2014')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2011")

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2012")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2013")

plt.plot(i3,df4['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2014")

plt.legend()
plt.show()


#******************* Question - :plot-6: 20-23 (2015-2018) :  ********************


df1 = df[df.Period == 2015]
print("\n\n--------------[ OUTPUT for 2015 ]----------------------\n\n")
print(df1[['Location','Period','First Tooltip']])

df2 = df[df.Period == 2016]
print("\n\n--------------[ OUTPUT for 2016 ]----------------------\n\n")
print(df2[['Location','Period','First Tooltip']])

df3 = df[df.Period == 2017]
print("\n\n--------------[ OUTPUT for 2017 ]----------------------\n\n")
print(df3[['Location','Period','First Tooltip']])

df4 = df[df.Period == 2018]
print("\n\n--------------[ OUTPUT for 2018 ]----------------------\n\n")
print(df4[['Location','Period','First Tooltip']])

i = np.arange(len(df1['Location']))
print(i)

i1 = np.arange(len(df2['Location']))
print(i1)

i2 = np.arange(len(df3['Location']))
print(i2)

i3 = np.arange(len(df4['Location']))
print(i3)

#--------------- plot ----------------------

plt.title('Question - : slot-6 : 2015-2018')
plt.xlabel("Country sl. no --- >")
plt.ylabel("Number(%) --- >")
    
plt.plot(i,df1['First Tooltip'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] 2015")

plt.plot(i1,df2['First Tooltip'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] 2016")

plt.plot(i2,df3['First Tooltip'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] 2017")

plt.plot(i3,df4['First Tooltip'],
            marker='o',
            markersize=10,
            linestyle='dashed',
            label="[4] 2018")

plt.legend()
plt.show()


