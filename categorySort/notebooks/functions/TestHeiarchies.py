from imports import *
from levels import *


""" Use this file for testing the assignment of categories to levels """

class TestHeiarchies():
   """ This is a solid option, however its terribly slow. Perhaps a better one would be to use json files and indexing""" 
   #def sortingByLevel(combined_df,years_and_active_df,test_dict):
   def sortingByLevel(combined_df, years_and_active_df):
      writer = pd.ExcelWriter('notebooks/data/test.xlsx')

      #bring in dictionary
      path2 = 'notebooks/data/dictionaryFull.xlsx'
      dictionary = pd.read_excel(path2)
      
      #create the dataframe where values will go into
      names = ['Level1', 'Level2', 'Level3', 'Level4','Code Description', 'Variables','Files', 'Years Active', 'First Quarter', 'Last Quarter']
      final_df = pd.DataFrame(columns = names)

      #add data already found
      final_df['Code Description'] = years_and_active_df["Category"]
      final_df['Variables'] = years_and_active_df["Variables"]
      final_df['Files'] = years_and_active_df['Files']
      final_df['Years Active'] = years_and_active_df['Years Active']
      final_df['First Quarter'] = years_and_active_df['First quarter']
      final_df['Last Quarter'] = years_and_active_df['Last quarter']

      #Now compare values in the completedHierarachy to the dictionary 
      category_list = combined_df['Category Placement']
      level4_placement = []
      level3_placement = []
      level2_placement = []
      level1_placement = []
      counter = 0
      for place in range(len(category_list)):
         for cat4 in range(len(dictionary)):
            place_name = category_list.iloc[place]
            if place_name == dictionary.iloc[cat4, 3]:
               level4_placement.append(place_name)
               level3_placement.append(dictionary.iloc[cat4, 2])
               level2_placement.append(dictionary.iloc[cat4, 1])
               level1_placement.append(dictionary.iloc[cat4, 0])
               break
            elif place_name == dictionary.iloc[cat4,2]:
               level4_placement.append(combined_df.iloc[place, 3])
               level3_placement.append(place_name)
               level2_placement.append(dictionary.iloc[cat4, 1])
               level1_placement.append(dictionary.iloc[cat4, 0])
               break
            elif place_name == dictionary.iloc[cat4, 1]:
               level4_placement.append('None')
               level3_placement.append(combined_df.iloc[place,3])
               level2_placement.append(place_name)
               level1_placement.append(dictionary.iloc[cat4, 0])
               break
            elif place_name == dictionary.iloc[cat4, 0]:
               level4_placement.append('None')
               level3_placement.append('None')
               level2_placement.append(combined_df.iloc[place,3])
               level1_placement.append(place_name)
               break
         if cat4 == len(dictionary)-1:
            level4_placement.append('None')
            level3_placement.append('None')
            level2_placement.append('None')
            level1_placement.append('None')
         counter = counter + 1
      
      final_df['Level4'] = level4_placement
      final_df['Level3'] = level3_placement
      final_df['Level2'] = level2_placement
      final_df['Level1'] = level1_placement


      
      final_df.to_excel(writer)
      writer.save()
      return final_df