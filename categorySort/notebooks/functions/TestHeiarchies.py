from imports import *
class test():
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
   path = 'categorySort/notebooks/data/completedHeiarachy.xlsx'
   excel_sheet = pd.read_excel(path, dropna = True, na_values=["NaN","nan","Question"])

   names = ['Level1', 'Level2', 'Level3', 'Level4', 'Level5','Code Descripton', 'Variable', 'Years Active']
   final_df = pd.DataFrame(columns = names)
   # Using columns that are Acura to figure out process
   toSort = excel_sheet[245:252]
   index = toSort.index
   #cat_toBe_sorted = excel_sheet['Category Placement']#.values[0]
   #print(cat_toBe_sorted)
   #for x in excel_sheet['Category Placement']:
   print(toSort)
   
   x = 1
   for x in index: #For all or selected rows
      for cur_dict in test_dict: # for 'current selected dictionary' in larger 'test_dictionary'
         for level_data in cur_dict['level_data']: #for leve_data in the 'Currently selected dictionary'
            cat_toBe_sorted = toSort['Category Placement'] #Category to be sorted = 'Category Placement' column of completedHeirarchies.xlsx
            cur_level = level_data['level']  #define current level as numeric value (2-5)
            level_name = level_data['level_name'] #level name is the broader category, this allows us to reverse thru the path (levels)
            for sub_cat in level_data['sub_categories']: #looking thru all the sub categories in the current dictionary 

               ''' TODO: Trying to compare cat_toBe_sorted and the sub categories , see below ''' 

               if cat_toBe_sorted == level_data['sub_categories']: #if our selected category matches a sub category...
                  print('level' + cur_level + ': ' + cat_toBe_sorted) #test line
                  #following if statements identify and assign cat_toBe_sorted to their appropriate columns
                  if cur_level == 4:
                     final_df['Level4'] = cat_toBe_sorted
                  if cur_level == 3:
                     final_df['Level3'] = cat_toBe_sorted
                  if cur_level == 2:
                     final_df['Level2'] = cat_toBe_sorted
                  else:
                     final_df['Level1'] = cat_toBe_sorted
                  #reset, make cat_toBe_sorted into the broader level (next level up)
                  cat_toBe_sorted = level_name
                  #restart the loop
                  x + 1
                  
                     
                  #final_df['']
                  #print("level" + str(cur_level) + ": {0}".format(cat_toBe_sorted))
                     
               
               
               
                  #print("level_name: {0}".format(level_name))
                  #level4 = sub_cat
                  #look for category
                  #assuming the final levels dont have sub categories 
                  #print("level4: {0}".format(level4))
                  #print("level" + str(cur_level) + ": {0}".format(level4))