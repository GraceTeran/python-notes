import pandas as pd     #this imports pandas as pd
import seaborn as sns    #seaborn is imported as sns as opposed to sb because the dude who develpoed it was/is Samuel Nicholas Seaborn

#functions
# variable = object.function_name(argument, argument) ... this type of function returns a value
df = pd.read_csv('ur_mom.csv') ... #file names have to be in quotation marks
# function_name(argument or no argument) ... this function does not return a value, it only outputs things into the console
print(7) ... # 7 is an integer 
print(7.25) ... # 7.25 is a float
print("Linda Belcher") ... # "Linda Belcher" is a string
print('Gene Belcher') ... # 'Gene Belcher' is also a string
# variable = object.function_name() ... function returns value, but does not use any argument
burgers = df.head() ... #.head() returns a value but doesn't take any arguments
