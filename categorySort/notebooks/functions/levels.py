from imports import *
from CategorySort import CategorySort
from dictionary import *

class levels():

    """
    Desired Output                                                                                    These last three are already completed in CategorySort.py
    Level1 -------------- Level2 ----------- Level3 ------------ Level4 ----------- Level5 ---------- Code Description ----------File ------------- Years Active
    Property              Vehicles           Car                 Acura              NaN(Or 'Not')     Acura Integra              OVB                1996 - 2003
    ...
    """
      
    def cleaning_layer(self,df,column):
        #removes NaN rows, when optimized, perhaps use vectors and booleans?
        clean_df = df
        for x in range(df.shape[0]-1,-1,-1):
            if str(df[column][x]) == 'nan':
                clean_df = clean_df.drop(clean_df.index[x])
        return clean_df

    def combination_layer(self,df):
        #combines any categories that have been marked to have similiar names to the desired name into a column BaseLevel
        #just replaces any empty slots in the combined column with the code description
        function_df = pd.DataFrame(columns = ['Code Description','Category Placement' 'BaseLevel'])
        function_df['Code Description'] = df['Code description']
        function_df['Category Placement'] = df['Category Placement']

        baseLevel_series = []
        for x in range(df.shape[0]):
            if str(df.iloc[x, 3]) == 'nan':
                baseLevel_series.append(df.iloc[x,2])
            else:
                baseLevel_series.append(df.iloc[x,3])
        function_df['BaseLevel'] = baseLevel_series
        return function_df






    def tagging_method(df, cat_info_dict):
        #this was my initial attempt at this, still has some merit as to solving the problem, albeit not the fastest or most effective way
        names = ['Level1', 'Level2', 'Level3', 'Level4', 'Level5','Code Descripton', 'Years Active', 'Variables']
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
