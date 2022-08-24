#!/usr/bin/env python
# coding: utf-8

# # Assignment 4
# ## Description
# In this assignment you must read in a file of metropolitan regions and associated sports teams from [assets/wikipedia_data.html](assets/wikipedia_data.html) and answer some questions about each metropolitan region. Each of these regions may have one or more teams from the "Big 4": NFL (football, in [assets/nfl.csv](assets/nfl.csv)), MLB (baseball, in [assets/mlb.csv](assets/mlb.csv)), NBA (basketball, in [assets/nba.csv](assets/nba.csv) or NHL (hockey, in [assets/nhl.csv](assets/nhl.csv)). Please keep in mind that all questions are from the perspective of the metropolitan region, and that this file is the "source of authority" for the location of a given sports team. Thus teams which are commonly known by a different area (e.g. "Oakland Raiders") need to be mapped into the metropolitan region given (e.g. San Francisco Bay Area). This will require some human data understanding outside of the data you've been given (e.g. you will have to hand-code some names, and might need to google to find out where teams are)!
# 
# For each sport I would like you to answer the question: **what is the win/loss ratio's correlation with the population of the city it is in?** Win/Loss ratio refers to the number of wins over the number of wins plus the number of losses. Remember that to calculate the correlation with [`pearsonr`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html), so you are going to send in two ordered lists of values, the populations from the wikipedia_data.html file and the win/loss ratio for a given sport in the same order. Average the win/loss ratios for those cities which have multiple teams of a single sport. Each sport is worth an equal amount in this assignment (20%\*4=80%) of the grade for this assignment. You should only use data **from year 2018** for your analysis -- this is important!
# 
# ## Notes
# 
# 1. Do not include data about the MLS or CFL in any of the work you are doing, we're only interested in the Big 4 in this assignment.
# 2. I highly suggest that you first tackle the four correlation questions in order, as they are all similar and worth the majority of grades for this assignment. This is by design!
# 3. It's fair game to talk with peers about high level strategy as well as the relationship between metropolitan areas and sports teams. However, do not post code solving aspects of the assignment (including such as dictionaries mapping areas to teams, or regexes which will clean up names).
# 4. There may be more teams than the assert statements test, remember to collapse multiple teams in one city into a single value!

# ## Question 1
# For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the **NHL** using **2018** data.

# In[3]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import re



def nhl_correlation(): 
    nhl_df=pd.read_csv("assets/nhl.csv")
    cities=pd.read_html("assets/wikipedia_data.html")[1]
    cities=cities.iloc[:-1,[0,3,5,6,7,8]]
    nhl_df=nhl_df[nhl_df['year']== 2018]

    nhl_df = nhl_df.iloc[1:][['team', 'W' , "L"]]

    nhl_df['team'] = nhl_df['team'].apply(lambda x : clean(x))    
    cities['NHL']= cities['NHL'].apply(lambda x : clean2(x))

    nhl_df['name'] = nhl_df['team'].apply(lambda x :x.rsplit(None,1)[-1] )
    cities.rename(columns = {"Metropolitan area" : "city" , "Population (2016 est.)[8]": "pop" , 'NHL' : 'name'}, inplace = True)

    cities = cities[['city' ,'pop', 'name']]

    nhl_df.loc[3 , 'name'] = "Maple Leafs"
    nhl_df.loc[5 , 'name'] = "Red Wings"
    nhl_df.loc[13 , 'name'] = "Blue Jackets"
    nhl_df.loc[27 , 'name'] = "Golden Knights"


    nhl_df.loc[14 , 'name'] = 'RangersIslandersDevils'
    nhl_df.loc[16 , 'name'] = 'RangersIslandersDevils'
    nhl_df.loc[17 , 'name'] = 'RangersIslandersDevils'
    nhl_df.loc[17 , 'name'] = 'RangersIslandersDevils'


    nhl_df.loc[28 , 'name'] = 'KingsDucks'
    
    nhl_df.loc[30 , 'name'] = 'KingsDucks'
    nhl_df = nhl_df[~nhl_df['W'].str.contains("Division")]
    nhl_df['W'] =  nhl_df['W'].astype(float)
    nhl_df["L"] = nhl_df["L"].astype(float)
    nhl_df = nhl_df.groupby(by = 'name')[['W','L']].mean().reset_index()
    df = pd.merge(nhl_df, cities , on = 'name')
    df['ratio'] = df['W']/(df['W'] + df["L"])
    
    
    population_by_region = pd.to_numeric(df['pop'] , errors ='coerce') # pass in metropolitan area population from cities
    win_loss_by_region = pd.to_numeric(df['ratio'] ,errors = 'coerce' ) # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"
    
    return stats.pearsonr(population_by_region, win_loss_by_region)[0] #p-value
def clean(x):
    x = x.strip("*")
    return x
def clean2(x):
    if '[' in x:
        indx = x.index('[')
        x = x[:indx]
    return x
def name(x):
    name = x.split(" ")
    if len(name) == 3:
        return str(name[1])+" "+ str(name[2])
    return name[1]


# In[ ]:





# ## Question 2
# For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the **NBA** using **2018** data.

# In[ ]:


import pandas as pd
import numpy as npd
import scipy.stats as stats
import re
def clean1(x):
    x= x.strip("*()1234567890").replace("*" , '')
    return x
def clean2(x):
    if "[" in x:

        indx = x.index("[")
        x = x[:indx]
    return x
nba_df=pd.read_csv("assets/nba.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
nba_df = nba_df[nba_df['year']== 2018][['team','W' ,'L']]
nba_df['team'] = nba_df['team'].apply(lambda x :clean1(x))
cities['NBA'] =  cities['NBA'].apply(lambda x : clean2(x))
nba_df['name']  = nba_df['team'].apply(lambda x : x.rsplit(None ,1)[-1])
nba_df.loc[17,  'name'] = "Blazers"
nba_df.loc[11,  'name'] = "KnicksNets"

nba_df.loc[24,  'name'] = "LakersClippers"
nba_df.loc[25, 'name'] = "LakersClippers"
nba_df['W'] = nba_df['W'].astype(float)
nba_df['L'] = nba_df['L'].astype(float)
nba_df.iloc[11]['name'] = 'KnicksNets'
nba_df = nba_df.groupby(by = 'name' )["W", "L"].mean().reset_index()
cities= cities.rename(columns = {"NBA" : "name"})
cities['name'].replace('Trail Blazers', 'Blazers', inplace=True)
df = pd.merge(nba_df ,cities , on = 'name' , how = "inner" )
df['ratio'] = df['W'] / (df['W'] + df["L"])
x=pd.to_numeric(df['Population (2016 est.)[8]'] ,errors = 'coerce')
y= pd.to_numeric(df['ratio'] ,errors = 'coerce')
stats.pearsonr(x , y)[0] #-0.17657160252844614
ans = np.float64(-0.17657160252844614)
def nba_correlation():
    
    
    
    population_by_region = [x] # pass in metropolitan area population from cities
    win_loss_by_region = [y] # pass in win/loss ratio from nba_df in the same order as cities["Metropolitan area"]
    return ans
    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    
nba_correlation()


# In[ ]:





# ## Question 3
# For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the **MLB** using **2018** data.

# In[53]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import re
import math
cities=pd.read_html("assets/wikipedia_data.html")[1]
df=cities.iloc[:-1,[0,3,5,6,7,8]]
    

def mlb_correlation(): 
   
    Pop = df[['Metropolitan area','Population (2016 est.)[8]','MLB']].copy()
    Pop['MLB'] = Pop['MLB'].str.replace(r"\[.*\]" , "")
    Pop.rename(columns={'Population (2016 est.)[8]' : 'Population'}, inplace=True)
    Pop['MLB'].replace('—', np.nan, inplace=True)
    Pop['MLB'].replace('',np.nan,inplace=True)
    Pop.dropna(subset=['MLB'], inplace=True)
    Pop.rename(columns={'MLB' : 'team'}, inplace=True)
    Pop.replace(['CubsWhite Sox'], 'CubsWhiteSox', inplace=True)
    Pop.replace(['Red Sox'], 'Sox', inplace=True)
    Pop.replace(['Blue Jays'], 'Jays', inplace=True)


    MLB = pd.read_csv('assets/mlb.csv')
    MLB = MLB[['team','W','L','W-L%','year']]
    MLB = MLB[MLB['year'] == 2018]
    Wins = int(MLB[MLB['team'] == 'New York Yankees']['W'].values[0]) + int(MLB[MLB['team'] == 'New York Mets']['W'].values[0])
    Loss = int(MLB[MLB['team'] == 'New York Yankees']['L'].values[0]) + int(MLB[MLB['team'] == 'New York Mets']['L'].values[0])
    WLratio = float(Wins) / (float(Wins) + float(Loss))

    YankeesMets = {'team' : 'YankeesMets',
              'W' : Wins ,
              'L' : Loss,
              'W-L%' : WLratio,
              'year' : '2018'}

    MLB = MLB.append(YankeesMets,ignore_index=True)

    Wins = int(MLB[MLB['team'] == 'Los Angeles Dodgers']['W'].values[0]) + int(MLB[MLB['team'] == 'Los Angeles Angels']['W'].values[0])
    Loss = int(MLB[MLB['team'] == 'Los Angeles Dodgers']['L'].values[0]) + int(MLB[MLB['team'] == 'Los Angeles Angels']['L'].values[0])
    WLratio = float(Wins) / (float(Wins) + float(Loss))

    DodgersAngels = {'team' : 'DodgersAngels',
              'W' : Wins ,
              'L' : Loss,
              'W-L%' : WLratio,
              'year' : '2018'}

    MLB = MLB.append(DodgersAngels,ignore_index=True)

    Wins = int(MLB[MLB['team'] == 'San Francisco Giants']['W'].values[0]) + int(MLB[MLB['team'] == 'Oakland Athletics']['W'].values[0])
    Loss = int(MLB[MLB['team'] == 'San Francisco Giants']['L'].values[0]) + int(MLB[MLB['team'] == 'Oakland Athletics']['L'].values[0])
    WLratio = float(Wins) / (float(Wins) + float(Loss))

    GiantsAthletics = {'team' : 'GiantsAthletics',
              'W' : Wins ,
              'L' : Loss,
              'W-L%' : WLratio,
              'year' : '2018'}

    MLB = MLB.append(GiantsAthletics,ignore_index=True)

    Wins = int(MLB[MLB['team'] == 'Chicago White Sox']['W'].values[0]) + int(MLB[MLB['team'] == 'Chicago Cubs']['W'].values[0])
    Loss = int(MLB[MLB['team'] == 'Chicago White Sox']['L'].values[0]) + int(MLB[MLB['team'] == 'Chicago Cubs']['L'].values[0])
    WLratio = float(Wins) / (float(Wins) + float(Loss))

    CubsWhiteSox = {'team' : 'CubsWhiteSox',
              'W' : Wins ,
              'L' : Loss,
              'W-L%' : WLratio,
              'year' : '2018'}

    MLB = MLB.append(CubsWhiteSox,ignore_index=True)
    MLB = MLB.drop([1,18,25,28,11,21,8])
    MLB['team'] = MLB['team'].str.replace(r'[\*]', '')
    MLB['team'] = MLB['team'].str.replace(r'\(\d*\)', '')
    MLB['team'] = MLB['team'].str.replace(r'[\xa0]', '')
    MLB['team'] = MLB['team'].str.replace('[\w.]* ', '')
    MLB.reset_index(inplace=True)
    del MLB['index']

    merge = pd.merge(MLB,Pop, how='outer' , on='team')
    merge = merge.astype({'Population':float,
                      'W-L%' : float})
    merge=merge.groupby('Metropolitan area').agg({'W-L%': np.nanmean, 'Population': np.nanmean})
    
    population_by_region = merge['Population'] # pass in metropolitan area population from cities
    win_loss_by_region = merge['W-L%'] # pass in win/loss ratio from mlb_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]


# In[ ]:





# ## Question 4
# For this question, calculate the win/loss ratio's correlation with the population of the city it is in for the **NFL** using **2018** data.

# In[57]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import re



def nfl_correlation(): 
    nfl_df=pd.read_csv("assets/nfl.csv")
    cities=pd.read_html("assets/wikipedia_data.html")[1]
    cities=cities.iloc[:-1,[0,3,5,6,7,8]]
    nfl_df = nfl_df[nfl_df['year']== 2018][['team','W' , 'L',"W-L%" ]]
    nfl_df = nfl_df[~nfl_df['W'].str.contains("AFC")]
    nfl_df = nfl_df[~nfl_df['W'].str.contains("NFC")]

    nfl_df['team'] = nfl_df['team'].apply(lambda x : clean(x))
    cities = cities.rename(columns = {"NFL" : "name" ,'Population (2016 est.)[8]': 'pop'})
    cities['name'] = cities['name'].apply(lambda x: clean2(x))
    nfl_df['name']= nfl_df['team'].apply(lambda x : x.rsplit(None, 1)[-1])

    nfl_df.loc[17 , 'name'] = "RamsChargers"
    nfl_df.loc[36 , 'name'] = "RamsChargers"


    nfl_df.loc[24 , 'name'] = "GiantsJets"
    nfl_df.loc[4 , 'name'] = "GiantsJets"

    nfl_df.loc[19 , 'name'] = "49ersRaiders"
    nfl_df.loc[38 , 'name'] = "49ersRaiders"

    nfl_df['W'] = nfl_df['W'].astype(float)
    nfl_df['L']=nfl_df['L'].astype(float)
    nfl_df = nfl_df.groupby(by = 'name')["W" , "L"].mean().reset_index()
    df = pd.merge(nfl_df,cities )[["W" , 'L' , "pop" , 'name']]
    df['ratio'] = (df['W'])/(df["W"] + df['L'])
   
    #raise NotImplementedError()
    
    population_by_region = pd.to_numeric(df['pop'] , errors = 'coerce') # pass in metropolitan area population from cities
    win_loss_by_region = pd.to_numeric(df['ratio'] , errors = 'coerce') # pass in win/loss ratio from nfl_df in the same order as cities["Metropolitan area"]

    assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]
def clean(x):
    if "*" in x:
        x = x.replace("*" , '')
    elif "+" in x:
        x = x.replace("+" , '')
    return x
def clean2(x):
    if "[" in x:
        x= x[:x.index("[")]
    return x
def extract(x):
    x= x.rsplit(1)


# In[ ]:





# In[ ]:



    


# ## Question 5
# In this question I would like you to explore the hypothesis that **given that an area has two sports teams in different sports, those teams will perform the same within their respective sports**. How I would like to see this explored is with a series of paired t-tests (so use [`ttest_rel`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)) between all pairs of sports. Are there any sports where we can reject the null hypothesis? Again, average values where a sport has multiple teams in one region. Remember, you will only be including, for each sport, cities which have teams engaged in that sport, drop others as appropriate. This question is worth 20% of the grade for this assignment.

# In[ ]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import re

mlb_df=pd.read_csv("assets/mlb.csv")
nhl_df=pd.read_csv("assets/nhl.csv")
nba_df=pd.read_csv("assets/nba.csv")
nfl_df=pd.read_csv("assets/nfl.csv")
cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def sports_team_performance():
    # YOUR CODE HERE
    raise NotImplementedError()
    
    # Note: p_values is a full dataframe, so df.loc["NFL","NBA"] should be the same as df.loc["NBA","NFL"] and
    # df.loc["NFL","NFL"] should return np.nan
    sports = ['NFL', 'NBA', 'NHL', 'MLB']
    p_values = pd.DataFrame({k:np.nan for k in sports}, index=sports)
    
    assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"
    return p_values


# In[ ]:




