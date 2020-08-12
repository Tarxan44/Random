from imports import *
class test():
   test_dict = [
      { 
         'category_name': 'categories',
         'level_data': [ 
               { 
                  'level': 1,
                  'level_name':'Property',
                  'sub_categories': ['Vehicles','Housing Expenses','Physical Assets', 'Real Estate'],
               },
               { 
                  'level': 2,
                  'level_name': 'Vehicles',
                  'sub_categories': ['Car','Car Upkeep', 'Other Vehicles'],
               },
               { 
                  'level': 3,
                  'level_name': 'Car',
                  'sub_categories': ['Acura', 'Alfa Romeo'],
               }
         ] 
      }
   ]
   df = pd.DataFrame()
   for cur_dict in test_dict:
      for level_data in cur_dict['level_data']:
         cur_level = level_data['level']
         level_name = level_data['level_name']
         for sub_cat in level_data['sub_categories']:
               print("level_name: {0}".format(level_name))
               level4 = sub_cat
               print("level4: {0}".format(level4))