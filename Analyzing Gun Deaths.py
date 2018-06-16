
# coding: utf-8

# In[7]:


import csv
f = open('guns.csv')
data = list(csv.reader(f))
headers = data[0]
data = data[1:]

print(headers)
print(data[0:5])


# In[2]:


dates = [row[1] for row in data]

date_counts = dict()

for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
print(date_counts)


# In[5]:


import datetime
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]

print(dates[0:4])

date_counts = dict()

for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
print(date_counts)


# In[6]:


def count_column(data, int):
    
    counts = dict()
    
    for row in data :
        if row[int] in counts:
            counts[row[int]] += 1
        else:
            counts[row[int]] = 1
    
    return(counts)

sex_counts = count_column(data, 5)
race_counts = count_column(data, 7)

print(sex_counts)
print(race_counts)


# In[4]:


import csv
f = open('census.csv')
census = list(csv.reader(f))
print(census)


# In[13]:


mapping = {
    'Asian/Pacific Islander': ( int(census[1][14]) + int(census[1][15]) ),
    'Black': census[1][12],
    'Hispanic': census[1][11],
    'Native American/Native Alaskan': census[1][13],
    'White': census[1][10]
}

print(mapping)


# In[19]:


race_per_hundredk = dict()

for entry in race_counts:
    race_per_hundredk[entry] = int(race_counts[entry]) / int(mapping[entry])
    race_per_hundredk[entry] = race_per_hundredk[entry] * 100000

print(race_per_hundredk)


# In[12]:


intents = [row[3] for row in data]
races = [row[7] for row in data]

homicide_race_counts = {}

for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        if race in homicide_race_counts:
            homicide_race_counts[race] += 1
        else:
            homicide_race_counts[race] = 1


print(homicide_race_counts)


# In[14]:


for entry in homicide_race_counts:
    homicide_race_counts[entry] = int(homicide_race_counts[entry]) / int(mapping[entry])
    homicide_race_counts[entry] = homicide_race_counts[entry] * 100000

print(homicide_race_counts)

