from imports import *
from CategorySort import *
from levels import *
class runnyBoi():
     #just a class to run all of the functions
     
     #runs the CategorySort functions
     #table = CategorySort.category_frequency('','Code description')

     #run the levels function
     orginal_df = pd.read_excel('data\completedHeiarachy.xlsx')
     clean_df = levels.cleaning_layer(orginal_df)
     combined_df = levels.combination_layer(clean_df)
     print(combined_df)
     

