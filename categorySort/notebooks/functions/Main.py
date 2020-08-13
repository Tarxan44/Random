from imports import *
from CategorySort import *
from levels import *
from TestHeiarchies import *

"""
    Desired Output(Example from line 248 of completedHierarchy.xlsx)                                  These last three are already completed in CategorySort.py
    Level1 -------------- Level2 ----------- Level3 ------------ Level4 ----------- Level5 ---------- Code Description ----------File ------------- Years Active
    Property              Vehicles           Car                 Acura              NaN(Or 'Not')     Acura Integra              OVB                1996 - 2003
    ...

    5050 ish lines, printed to excel sheet 
"""

class Main():
     
     #runs the CategorySort functions
     #table = CategorySort.category_frequency('','Code description')

     #run the levels function
     orginal_df = pd.read_excel('data\completedHierarachy.xlsx')
     clean_df = levels.cleaning_layer(orginal_df)
     #print(clean_df)
     combined_df = levels.combination_layer(clean_df)
     #print(combined_df)

     #bring in dictionary
     dictionary = TestHeiarchies.dictionary()

     #run Test Hierarchies to test the sorting function by levels 
     levels_df = TestHeiarchies.sortingByLevel(combined_df, dictionary)
     
     

