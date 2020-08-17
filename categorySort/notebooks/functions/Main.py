from imports import *
from CategorySort import CategorySort
from levels import levels
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
     #cs_object = CategorySort()
     #bring in the completed categorized excel sheet
     orginal_df = pd.read_excel('categorySort/notebooks/data/completedHierarchy.xlsx')

     #get codes and years active - takes a long time - might just pull from the excel file
     #years_and_codes_df = CategorySort.category_frequency('not needed', 'Code description')
     years_and_codes_df = pd.read_excel('categorySort/notebooks/data/finalTable.xlsx')
     #print(years_and_codes_df)
     
     years_and_codes_df = pd.read_excel('categorySort/notebooks/data/finalTable.xlsx')
     print(years_and_codes_df)

     levels_object = levels()
     #remove extraneous rows
     clean_df = levels_object.cleaning_layer(orginal_df)
     
     #combine layers with similiar names (previously marked)
     combined_df = levels_object.combination_layer(clean_df)

     #bring in dictionary
     category_dictionary = dictionary.dictionary()

     #run Test Hierarchies to test the sorting function by levels 
     #levels_df = TestHeiarchies.sortingByLevel(combined_df, years_and_codes_df,category_dictionary)
     levels_df = TestHeiarchies.sortingByLevel(combined_df, clean_df)
     #levels_df = TestHeiarchies.sortingByLevel(combined_df, years_and_codes_df,category_dictionary)

     print(levels_df)
     
     
     

