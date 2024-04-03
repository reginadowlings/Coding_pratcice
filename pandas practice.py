import pandas as pd

'''SERIES IN PANDAS'''

ages = [23, 25, 27, 43, 47] # series prints the column of a table with idexs from 0

# aged =pd.Series(ages)
# print(aged)


indexed_age = pd.Series(ages, index=['me', 'nef', 'steph', 'mum', 'aunt'])   #this line of code is indexed giving names of ages listed
# print(indexed_age)


calories = {"day1": 420, "day2": 380, "day3": 390}  #this set of dictionary uses the key as the index label in a Series Data 
myvar = pd.Series(calories)
# print(myvar)



'''PANDAS DATAFRAME'''

members = {
    'rapline' : ['suga', 'hope','rm'],
    'age': [28, 27, 26 ]
}

framed_members = pd.DataFrame(members)
# print(framed_members.loc[[1,2]])
'''this line of code extracts the row of a particular index and prints it as a string. However, when two rows are referenced
 (with 2  brackets), the output comes as a dataframe'''


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

# print(myvar)




'''THIS CODES ARE A PRACTICE OF CSV DATA WITH THE PANDAS MODULE '''
file = pd.read_excel('city.xlsx')
# new_file = file.dropna() #this line of code drops rows with a vlaue missing

# file['SCORES'].fillna(0, inplace= True)
file['SCORES'].mean()
# print(file)
















