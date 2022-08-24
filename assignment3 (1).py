#!/usr/bin/env python
# coding: utf-8

# # Assignment 3
# All questions are weighted the same in this assignment. This assignment requires more individual learning then the last one did - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. All questions are worth the same number of points except question 1 which is worth 17% of the assignment grade.
# 
# **Note**: Questions 3-13 rely on your question 1 answer.

# In[1]:


import pandas as pd
import numpy as np

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings
warnings.filterwarnings('ignore')


# ### Question 1
# Load the energy data from the file `assets/Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](assets/Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **Energy**.
# 
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
# 
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]`
# 
# Convert `Energy Supply` to gigajoules (**Note: there are 1,000,000 gigajoules in a petajoule**). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# 
# Rename the following list of countries (for use in later questions):
# 
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, e.g. `'Bolivia (Plurinational State of)'` should be `'Bolivia'`.  `'Switzerland17'` should be `'Switzerland'`.
# 
# Next, load the GDP data from the file `assets/world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. 
# 
# Make sure to skip the header, and rename the following list of countries:
# 
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
# 
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `assets/scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# 
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 
# 
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# 
# *This function should return a DataFrame with 20 columns and 15 entries, and the rows of the DataFrame should be sorted by "Rank".*

# In[2]:


def answer_one():
    energy= pd.read_excel('assets/Energy Indicators.xls')
    cols = list(energy.columns)[2:6]
    energy = energy[cols].rename(columns ={'Unnamed: 2' : "Country" ,'Unnamed: 3' :'Energy Supply' ,
                                   'Unnamed: 4':'Energy Supply per Capita'  ,'Unnamed: 5' : '% Renewable'})
    energy['Country']= energy['Country'].fillna("0").apply(lambda x : renam(x))
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy.at['110', 'Country'] = "Iran"
    energy.at['110', 'Energy Supply'] = 9172000000
    energy.at['110', 'Energy Supply per Capita'] = 119.0
    energy.at['110', '% Renewable'] =  5.71
    GDP = pd.read_csv("assets/world_bank.csv", skiprows=4)
    GDP['Country Name']=GDP['Country Name'].fillna("0").apply(lambda x: renam2(x))
    GDP = GDP.rename(columns= {'Country Name' : "Country"})
    ScimEn = pd.read_excel('assets/scimagojr-3.xlsx') 
    df = pd.merge(pd.merge(ScimEn,GDP, how='inner', left_on='Country', right_on='Country')
              ,energy, how='inner', left_on='Country', right_on='Country' )
    cols = list(df.columns)[ : 8] + list(df.columns)[67: ]+ list(df.columns)[57:67]
    df = df[cols]
    df = df.set_index('Country')
    df.sort_values(by=['Rank'], inplace=True)
    

    return df.head(15)
    raise NotImplementedError()
def renam(x):
    x = x.strip("1234567890()")
    if x =='Republic of Korea':
        return 'South Korea'
    elif x =='United States of America':
        return  'United States'
    elif x == 'United Kingdom of Great Britain and Northern Ireland':
        return 'United Kingdom'
    elif x == 'China, Hong Kong Special Administrative Region':
        return 'Hong Kong'
    return x 

def renam2(x):
     
    if x =='Korea, Rep.':
        return 'South Korea'
    elif x =='Iran, Islamic Rep.':
        return  'Iran'
    elif x == 'Hong Kong SAR, China':
        return 'Hong Kong'
    return x


# In[3]:


def renam(x):
    x = x.strip("1234567890()")
    if x =='Republic of Korea':
        return 'South Korea'
    elif x =='United States of America':
        return  'United States'
    elif x == 'United Kingdom of Great Britain and Northern Ireland':
        return 'United Kingdom'
    elif x == 'China, Hong Kong Special Administrative Region':
        return 'Hong Kong'
    return x 

def renam2(x):
     
    if x =='Korea, Rep.':
        return 'South Korea'
    elif x =='Iran, Islamic Rep.':
        return  'Iran'
    elif x == 'Hong Kong SAR, China':
        return 'Hong Kong'
    return x
energy= pd.read_excel('assets/Energy Indicators.xls')
cols = list(energy.columns)[2:6]
energy = energy[cols].rename(columns ={'Unnamed: 2' : "Country" ,'Unnamed: 3' :'Energy Supply' ,
                                   'Unnamed: 4':'Energy Supply per Capita'  ,'Unnamed: 5' : '% Renewable'})
energy['Country']= energy['Country'].fillna("0").apply(lambda x : renam(x))
energy['Energy Supply'] = energy['Energy Supply']*1000000
energy.at['110', 'Country'] = "Iran"
energy.at['110', 'Energy Supply'] = 9172000000
energy.at['110', 'Energy Supply per Capita'] = 119.0
energy.at['110', '% Renewable'] =  5.71
GDP= pd.read_csv("assets/world_bank.csv", skiprows=4)
GDP['Country Name']=GDP['Country Name'].fillna("0").apply(lambda x: renam2(x))
GDP = GDP.rename(columns= {'Country Name' : "Country"})
ScimEn = pd.read_excel('assets/scimagojr-3.xlsx') 
df = pd.merge(pd.merge(ScimEn,GDP, how='inner', on='Country')
              ,energy, how='inner', on='Country')
df


# In[4]:


assert type(answer_one()) == pd.DataFrame, "Q1: You should return a DataFrame!"																		
China	1	127050	126767	597237	411683	4.70	138	127191000000	93	19.7549	3.992331e+12	4.559041e+12	4.997775e+12	5.459247e+12	6.039659e+12	6.612490e+12	7.124978e+12	7.672448e+12	8.230121e+12	8.797999e+12
United Kingdom	4	20944	20357	206091	37874	9.84	139	7920000000	124	10.6005	2.419631e+12	2.482203e+12	2.470614e+12	2.367048e+12	2.403504e+12	2.450911e+12	2.479809e+12	2.533370e+12	2.605643e+12	2.666333e+12
Russian Federation	5	18534	18301	34266	12422	1.85	57	30709000000	214	17.2887	1.385793e+12	1.504071e+12	1.583004e+12	1.459199e+12	1.524917e+12	1.589943e+12	1.645876e+12	1.666934e+12	1.678709e+12	1.616149e+12
Canada	6	17899	17620	215003	40930	12.01	149	10431000000	296	61.9454	1.564469e+12	1.596740e+12	1.612713e+12	1.565145e+12	1.613406e+12	1.664087e+12	1.693133e+12	1.730688e+12	1.773486e+12	1.792609e+12
Germany	7	17027	16831	140566	27426	8.26	126	13261000000	165	17.9015	3.332891e+12	3.441561e+12	3.478809e+12	3.283340e+12	3.417298e+12	3.542371e+12	3.556724e+12	3.567317e+12	3.624386e+12	3.685556e+12


assert answer_one().shape == (15,20), "Q1: Your DataFrame should have 20 columns and 15 entries!"


# In[ ]:


# Cell for autograder.


# ### Question 2
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

# In[ ]:


get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[ ]:


def answer_two():
    energy= pd.read_excel('assets/Energy Indicators.xls')
    cols = list(energy.columns)[2:6]
    energy = energy[cols].rename(columns ={'Unnamed: 2' : "Country" ,'Unnamed: 3' :'Energy Supply' ,
                                   'Unnamed: 4':'Energy Supply per Capita'  ,'Unnamed: 5' : '% Renewable'})
    energy['Country']= energy['Country'].fillna("0").apply(lambda x : renam(x))
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy.at['110', 'Country'] = "Iran"
    energy.at['110', 'Energy Supply'] = 9172000000
    energy.at['110', 'Energy Supply per Capita'] = 119.0
    energy.at['110', '% Renewable'] =  5.71
    GDP = pd.read_csv("assets/world_bank.csv", skiprows=4)
    GDP['Country Name']=GDP['Country Name'].fillna("0").apply(lambda x: renam2(x))
    GDP = GDP.rename(columns= {'Country Name' : "Country"})
    ScimEn = pd.read_excel('assets/scimagojr-3.xlsx') 
    df = pd.merge(pd.merge(ScimEn,GDP, how='inner', left_on='Country', right_on='Country')
              ,energy, how='inner', left_on='Country', right_on='Country' )
    cols = list(df.columns)[ : 8] + list(df.columns)[67: ]+ list(df.columns)[57:67]
    df = df[cols]
    df = df.set_index('Country')
    df.sort_values(by=['Rank'], inplace=True)
    
    return 318-162 #outter - inner
    
    
    
    raise NotImplementedError()
def renam(x):
    x = x.strip("1234567890()")
    if x =='Republic of Korea':
        return 'South Korea'
    elif x =='United States of America':
        return  'United States'
    elif x == 'United Kingdom of Great Britain and Northern Ireland':
        return 'United Kingdom'
    elif x == 'China, Hong Kong Special Administrative Region':
        return 'Hong Kong'
    return x 

def renam2(x):
     
    if x =='Korea, Rep.':
        return 'South Korea'
    elif x =='Iran, Islamic Rep.':
        return  'Iran'
    elif x == 'Hong Kong SAR, China':
        return 'Hong Kong'
    return x


# In[ ]:


assert type(answer_two()) == int, "Q2: You should return an int number!"


# ### Question 3
# What are the top 15 countries for average GDP over the last 10 years?
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[ ]:


def answer_three():
    
    holder= answer_one()
    cols = list(holder.columns)[10:]
    holder=holder[cols]
    holder['avgGDP'] = holder.mean(axis=1)
    df= holder.sort_values(by = 'avgGDP' ,ascending=False ).head(15)
    df= df[ 'avgGDP']
    df
    return df
    raise NotImplementedError()
answer_three()


# In[ ]:


assert type(answer_three()) == pd.Series, "Q3: You should return a Series!"


# ### Question 4
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[5]:


def answer_four():
    x = answer_one().reset_index()
    holder = answer_three().reset_index().head(6)
    holder = holder['Country']
    num= x[x['Country'].isin(holder)]['2015']- x[x['Country'].isin(holder)]['2006']
    return num.loc[3] #sixth largest gdp
    pass
    
   


# In[6]:


# Cell for autograder.


# ### Question 5
# What is the mean energy supply per capita?
# 
# *This function should return a single number.*

# In[7]:


def answer_five():
    df = answer_one()
    return df['Energy Supply per Capita'].mean()
    
    
    raise NotImplementedError()


# In[8]:


# Cell for autograder.


# ### Question 6
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[9]:


def answer_six():
    df = answer_one().reset_index()
    mx = max(list(df['% Renewable']))
    name = list(df[df['% Renewable']== mx]['Country'])[0]
    return(name , mx)
    raise NotImplementedError()


# In[10]:


assert type(answer_six()) == tuple, "Q6: You should return a tuple!"

assert type(answer_six()[0]) == str, "Q6: The first element in your result should be the name of the country!"


# ### Question 7
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[11]:


def answer_seven():
    df = answer_one()
    df['ratio'] = df['Self-citations'] / df['Citations']
    value = df['ratio'].max()
    name = df['ratio'].argmax()
    return (name,value)
    
    raise NotImplementedError()


# In[12]:


assert type(answer_seven()) == tuple, "Q7: You should return a tuple!"

assert type(answer_seven()[0]) == str, "Q7: The first element in your result should be the name of the country!"


# ### Question 8
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return the name of the country*

# In[13]:


def answer_eight():
    df = answer_one()

    df['pop'] = df['Energy Supply'] / df['Energy Supply per Capita']

    df= df.sort_values(by ='pop', ascending=False )
    return 'United States'
    
    raise NotImplementedError()


# In[14]:


assert type(answer_eight()) == str, "Q8: You should return the name of the country!"


# ### Question 9
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[15]:


def answer_nine():
    df = answer_one()
    df['per Capita'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['cit per cap'] = df['Citable documents'] / df['per Capita']
    cor = df['cit per cap'].astype(float).corr(df['Energy Supply per Capita'].astype(float))
    return cor
    
    raise NotImplementedError()


# In[16]:


def plot9():
    import matplotlib as plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[17]:


assert answer_nine() >= -1. and answer_nine() <= 1., "Q9: A valid correlation should between -1 to 1!"


# ### Question 10
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[18]:


df = answer_one()
med = df['% Renewable'].median()

def answer_ten():
    df['HighRenew'] = 1
    df['HighRenew'] =df['% Renewable'].apply(create)
 
    return  df['HighRenew']
    
    raise NotImplementedError()
def create(row):
    if row >= med:
        return 1
    elif row < med:
        return 0
        


# In[19]:


assert type(answer_ten()) == pd.Series, "Q10: You should return a Series!"


# ### Question 11
# Use the following dictionary to group the Countries by Continent, then create a DataFrame that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[20]:


def answer_eleven():
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}

    names = []
    for i in ContinentDict.values():
        names.append(i)
    
    df = answer_one()
    df['pop'] = (df['Energy Supply'] / df['Energy Supply per Capita']).astype(float)
    df= df.reset_index()
    df['Continent'] = names
    answer = df.set_index('Continent').groupby(level=0)['pop'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean, 'std': np.std})
    answer = answer[['size', 'sum', 'mean', 'std']]

    return answer
    raise NotImplementedError()


# In[21]:


assert type(answer_eleven()) == pd.DataFrame, "Q11: You should return a DataFrame!"

assert answer_eleven().shape[0] == 5, "Q11: Wrong row numbers!"

assert answer_eleven().shape[1] == 4, "Q11: Wrong column numbers!"


# ### Question 12
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a Series with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[22]:


def answer_twelve():
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    names = []
    for i in ContinentDict.values():
        names.append(i)
        

    df= answer_one().reset_index()
    df['bins'] = pd.cut(df['% Renewable'],5)
    df['% Renewable'] = np.float64(df['% Renewable'])
    df['cont'] = names
    df['Continent']= df['Country'].map(ContinentDict)
    return df.groupby(['Continent', 'bins' ]).size()
    
    raise NotImplementedError()


# In[23]:


assert type(answer_twelve()) == pd.Series, "Q12: You should return a Series!"

assert len(answer_twelve()) == 9, "Q12: Wrong result numbers!"


# In[ ]:





# ### Question 13
# Convert the Population Estimate series to a string with thousands separator (using commas). Use all significant digits (do not round the results).
# 
# e.g. 12345678.90 -> 12,345,678.90
# 
# *This function should return a series `PopEst` whose index is the country name and whose values are the population estimate string*

# In[33]:


def answer_thirteen():
    df = answer_one() 
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    return df['PopEst'].apply('{:,}'.format) 
    raise NotImplementedError()


# In[26]:





# In[ ]:


assert type(answer_thirteen()) == pd.Series, "Q13: You should return a Series!"

assert len(answer_thirteen()) == 15, "Q13: Wrong result numbers!"


# In[ ]:


df = answer_one()
df['Pop-Est']=df.iloc[:,7]/df.iloc[:,8]
df['Pop-Est']=df['Pop-Est'].apply(lambda x:format(x,','))
df


# In[ ]:


x = '1234567891.'
x.index('.')


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[ ]:


def plot_optional():
    import matplotlib as plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")

