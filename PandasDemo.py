import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#make this example reproducible
np.random.seed(0)

"""first try
students = pd.DataFrame({'phone': ['555-1212', '234-5423', '425-2563', '426-7435'], 'age': [17, 17, 26, 30], 'grade':[78, 68,49,93] #}
                       , 'index':['Melanie', 'Bob', 'viday', 'Ming'] })
"""
#original dataFrame: 
students = pd.DataFrame({'phone': ['555-1212', '555-1234', '555-1111', '555-2222'], 'age': [17, 17, 18, 18], 'grade':[100, 68,49,93]} #}
                       , index=['Melanie', 'Bob', 'Vidhya', 'Ming'] )

print("students = ", students)
#row names : named parameter is called index
# get data: so that it's human read-able

print("students.index = ", students.index)


# can also: # Look at data-frame : with numpy array
""" You can also create: dataframe : with numpy and some column name 
"""

def generateData(interval, indexVector=['Jenny', 'Frank' , 'Wenfei','Arun', 'Mary', 'Ivan'] , columnsVector=list('ABCD')):

    a = interval[0]; b = interval[1];
    
    df = pd.DataFrame( np.random.randn(a,b), index = indexVector ,
                  columns = columnsVector)
    return df
def generateDataFrame(interval,_3dTuple, _cols=['A','B']):

    
    a = interval[0]; b = interval[1];
    x = _3dTuple[0]; y = _3dTuple[1]; z = _3dTuple[2];
    
    #create DataFrame
    df = pd.DataFrame(np.random.rand(a,b), index=range(x,y,z), columns=[_cols[0], _cols[1]])
    return df

print( generateDataFrame((6,2), (0,18,3) ) ) 

#Auto-Generate data 
df = pd.DataFrame(np.random.randn(6,4), index = ['Jenny', 'Frank' , 'Wenfei','Arun', 'Mary', 'Ivan'],
                  columns = list('ABCD'))

print("df =",df)
"""There are also Series, which gets you all the functionality of a data frame,
when you have a 1-Dimensional set of data with an index 
"""
s = pd.Series([1,3,5, np.nan, 6,8])
print("s =",s)
"""
Serves as 1D data frame: with time series esp

Instanciated it as a series

missing data :
find the nulls 

# DataFrames :


- Missing data: is the reality of life

"""


print( s.isnull()) 

"""
there are isnull()

# Dataframes and series play nice with plotting


"""

ax = df.plot(kind='line', color='#c93867', figsize=(50, 10))
df.plot(kind='line', color='#c93867', figsize=(50,10))
s.plot()
df.plot()

# plt.show() #UncommentMe:


"""Show what data looks  like
"""
print( df.head() ) 

"""once got dataframe, it's easy to see portions of your data, that match what you want
(same goes for series ) """

#print()
#idx = s.index > list.index( 'c')
#print("index", idx)

#result
lst = []
#s = str(s)
#1. initialize value: 
value  =""

#way 1: didn't work
#result = next(k for k, value in enumerate(s)
#if value > 'c'); lst.append(value) ; print("Index is: ",result)

#way2: works!
#1. STICK my logical condition, inside these brackets: index s > 'c'
if value > 'c':
    result = next(k for k, value in enumerate(s))
    lst.append(value) ; print("Index is: ", result)
            

# s[(s.index) > ('c')] # give me s after c (don't care about a, b)


# Find s' that aren't `null`
#find s that aren't null
s[s.isnull() == False] # dropped  nan

print(students.head()) #recall how students look like 

print(students.age)#how old they are: 

students['age']
students.age # grab whatever (as attribute with dot operator )

# selection by label
students.loc['Melanie'] #use .loc (location) [Selecting by Label]


students.loc['Melanie', ['age', 'grade']] #get somethings about her (her attributes)


#students.index.get_loc['Melanie', ['age', 'grade']]

# select different (partitions)

print( students.iloc[1,2] )


print(students[students['age'] > 17])

# It's also easy to summarize  data



##basic stats - summarize data: [no for loops]

### Mean

print("Mean age = ", students.age.mean() )

print( "min_age = ", students.age.min() ) 

print( "max_age = ", students.age.max() ) 

### add Information , to an existing dataframe :
""" add the following new `grade` column """
students['grade'] = [100, 97, 80, 85]
print(students['grade'])

print( "find the student with max(grade): [ students['grade'] =?= Max( students['grade']) = \n", students[ students['grade'] == students['grade'].max()] , end="\n" )

### Aggregate Information:

students.groupby('age').grade.mean()


## aggregate by grouping (i.e. "maybe I wanted the means divided-up!" )
### by gender , age , phoneNumber 



print( students.groupby('age').grade.mean())
# notice: the '17' year old is studying more (than their 18 year old )

# create Categories to aggregate with, "on-the-fly" [ `linspace` bins method]
# 1. create bins (of linspace ) - 3D
bins = np.linspace(70,100, 3) # in range [70, 100]
print("bins = ",bins)

#2. another operation: groupby grade 
print( students.groupby(np.digitize(students.grade, bins)).age.mean() ) 
""" I don't care if you got 83, or 87 , just give me a range around [70, 100] """

# Finally, Apply functions  [Straight-forward]
"""the Why:  lambda functions : mostly used when you don't want to `declare` a function
How: by applying something, (where) you'll nver going to use it again"""

f = lambda x: x +1

print( f(4) )


students.age.apply(lambda age : age + 1 )

# Let's look at built-in methods (we can apply)

print("mean age(students) = ", students.age.mean() )


#New: But, the  real use of Lambda, when you stick it to an `apply` statement 

print("Lambda[Increase everyone's age, by '1'] = ", students.age.apply( lambda age : age +1 ) )

# Alse: lots of built-In Methods (you want to be aware of)
## come in handy
#1. mean
print( students.age.mean() )
#2. count
print( students.age.count() )

#3. correlations
print( students.age.corr() )
#4. cumulative max
print( students.age.cummax() ) #max cummulative

#if you're rolling your own there's something wrong


    






