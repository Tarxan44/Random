from imports import *
from CategorySort import CategorySort
from dictionary import *

class levels():

    """
    Desired Output                                                                                    These last three are already completed in CategorySort.py
    Level1 -------------- Level2 ----------- Level3 ------------ Level4 ----------- Level5 ---------- Code Description ----------File ------------- Years Active
    Property              Vehicles           Car                 Acura              NaN(Or 'Not')     Acura Integra              OVB                1996 - 2003
    ...

    5050 ish lines, printed to excel sheet (from completedHierarchy.xlsx)
    """
      
    def cleaning_layer(df):
        #removes NaN rows, if ever optimized, perhaps use vectors and booleans?
        clean_df = df
        for x in range(df.shape[0]-1,-1,-1):
            if str(df['Category Placement'][x]) == 'nan':
                clean_df = clean_df.drop(clean_df.index[x])
        return clean_df

    def combination_layer(df):
        #combines any categories that have been marked to have similiar names to the desired name into a column BaseLevel
        function_df = pd.DataFrame(columns = ['Code Description', 'BaseLevel'])
        baseLevel_series = []
        for x in range(df.shape[0]):
            if str(df.iloc[x, 3]) == 'nan':
                baseLevel_series.append(df.iloc[x,2])
            else:
                baseLevel_series.append(df.iloc[x,3])
        function_df['BaseLevel'] = baseLevel_series
        return function_df

    def tagging_method(df, cat_info_dict):
        #creates df
        names = ['Level1', 'Level2', 'Level3', 'Level4', 'Level5','Code Descripton', 'Variable', 'Years Active']
        final_df = pd.Dataframe(columns = names)
        for x in range(5): #size(df)
            #call code desc
            #insert code desc in df

            #call combined as level5
            #insert code desciption for respective rows if NaN
            #insert baseLevel into temp_df

            #iterate thru baseLevel to determine level path
            #rental -> transport -> leisure -> Income/Expenses
            # atTop = False
            # category_path = []
            #counter = 0

            """ This is 1 of 2 methods being used to try and assign categories to levels, see TestHierarchies for other one """
            """ Trying to assign categories to levels as the for loops progress, like a cmd path """
            current_category = df['baseLevel'][x] #grab baseLevel column, row x
            
            for cat1 in cat_info_dict['level1']:
                for cat2 in cat1['level2']:
                    for cat3 in cat2['level3']:
                        for cat4 in cat3['level4']:
                            for cat5 in cat4['level5']:
                                if current_category == cat5:
                                    final_df['Level5'] = current_category
                                    final_df['Level4'] = cat4
                                    final_df['Level3'] = cat3
                                    final_df['Level2'] = cat2
                                    final_df['Level1'] = cat1
                                    break
                                else:
                                    final_df['Level5'] = 'None'
                        if current_category == cat4:
                            final_df['Level4'] = current_category
                            final_df['Level3'] = cat3
                            final_df['Level2'] = cat2
                            final_df['Level1'] = cat1
                            break
                        else:
                            final_df['Level4'] = 'None'
                    if current_category == cat3:
                        final_df['Level3'] = current_category
                        final_df['Level2'] = cat2
                        final_df['Level1'] = cat1
                        break
                    else:
                            final_df['Level3'] = 'None'
                if current_category == cat2:
                    final_df['Level2'] = current_category
                    final_df['Level1'] = cat1   
                    break             
                else:
                    final_df['Level2'] = 'None'
            if current_category == cat1:
                final_df['Level1'] = current_category
                break
                
        return()





        

        
        
    

        






"""

        def defining_levels(path, target_level):
        # Test xlsx for seeing the output of the level schemes without messing up FinalTable 
        #used for testing - to remove - write to an excel file 
        writer = pd.ExcelWriter('categorySort/notebooks/data/test.xlsx')

        #Write to a file to check outputs
        #df.to_excel(writer)

        #  future Column names on final output table/intitialization stuffs
        names = ['Variable','Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5']
        levelTable = pd.DataFrame(columns = names)

        #Sets up datatypes and column names to pull from sheet
        dtypes2 = {
            "Code description" : "category",
            "Variable " : "category" # Note: typo by bls, space ( ) after Variable
        }
        
        #path to BLS Sheet
        path = 'categorySort/notebooks/data/ce_pumd_interview_diary_dictionary.xlsx'

        megaSheet = pd.read_excel(path,sheet_name=2,dtype = dtypes2, usecols = list(dtypes2))

        #creates a DataFrameGroupBys with each category
        mentioned_byVariable = megaSheet.groupby(['Variable '])
        groups = [name for name,unused_df in mentioned_byVariable]
        

        #Gets the various catagories within level1 (Variable)
        #levelTable['Variable'] = megaSheet['Variable '] # All 'Variable ' values (not just unique ones)
        levelTable['Variable'] = megaSheet['Variable '].unique() #finished up to here - name print in df but nothing else 
        print(levelTable)


        # Problem: How does one group these items in nested groups? It should be like a tree with its branches, the higher you go the less thick the branch is but the more leaves that grow 
        for i in mentioned_byVariable:
            mentioned_byVariable.groupby(i)
"""