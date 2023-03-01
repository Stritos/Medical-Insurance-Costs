#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# # Analyze the data set as you wish

# In[21]:


#storing the data set into a list
import csv
data = []
with open ('insurance.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        data.append(row)

#print(data)


# # Analyze the data set and identify the average insurance cost of smokers and non smokers.

# In[22]:


def insurance(data):
    count = 0
    ns_cost = 0
    s_cost = 0
    
# calculate the average insurance cost for smokers/non smokers
    for person in data:
        if person['smoker'] == 'yes':
            count += 1
            ns_cost += float(person['charges'])
        elif person['smoker'] == 'no':
            count += 1
            s_cost += float(person['charges'])
            
    ns_average = ns_cost / count
    s_average = s_cost / count
    
    print(f'The average insurance cost of a non smoker is ${int(ns_average)}.')
    print(f'The average insurance cost of a smoker is ${int(s_average)}.')
                                    
print(insurance(data))


# # Identify the average insurance cost of a smoker female vs non smoker female

# In[27]:


def female_insurance(data):
    count = 0
    s_cost = 0
    ns_cost = 0
    for person in data:
        if person['smoker'] == 'yes' and person['sex'] == 'female':
            count += 1
            s_cost += float(person['charges'])
            s_female = s_cost / count
        elif person['smoker'] == 'no' and person['sex'] == 'female':
            count += 1 
            ns_cost += float(person['charges'])
            ns_female = ns_cost / count
    
    print(f'The average insurance cost of a smoker female is ${int(s_female)}')
    print(f'The average insurance cost of a non smoker female is ${int(ns_female)}')
    
print(female_insurance(data))


# # Identify the average insurance cost of a smoker male vs non smoker male

# In[25]:


def male_insurance(data):
    count = 0
    s_cost = 0
    ns_cost = 0
    for person in data:
        if person['smoker'] == 'yes' and person['sex'] == 'male':
            count += 1
            s_cost += float(person['charges'])
            s_male = s_cost / count
        elif person['smoker'] == 'no' and person['sex'] == 'male':
            count += 1 
            ns_cost += float(person['charges'])
            ns_male = ns_cost / count
    
    print(f'The average insurance cost of a smoker male is ${int(s_male)}')
    print(f'The average insurance cost of a non smoker male is ${int(ns_male)}')
    
print(male_insurance(data))


# # Based on the analysis above we can say that on average, a smoker will have to pay more in insurance than a non smoker

# In[ ]:





# In[ ]:




