from imports import *
class CategorySort():   
  """Completed Output of this file can be found in notebooks/data/finalTable.xlsx"""

def category_frequency(path, target_variable):
      """ Using the orginal BLS excel file, find categories, number of times used, years active and inactive 
                                             ***CHECK PATH***                                            """
      #used for testing - to remove - write to an excel file
      writer = pd.ExcelWriter('notebooks/data/finalTable.xlsx')


      #  future Column names on final output table/intitialization stuffs
      names = ['Category', 'Times Mentioned', 'Years Active']
      finalTable = pd.DataFrame(columns = names)

      #Sets up datatypes and column names to pull from sheet
      dtypes = {
         "File" : "category",
         "Code description" : "category",
         "First year" : "category",
         "Last year" : "category",
      }

      #path to BLS Sheet - need try/catch
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

      #finds number of times each category is used 

      import collections as clt #  This is just here because it was being wack and wouldn't define itself in imports. Kudos if you get it to work

      # Use Collections to isolate the numerical value of frequency. (Basically just want the number part of how many times each category shows up)
      frequency_count = clt.Counter(megaSheet['Code description'])
      # Isolate the numbers only with .values()
      times_mentioned = frequency_count.values()
      finalTable['Times Mentioned'] = times_mentioned # Put .values() array into the 'Times Mentioned' Column
      #print(finalTable)
      

      """ --------------- END TIMES MENTIONED ----------------"""


      """--------------- Find Years Active V2 ----------------"""
      
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

            #unique
            tempSetVars = set(tempListVars)
            tempListVars = list(tempSetVars)

            tempSetYears = set(tempListYears)
            tempListYears = list(tempSetYears)

            tempYears.append(tempListYears) 
            tempVars.append(tempListVars)  
     
      #add to the final table
      finalTable["Years Active"] = tempYears
      finalTable["Variables"] = tempVars
      """-------------- END YEARS ACTIVE -------------------"""
      
      #Close the excel writer at the end
      #write results to FinalTable excel
      finalTable.to_excel(writer) #  Write to Excel file (finalTable.xlsx)
      writer.save()

      return finalTable
      



   