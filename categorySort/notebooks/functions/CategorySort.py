from imports import *
class CategorySort():   
   #runs the function
   category_frequency('ye','Code description')

   def category_frequency(path, target_variable):
      """ Using the orginal BLS excel file, find categories, number of times used, years active and inactive """
      #used for testing - to remove - write to an excel file
      writer = pd.ExcelWriter('notebooks/data/test.xlsx')

      #Write to a file to check outputs
      #df.to_excel(writer)

      #  future Column names on final output table/intitialization stuffs
      names = ['Category', 'Times Mentioned', 'Years Absent', 'Years Present']
      finalTable = pd.DataFrame(columns = names)

      #Sets up datatypes and column names to pull from sheet
      dtypes = {
         "File" : "category",
         "Code description" : "category",
         "First year" : "category",
         "Last year" : "category"
      }

      #path to BLS Sheet
      path = 'notebooks/data/ce_pumd_interview_diary_dictionary.xlsx'

      #Read sheet in and replace NaNs in Last year column with present year
      megaSheet = pd.read_excel(path,sheet_name=2,dtype = dtypes, usecols = list(dtypes))
      megaSheet["Last year"] = megaSheet["Last year"].fillna(2019)

      #creates a DataFrameGroupBys with each category
      mentioned_byCodeDesc = megaSheet.groupby([target_variable])

      #Gets categories in an array
      keys = megaSheet['Code description'].unique()  
      
      #finds number of times each category is used - still need to move those numbers in the final table under 'Times Mentioned'
      '''
      times_mentioned = megaSheet.groupby([target_variable])
      nameAndActiveDF = pd.DataFrame(codeDesc)
      #active = []
      for f in times_mentioned
         test = times_mentioned.get_group({}).take([5,7], axis = 1)
         active =  str(test.iloc[1,0]) + '-' + str(int(test.iloc[2,1])) 
         nameAndActiveDF['Years Active: '] = active
      #print(nameAndActiveDF)
      
      #Close the excel writer at the end
      #writer.save()
      '''
      
