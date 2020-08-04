from imports import *
class CategorySort():   
  

   def category_frequency(path, target_variable):
      """ Using the orginal BLS excel file, find categories, number of times used, years active and inactive 
                                             ***CHECK PATH***                                            """
      #used for testing - to remove - write to an excel file 
      writer = pd.ExcelWriter('categorySort/notebooks/data/finalTable.xlsx')

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
         "Last year" : "category",
      }
     
      #path to BLS Sheet
      path = 'categorySort/notebooks/data/ce_pumd_interview_diary_dictionary.xlsx'

      #Read sheet in and replace NaNs in Last year column with present year
      megaSheet = pd.read_excel(path,sheet_name=2,dtype = dtypes, usecols = list(dtypes))
      #megaSheet["Last year"] = megaSheet["Last year"].fillna(2019) #doesnt run bc of data type

      #creates a DataFrameGroupBys with each category
      mentioned_byCodeDesc = megaSheet.groupby([target_variable])
      groups = [name for name,unused_df in mentioned_byCodeDesc]
      mentioned_byCodeDesc = megaSheet.groupby([target_variable])

      #Gets categories in an category
      finalTable['Category'] = groups #finished up to here - name print in df but nothing else 

     

      """ ---------------- Times Mentioned -------------- """

      #finds number of times each category is used - still need to move those numbers in the final table under 'Times Mentioned'

      import collections as clt #  This is just here because it was being wack and wouldn't define itself in imports. Kudos if you get it to work

      # Use Collections to isolate the numerical value of frequency. (Basically just want the number part of how many times each category shows up)
      frequency_count = clt.Counter(megaSheet['Code description'])
      # Isolate the numbers only with .values()
      times_mentioned = frequency_count.values()
      finalTable['Times Mentioned'] = times_mentioned # Put .values() array into the 'Times Mentioned' Column
      #print(finalTable)
      finalTable.to_excel(writer) #  Write to Excel file (finalTable.xlsx)

      """ --------------- END TIMES MENTIONED ----------------"""
      
      """
      #Attempt 1
      times_mentioned = megaSheet.groupby([target_variable])
      #nameAndActiveDF = pd.DataFrame(groups)
      #active = []
      for f in times_mentioned:
         test = times_mentioned.get_group().take([5,7], axis = 1)
         active =  str(test.iloc[1,0]) + '-' + str(int(test.iloc[2,1])) 
         nameAndActiveDF['Years Active: '] = active
         #print(nameAndActiveDF)
      """
      '''

      #Attempt 2
      path = 'data\ce_pumd_interview_diary_dictionary.xlsx'
      megaSheet = pd.read_excel(path,sheet_name=2,dtype = dtypes, usecols = list(dtypes))
      #megaSheet["Last year"] = megaSheet["Last year"].fillna(2019)
      mentioned_byCodeDesc = megaSheet.groupby([target_variable])
      groups = [name for name,unused_df in mentioned_byCodeDesc]
      #keys = megaSheet['Code description'].unique()
      finalTable['Category'] = groups #finished up to here - name print in df but nothing else
            
      #focus on getting times mentioned for each category
      times_mentioned = megaSheet.groupby([target_variable])
      active = pd.DataFrame(column = 'Years active')
      counter = 0
      for mentioned in mentioned, rando_df in times_mentioned:
         counter = counter +1
         active
      '''
      #Close the excel writer at the end
      writer.save()
      
      
 #runs the function
   category_frequency('ye','Code description')