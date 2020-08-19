from imports import *
class CategorySort():   
   """Completed Output of this file can be found in notebooks/data/finalTable.xlsx"""
   #need variables, years active, quarters, code desc, files, columns

   def category_frequency(path, target_variable):
      """ Using the orginal BLS excel file, find categories, number of times used, years active and inactive 
                                             ***CHECK PATH***                                            """
      #sed for testing - to remove - write to an excel file
      writer = pd.ExcelWriter('notebooks/data/finalTable.xlsx')


      #  future Column names on final output table/intitialization stuffs
      names = ['Code Description', 'Times Mentioned', 'Years Active','Variables', 'First quarter', 'Last quarter']
      finalTable = pd.DataFrame(columns = names)

      #Sets up datatypes and column names to pull from sheet
      dtypes = {
         "File" : "category",
         "Code description" : "category",
         "First year" : "category",
         "Last year" : "category",
         "First quarter" : "category",
         "Last quarter" : "category",
         "Variable " : "category",
         "Code value" : "category"
      }

      #path to BLS Sheet - need try/catch
      path = 'notebooks/data/ce_pumd_interview_diary_dictionary.xlsx'

      #Read sheet in and replace NaNs in Last year column with present year and converts to int for looks
      megaSheet = pd.read_excel(path,sheet_name=2,dtype = dtypes, usecols = list(dtypes))
      megaSheet["Last year"] = megaSheet["Last year"].cat.add_categories([2020]).fillna(2020)
      megaSheet["Last year"] = megaSheet["Last year"].astype(int)

      #Replace last quarter NaN with Q4
      megaSheet["Last quarter"] = megaSheet["Last quarter"].fillna(4).astype(int)
      #megaSheet["Last quarter"] = megaSheet["Last quarter"].cat.add_categories([4]).fillna(4)

      #creates a DataFrameGroupBys with each category
      mentioned_byCodeDesc = megaSheet.groupby([target_variable])
      groups = [name for name,unused_df in mentioned_byCodeDesc]
      #mentioned_byCodeDesc = megaSheet.groupby([target_variable])

      #Gets categories in an category
      finalTable['Category'] = groups 

      

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


      """--------------- Find Years Active, Variables, File Names V2 ----------------"""
      #initialize temp list
      tempYears = []
      tempVars = []
      tempFiles = []
      tempFirstQuarters = []
      tempLastQuarters = []

      for name in groups:
         #get the list of years and vars
         years = mentioned_byCodeDesc.get_group(name).to_numpy()

         #split them 
         files = years[:,0] 
         var = years[:,1]
         codes = years[:,2]
         firstUse = years[:,4]
         lastUse = years[:,6]
         first_quarter = years[:,5]
         last_quarter = years[:,7]
         

         #Multiple Values for a single Code Description   
         tempListYears = list(range(len(firstUse)))
         tempListVars = list(range(len(var)))
         tempListFiles = list(range(len(files)))
         tempListFirstQuarters = list(range(len(first_quarter)))
         tempListLastQuarters = list(range(len(last_quarter)))
         tempListCodes = list(range(len(codes)))

         for x in range(0,len(firstUse)):
            tempListYears[x] = str(firstUse[x]) + ' - ' + str(lastUse[x])
            tempListVars[x] = str(var[x])
            tempListFiles[x] = str(files[x])
            tempListFirstQuarters[x] = str(first_quarter[x])
            tempListLastQuarters[x] = str(last_quarter[x])
            tempListCodes[x] = str()


         #unique
         tempSetFiles = set(tempListFiles)
         tempListFiles = list(tempSetFiles)

         tempSetYears = set(tempListYears)
         tempListYears = list(tempSetYears)

         tempSetVars = set(tempListVars)
         tempListVars = list(tempSetVars)

         tempSetFirstQuarters = set(tempListFirstQuarters)
         tempListFirstQuarters =list(tempSetFirstQuarters)

         tempSetLastQuarters = set(tempListLastQuarters)
         tempListLastQuarters = list(tempSetLastQuarters)

         tempYears.append(tempListYears) 
         tempVars.append(tempListVars)
         tempFiles.append(tempListFiles)
         tempFirstQuarters.append(tempListFirstQuarters) 
         tempLastQuarters.append(tempListLastQuarters) 
      
      #add to the final table
      finalTable["Years Active"] = tempYears
      finalTable["Variables"] = tempVars
      finalTable['Files'] = tempFiles
      finalTable['First quarter'] = tempFirstQuarters
      finalTable['Last quarter'] = tempLastQuarters
      """-------------- END YEARS ACTIVE -------------------"""

      
      
      #Close the excel writer at the end
      #write results to FinalTable excel
      finalTable.to_excel(writer) #  Write to Excel file (finalTable.xlsx)
      writer.save()

      return finalTable
   



   