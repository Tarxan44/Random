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
   df = pd.DataFrame()
   #for x in df.size()
   for cur_dict in test_dict: #will become for x in size()...
      for level_data in cur_dict['level_data']:
         cur_level = level_data['level']
         level_name = level_data['level_name']
         for sub_cat in level_data['sub_categories']:
               print("level_name: {0}".format(level_name))
               level4 = sub_cat
               #look for category
               #assuming the final levels dont have sub categories 
               #print("level4: {0}".format(level4))
               print("level" + str(cur_level) + ": {0}".format(level4))