import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pycountry

directory = r'C:\Users\bloom\workspace\data_engineering'
os.chdir(directory)
#%% Import data
data = pd.read_csv('files/data_cleaned.csv')
data['avg_per_backer'] = data['usd_pledged_real']/data['backers']
data.drop(index, inplace = True)

#%% successrate
succesrate = data['target'].value_counts()[1]/len(data)
print(succesrate)

#%% Group by target
target_grouped = data.groupby('target')

#%% Total amount of money pledged
total_pledged = data['usd_pledged_real'].sum()
pledged_by_target = target_grouped['usd_pledged_real'].sum()
print(total_pledged)
print(pledged_by_target)

#%% Total amount of money pledged
total_pledged_and_given = data[data['target'] == False]['usd_pledged_real'].sum()
print(total_pledged_and_given)

#%% Average amount of backers per project
avg_backers = data['backers'].mean()

print(avg_backers)
#%% Average amount of funds given per backer
avg_per_backer = data['avg_per_backer'].mean()
avg_per_backer_by_target = target_grouped['avg_per_backer'].mean()

print(avg_per_backer)
print(avg_per_backer_by_target)

#%% Average duration
#First drop campaigns with an unrealistic length
index = data[data['time_delta'] > 10000].index
data.drop(index, inplace = True)

#%%
avg_duration = data['time_delta'].describe()
avg_duration_by_target = target_grouped['time_delta'].describe()

print(avg_duration)
print(avg_duration_by_target)

#%% avg goal campaign
avg_goal = data['usd_goal_real'].mean()
avg_goal_by_target = target_grouped['usd_goal_real'].mean()

print(avg_goal)
print(avg_goal_by_target)

#%% avg pledged per campaing
avg_pledged = data['usd_pledged_real'].mean()
avg_pledged_by_target = target_grouped['usd_pledged_real'].mean()

print(avg_pledged)
print(avg_pledged_by_target)

#%% Avg goal grouped by main category
category_grouped = data.groupby('main_category')
avg_goal_by_main_cat = category_grouped['usd_goal_real'].mean()

print(avg_goal_by_main_cat)
    