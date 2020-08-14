from imports import *
from CategorySort import *
from levels import *
from TestHeiarchies import *
from dictionary import *
from CategorySort import *

"""
    Desired Output(Example from line 248 of completedHierarchy.xlsx)                                  These last three are already completed in CategorySort.py
    Level1 -------------- Level2 ----------- Level3 ------------ Level4 ----------- Level5 ---------- Code Description ----------File ------------- Years Active
    Property              Vehicles           Car                 Acura              NaN(Or 'Not')     Acura Integra              OVB                1996 - 2003
    ...

    5050 ish lines, printed to excel sheet 
"""

class Main():
     #bring in the completed categorized excel sheet
     orginal_df = pd.read_excel('notebooks/data/completedHierarchy.xlsx')

     #get codes and years active - takes a long time - might just pull from the excel file
     #years_and_codes_df = CategorySort.category_frequency('not needed', 'Code description')
     
     years_and_codes_df = pd.read_excel('notebooks/data/finalTable.xlsx')
     print(years_and_codes_df)

     #remove extraneous rows
     clean_df = levels.cleaning_layer(orginal_df)
     
     #combine layers with similiar names (previously marked)
     combined_df = levels.combination_layer(clean_df)

     #bring in dictionary
     dict = dictionary.dictionary()

     #run Test Hierarchies to test the sorting function by levels 
     levels_df = TestHeiarchies.sortingByLevel(combined_df, years_and_codes_df,dict)
     
     
     
     #test

