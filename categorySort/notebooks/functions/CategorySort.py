from imports import *

class CategorySort():
   
   #  defining the path, and using panda to read it
   #path = 'notebooks/data/categories.csv'
   #  future Column names on final output table
   names = ['Category', 'Times Mentioned', 'Years Absent', 'Years Present']
   #  for just importing one csv
   #df = pd.read_csv(path, skiprows=0)
   
   #read in csv 
   
   counter = 1
   
   


   def category_frequency(self, path, target_variable):
      """ Defining category level and 'Times Mentioned' in .csv using a concatinated sheet """
      
      #  Concatinating all categories sheets in path
      allSheets = pd.concat([pd.read_csv(f) for f in glob.glob('notebooks/data/categories*.csv')], ignore_index = True)

      #big count sheet
      bigCountSheet = []

      #read in csv - assumes that there are no other files
      path = 'notebook/data'
      categories = os.listdir(path)

      #  defining the level of specificity 
      target_variable = 'level2'

      bigCountSheet[:1,:] = allSheets.groupby(target_variable).count()


      count = 0
      for x in categories:
         fullpath = path + categories[x]
         df = pd.read_csv(fullpath)

         #count how many times 'target_variable' occurs
         times_mentioned = df.groupby(target_variable).count()


      
      
