from imports import *
class CategorySort():   
  

   def category_frequency(path, target_variable):
      """ Using the orginal BLS excel file, find categories, number of times used, years active and inactive 
                                             ***CHECK PATH***                                            """
      #used for testing - to remove - write to an excel file 
      writer = pd.ExcelWriter('categorySort/notebooks/data/test.xlsx')

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
      path = 'categorySort/notebooks/data/ce_pumd_interview_diary_dictionary.xlsx'

      #Read sheet in and replace NaNs in Last year column with present year and converts to int for looks
      megaSheet = pd.read_excel(path,sheet_name=2,dtype = dtypes, usecols = list(dtypes))
      megaSheet["Last year"] = megaSheet["Last year"].cat.add_categories([2020]).fillna(2020)
      megaSheet["Last year"] = megaSheet["Last year"].astype(int)

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
      finalTable.to_excel(writer) #  Write to Excel file (test.xlsx)

      """ --------------- END TIMES MENTIONED ----------------"""


      """--------------- Find Years Active V2 ----------------"""
      #yes I understand that iteration is prob not the fastest way but Im not smart enough to figure it out with the time i have
      
      #initialize temp list
      tempYears = []
      tempVars = []
      for name in groups:
         #get the list of years and vars
         years = mentioned_byCodeDesc.get_group(name).to_numpy()

         #split them 
         var = years[:,0] 
         firstUse = years[:,2]
         lastUse = years[:,3]
         #check if they are all the same value
         varUnique = np.unique(var)
         firstCheck = np.unique(firstUse)
         lastCheck = np.unique(lastUse)

         #Unique Value for a single Code Description
         if len(firstCheck) == 1 & len(lastCheck) == 1:
            tempYears.append(str(firstCheck[0]) + ' - ' + str(lastCheck[0]))
            tempVars.append(varUnique[0])
         #Multiple Values for a single Code Description   
         else:
            tempListYears = list(range(len(firstUse)))
            tempListVars = list(range(len(var)))
            for x in range(0,len(firstUse)):
               tempListYears[x] = str(firstUse[x]) + ' - ' + str(lastUse[x])
               tempListVars[x] = str(var[x])
            tempYears.append(tempListYears) 
            tempVars.append(tempListVars)  
     
      #add to the final table
      finalTable["Years Active"] = tempYears
      finalTable["Variables"] = tempVars
      """--------------END YEARS ACTIVE -------------------"""
      
      #Close the excel writer at the end
      #writer.save()
      return finalTable
      
      
 #runs the function
 table = category_frequency('ye','Code description')
 print(table)