from imports import *
from levels import *


""" Use this file for testing the assignment of categories to levels """

class TestHeiarchies():

   """ Would recommend using this sample dictionary below for testing the rows that include 'Acura' , as opposed to importing the whole dict"""
   """
   def dictionary(self):
      test_dict = [
         { 
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
   """
   """ This is a solid option, however its terribly slow. Perhaps a better one would be to use json files and indexing""" 
   #def sortingByLevel(combined_df,years_and_active_df,test_dict):
   def sortingByLevel(combined_df, years_and_active_df):
      writer = pd.ExcelWriter('categorySort/notebooks/data/test.xlsx')
      #writer = pd.ExcelWriter('notebooks/data/test.xlsx')

      #bring in excel sheet
      path = 'categorySort/notebooks/data/completedHierarchy.xlsx'
      completedHierarachy = pd.read_excel(path)

      #bring in dictionary
      path2 = 'categorySort/notebooks/data/dictionaryFull.xlsx'
      dictionary = pd.read_excel(path2)
      
      #create the dataframe where values will go into
      names = ['Level1', 'Level2', 'Level3', 'Level4', 'Level5','Code Descripton', 'Variables', 'Years Active']
      final_df = pd.DataFrame(columns = names)

      #Now compare values in the completedHierarachy to the dictionary 
      #level 4

      #for place in completedHierarachy['Category Placement']: # .astype(str): 
      # NOTE: hopefuly you can get this working jackson, the first two loops work. the last two theoretically should work too. I just didnt 
      # know bc it would assign to the excel sheet and we need to use the excel sheet for an easy assignment
      category_list = combined_df['BaseLevel']
      level4_placement = []
      level3_placement = []
      level2_placement = []
      level1_placement = []
      #level5_placement = []
      for place in category_list:
         for cat4 in range(len(dictionary)):
            #if place == (dictionary['Level4'].all()) and (dictionary[cat4].all()):
            if place == ((dictionary['Level4']) & (dictionary[cat4])):
               level4_placement.append(place)
               level3_placement.append(dictionary[cat4, "Level3"])
               print("level4: " + level4_placement)
               print("level3: " + level3_placement)
               #category_list.remove(place)
      final_df['Level4'] = level4_placement
      final_df['Level3'] = level3_placement
      final_df['Level2'] = level2_placement
      final_df['Level1'] = level1_placement

      writer.save()
      return final_df
      
      
      
      '''
      for cat3 in dictionary["Level3"]:
         if place == cat3:
            final_df['Level3'] = place
      return final_df
      '''
      '''
      for place in completedHierarachy['Category Placement']: # .astype(str):  
         for cat3 in dictionary['Level3']: #.astype(str):
            if place == cat3:
               final_df['Level3'] = place 
               #print("level3: " + place) NOTE: beware this thing goes on forever, use above one instead
               #final_df.to_excel(writer) #  Write to Excel file (test.xlsx)

      for place in final_df['Level3']:
         for cat2 in dictionary['Level2']:
            if place == cat2:
               final_df['Level2'] = place
               #final_df.to_excel(writer)
   
      for place in final_df['Level2']:
         for cat1 in dictionary['Level1']:
            if place == cat1:
               final_df['Level1'] = place
      '''        
      
    
#      
                #  else:
                 #    for cat2 in dictionary["Level2"]:
                  #      if place == cat2:
                   #        final_df['Level2'] = place  
      
   
            


            

   #write a seperate loop that hopefully can just use the final_df compared to the dictionary to complete the last couple levels. 

     
"""
      #add years and variables
      final_df['Variables'] = years_and_active_df['Variables']
      final_df['Years Active'] = years_and_active_df['Years Active']

      #Initalize to the toSort list
      toSort = combined_df['BaseLevel']

      counter = 0
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
         break;
         counter = counter + 1          
         """     
               