import pandas as pd     #this imports pandas as pd
import seaborn as sns    #seaborn is imported as sns as opposed to sb because the dude who develpoed it was/is Samuel Nicholas Seaborn
from matplotlib import pyplot as plt #imports something to do with plots

#functions
_________________________________________________________________________________________________________________________________
# variable = object.function_name(argument, argument) ... this type of function returns a value
df = pd.read_csv('ur_mom.csv') ... #file names have to be in quotation marks

# function_name(argument or no argument) ... this function does not return a value, it only outputs things into the console
print(7) ... # 7 is an integer 
print(7.25) ... # 7.25 is a float
print("Linda Belcher") ... # "Linda Belcher" is a string
print('Gene Belcher') ... # 'Gene Belcher' is also a string

# variable = object.function_name() ... function returns value, but does not use any argument
burgers = df.head() ... #.head() returns a value but doesn't take any arguments
___________________________________________________________________________________________________________________________________________________
# some important/commonly used functions

___________________________________________________________________________________________________________________________________________________

#column selection

# dot notation
# variable = object.column ... only used for stuff with normal characters and underscores

# bracket and string notation
# variable = object['string wit special characters!'] 

__________________________________________________________________________________________________________________________________________________

logical statements
-------------------

variable == variable ... # checks if the variables are equal to one another, returns True or False

# can also use >, >=, <, <= (greater than, greater than or = to, less than, less than or = to)

!= ... # represents not equal to 

using logic w/ DataFrames
--------------------------

DataFrame_Name[logical statement]
Ex. credit_records[credit_records.price > 20.00] ... # will check for purchases greather than 20$

_________________________________________________________________________________________________________________

Line plot with mathplotlib
--------------------------

function_name(x_values, y_values)

plt.plot ... # makes the plot
plt.show ... # shows the plot
