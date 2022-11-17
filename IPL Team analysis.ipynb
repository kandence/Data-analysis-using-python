#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


#Reading data from the dataset
match_data = pd.read_csv("C:/Users/HP/OneDrive/Desktop/IPL Dataset/IPL Matches 2008-2020.csv")
ball_data = pd.read_csv("C:/Users/HP/OneDrive/Desktop/IPL Dataset/IPL Ball-by-Ball 2008-2020.csv")


# In[5]:


match_data.head()


# In[6]:


ball_data.head()


# In[7]:


#Checks whether there is null value in dataset
match_data.isnull().sum()


# In[8]:


ball_data.isnull().sum()


# In[9]:


match_data.shape


# In[10]:


ball_data.shape


# In[11]:


match_data.columns


# In[12]:


print('Matches played so far:', match_data.shape[0])
print('\n Cities played at:', match_data['city'].unique())
print('\n Teams participated: ', match_data['team1'].unique())


# In[13]:


match_data['Season'] = pd.DatetimeIndex(match_data['date']).year
match_data.head()


# In[14]:


#Total no of matches played each season
match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id': 'matches'})
match_per_season


# In[15]:


#Plotting total no of matches played each season 
sns.countplot(match_data['Season'])
plt.xticks(rotation = 90, fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlabel('Season', fontsize =10)
plt.ylabel('Count', fontsize =10)
plt.title('Total maches played in each season', fontweight = "bold")


# In[16]:


#Merge columns from two dataset
season_data = match_data[['id', 'Season']].merge(ball_data, left_on = 'id', right_on = 'id', how = 'left').drop('id', axis = 1)
season_data.head()


# In[19]:


#Total no of runs each season
season = season_data.groupby(['Season'])['total_runs'].sum().reset_index()
p = season.set_index('Season')
ax = plt.axes()
ax.set(facecolor = "grey")
sns.lineplot(data = p, palette = "magma")
plt.title('Total runs in each season', fontsize = 12, fontweight = "bold")
plt.show()


# In[21]:


#Runs scored per match
runs_per_season = pd.concat([match_per_season, season.iloc[:,1]], axis = 1)
runs_per_season['Runs scored per match'] = runs_per_season['total_runs']/runs_per_season['matches']
runs_per_season.set_index('Season', inplace= True)
runs_per_season


# In[22]:


# No of tosses won by each team
toss = match_data['toss_winner'].value_counts()
ax = plt.axes()
ax.set(facecolor = "grey")
sns.set(rc = {'figure.figsize': (15, 10)}, style = 'darkgrid')
ax.set_title('No. of tosses won by each team', fontsize = 15, fontweight = "bold")
sns.barplot(y = toss.index, x = toss, orient = 'h', palette = "icefire", saturation = 1)
plt.xlabel('# of toss won')
plt.ylabel('Team')
plt.show()


# In[23]:


#Checks what team chose after winning the toss
ax = plt.axes()
ax.set(facecolor = "grey")
sns.countplot(x = 'Season', hue = 'toss_decision', data = match_data, palette = "magma", saturation  = 1)
plt.xticks(rotation = 90, fontsize = 10)
plt.yticks(fontsize = 15)
plt.xlabel('\n Season', fontsize = 15)
plt.ylabel('Count', fontsize = 15)
plt.title('Toss decision across seasons', fontsize = 12, fontweight = "bold")
plt.show()


# In[24]:


match_data['result'].value_counts()


# In[25]:


#Checks best venue for winning by runs
match_data.venue[match_data.result!= 'runs'].mode()


# In[28]:


#Checks best venue for fielding and winning the match
match_data.venue[match_data.result != 'wickets'].mode()


# In[29]:


match_data.venue[match_data.toss_winner == 'Kings XI Punjab'][match_data.winner == 'Kings XI Punjab'].mode()


# In[30]:


match_data.winner[match_data.result!='runs'].mode()


# In[31]:


match_data.winner[match_data.result!='wickets'].mode()


# In[32]:


toss = match_data['toss_winner'] == match_data['winner']
plt.figure(figsize = (10, 5))
sns.countplot(toss)
plt.show()


# In[33]:


plt.figure(figsize = (12, 4))
sns.countplot(match_data.toss_decision[match_data.toss_winner == match_data.winner])
plt.show()


# In[35]:


player = (ball_data['batsman'] == 'SK Raina')
df_raina = ball_data[player]
df_raina.head()


# In[36]:


df_raina['dismissal_kind'].value_counts().plot.pie(autopct = '%1.1f%%', shadow = True, rotatelabels = True)
plt.title("Dismissal kind", fontweight = "bold", fontsize = 15)
plt.show()


# In[38]:


def count(df_raina, runs):
    return len(df_raina[df_raina['batsman_runs'] == runs])*runs


# In[39]:


print("Runs scored from 1's: ", count(df_raina, 1))
print("Runs scored from 2's: ", count(df_raina, 2))
print("Runs scored from 3's: ", count(df_raina, 3))
print("Runs scored from 4's: ", count(df_raina, 4))
print("Runs scored from 6's: ", count(df_raina, 6))


# In[40]:


match_data[match_data['result_margin']==match_data['result_margin'].max()]


# In[45]:


runs  =  ball_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
runs.columns = ['Batsman', 'runs']
y = runs.sort_values(by = 'runs', ascending = False).head(10).reset_index().drop('index', axis = 1)
y


# In[46]:


ax  = plt.axes()
ax.set(facecolor = "grey")
sns.barplot(x = y['Batsman'], y = y['runs'], palette = 'rocket', saturation = 1)
plt.xticks(rotation = 90, fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlabel('\n Player', fontsize = 15)
plt.ylabel('Total Runs', fontsize = 15)
plt.title('Top 10 run scorers in IPL', fontsize = 15, fontweight = "bold")


# In[47]:


ax = plt.axes()
ax.set(facecolor = "black")
match_data.player_of_match.value_counts()[:10].plot(kind = 'bar')
plt.xlabel('Players')
plt.ylabel("Count")
plt.title("Highest MOM award winners", fontsize = 15, fontweight = "bold")


# In[ ]:




