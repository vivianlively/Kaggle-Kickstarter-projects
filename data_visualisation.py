import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt
import pycountry
import seaborn as sns
import numpy as np


directory = r'C:\Users\bloom\workspace\data_engineering'
os.chdir(directory)
#%% Import data
data = pd.read_csv('files/data_cleaned.csv')
data['avg_per_backer'] = data['usd_pledged_real']/data['backers']
data.drop(index, inplace = True)
#%% Average duration
#First drop campaigns with an unrealistic length
index = data[data['time_delta'] > 10000].index
data.drop(index, inplace = True)
#%% Category 
category_grouped = data.groupby('main_category')
res = category_grouped['usd_goal_real'].mean().sort_values()


print(x)

g = sns.barplot(y = res, 
                x=res.index).set(title = 'Campaign goal (in USD) categorized by category')
plt.xticks(rotation=75)
plt.xlabel('Category')
plt.ylabel('Goal')

#%% Deadline 
month_deadline = pd.to_datetime(data['deadline']).dt.strftime('%b')
data['month_of_deadline']= month_deadline
year_deadline = pd.to_datetime(data['deadline']).dt.strftime('%Y')
data['year_of_deadline']=year_deadline

#%%
group = data.groupby(['year_of_deadline','month_of_deadline','target'])['state'].count()
group = group.reset_index()
group.drop(208, inplace = True)

a = np.array(group[group['target'] == True]['state'])
b = np.array(group[group['target'] == False]['state'])

result = a/(a+b)
series = pd.Series(result)

group_2 = data.groupby(['year_of_deadline','month_of_deadline'])['state'].count()
group_2 = group_2.reset_index()
group_2 = group_2.drop(104)

group_2['succesrate'] = series
group_2.drop('state',axis =1,inplace = True)

heatmap = group_2.pivot('month_of_deadline','year_of_deadline','succesrate')
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
heatmap = heatmap.reindex(index = months)
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(heatmap, linewidths=.5, ax=ax, annot = True)
plt.xlabel('Year of deadline')
plt.ylabel('Month of deadline')
plt.title('Heatmap of successrate of projects by month and year')

#%% Percentage of technology projects
group = data.groupby(['year_of_deadline','month_of_deadline','main_category'])['state'].count()
group = group.reset_index()
group_2 = group[group['main_category']=='Technology']
group_2.drop('main_category', axis =1,inplace = True)
group_3 = data.groupby(['year_of_deadline','month_of_deadline'])['state'].count()
group_3 = group_3.reset_index()
heatmap_2 = group_3.pivot('month_of_deadline','year_of_deadline','state')
heatmap_2 = heatmap_2.reindex(index = months)

heatmap = group_2.pivot('month_of_deadline','year_of_deadline','state')
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

heatmap_3 = heatmap/heatmap_2

f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(heatmap_3, linewidths=.5, ax=ax, annot = True)
plt.xlabel('Year of deadline')
plt.ylabel('Month of deadline')
plt.title('Heatmap of percentage of technology projects by month and year')

#%% Piechart of main_categories
pie_data = data['main_category'].value_counts()
i = data['main_category'].unique()

plt.pie(pie_data, labels = pie_data.index,autopct='%      1.1f%%')
plt.title('Share of main categories in projects')
plt.show()
