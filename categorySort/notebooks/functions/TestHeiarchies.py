from imports import *
from levels import *

""" Use this file for testing the assignment of categories to levels """

class TestHeiarchies():
   '''
   def dictionary():
      test_dict = [
         { 
            """ Will need to manualy make top 4 categories lvl 1 """
            'category_name': 'categories',
            'level_data': [ 
                  { 
                     'level': 2,
                     'level_name':'Property',
                     'sub_categories': ['Vehicles','Housing Expenses','Physical Assets', 'Real Estate'],
                  },
                  { 
                     'level': 3,
                     'level_name': 'Vehicles',
                     'sub_categories': ['Car','Car Upkeep', 'Other Vehicles'],
                  },
                  { 
                     'level': 4,
                     'level_name': 'Car',
                     'sub_categories': ['Acura', 'Alfa Romeo'],
                  }
            ] 
         }
      ]
      return test_dict
   '''
   def sortingByLevel(cleaned_and_combined_df, years_and_codes_df, test_dict):
      #path = 'data\completedHierarachy.xlsx'
      #excel_sheet = pd.read_excel(path)

      '''I think I got it to run thru the entire dataframe but doesnt assign the variables correctly, ie all rows and levels are Hygiene, Question, Hygiene
         Should be a relatively easy fix '''


      names = ['Level1', 'Level2', 'Level3', 'Level4', 'Level5','Code Descripton', 'Years Active', 'Variables']
      final_df = pd.DataFrame(columns = names)

      #assign years active and variables into final_df
      final_df['Years Active'] = years_and_codes_df['Years Active']
      final_df['Variables'] = years_and_codes_df['Variables']

      # Using columns that are Acura to test
      toSort = cleaned_and_combined_df['BaseLevel']
      #toSort = toSort[245:252]
      #index = toSort.index
      

      for cat_toBe_sorted in toSort: #For all or selected rows (in this instance rows 245 - 251 of completedHierarchies.xlsx)
         for cur_dict in test_dict: # for 'current selected dictionary' in larger 'test_dictionary'
            for level_data in cur_dict['level_data']: #for level_data in the 'Currently selected dictionary'
               cur_level = level_data['level']  #define current level as numeric value (2-5)
               level_name = level_data['level_name'] #level name is the broader category, this allows us to reverse thru the path(levels)
               for sub_cat in level_data['sub_categories']: #looking thru all the sub categories in the current dictionary 
                  #Next line seems to be a critical issue for the success of these loops
                  for cat_toBe_sorted in level_data['sub_categories']: #if our selected category matches a sub category...
                     print('level' + str(cur_level) + ': ' + cat_toBe_sorted) #test line
                     #following if statements identify and assign cat_toBe_sorted to their appropriate columns
                     if cur_level == 4:
                        final_df['Level4'] = cat_toBe_sorted
                     if cur_level == 3:
                        final_df['Level3'] = cat_toBe_sorted
                     if cur_level == 2:
                        final_df['Level2'] = cat_toBe_sorted
                     else:
                        final_df['Level1'] = cat_toBe_sorted
                     #reset, assign cat_toBe_sorted new value of level_name which is simply the broader level (next level up)
                     cat_toBe_sorted = level_name
                     
         return final_df              
                        