import pandas as pd
list1 = [1,2,3,4,5]
data = pd.Series(list1)
print(data)
data2 = pd.Series([2,3,4,5,6], index=['a','b','c','d','e'])
print(data2)
population_dict = {'California': 38332521,
 'Texas': 26448193,
 'New York': 19651127,
 'Florida': 19552860,
 'Illinois': 12882135}
population = pd.Series(population_dict)
print(population)
df = pd.DataFrame([{'a': 1, 'b': 2,'d':4}, {'a':5,'b': 3}])
print(df)
continentdf = pd.DataFrame([{'Asia':'India','Africa':'Botswana'},{'Africa':'Sudan'},{'Asia':'China'}])
print(continentdf)