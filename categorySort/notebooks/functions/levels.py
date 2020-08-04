from imports import *
from CategorySort import CategorySort

""" 
    Purpose of this file: defining simpler and more organized categories to the surveyed values using keywords to sort through the data
    Ranging in specificity, Level 1 --> level 5
    Level 1 is the most broad, level 5 is the most specific.

    For example, the thought process is just like categories.csv - broad --> specific
    Variable--------Level 1------------Level 2-----------Level 3---------------Level 4-------------Level 5
    MINAPPLY-------Property----------Appliances--------Minor Appliances-----Office and Electr.-----Calculator

    (except drawing from the dictionary to see how many a category is mentioned and what years they are present)

    High level attempt at the direction of this code:

    1. Use BLS Survey data to create most specific levels as a groupby (categories)
    2. Iterate thru the BLS category names and manually assign them a level Category
        2a. Assigning the level category will automatically drop it in a path of the broadest category
        (Category from BLS: Dryer, Assigned to Major Applicance(lvl3), automatically assigned to Housing Expense (lvl2), and Property(lvl1))
    3. Levels can be change with a categories["category name"].change_level()
    4. Levels can be quickly added and removed with a .add(), .remove()


    Level 1 Categories{
        "Property",
        "Expenses/Income",
        "Other",
        "Clothing, Fabric, Accessories",
    }

    Level 2 Categories{
        Property{Vehicles, Housing Expenses, Real Estate}
        Expenses/Income{Leisure, Stocks&Bonds,Savings, Transport, Education, Health, Income, Other Expenditures}
        Other{Catch all for things that dont fit anywhere else/Irrelevant/Errors}
        Clothing, Fabric, Acessories{Clothing, Accessories, Fabric}
    }

    Level 3 Categories{
        Physical Assets (exl vehicles){Real Estate, Records}
        Vehicles{Car Purchases, Records, Maintenance}
        Housing Expenses{Utilities, Construction}
        Income{Employment, Gov Intervention}
        Health{Insurance, Proactive Health, Reactive Health}
        Clothing{Men's Clothes, Women's Clothes, Unisex, Youth}
        Accessories{Jewlery, Baggage, Headwear, Shoes}
        Fabric{Commericial, Residential}
    }
    Level 4 Categories{
        Men's Clothing{}
        Womens's Clothing{}
        Youth Clothing{}
        Shoes{Men, womens, youth}
    }


    The purpose is to make the finalTable easy to read and categorize for the use of CategoryIQ api
"""

class levels():


    def defining_levels(path, target_level):
        """ Test xlsx for seeing the output of the level schemes without messing up FinalTable """
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


        """ Problem: How does one group these items in nested groups? It should be like a tree with its branches, the higher you go the less thick the branch is but the more leaves that grow """
        for i in mentioned_byVariable:
            mentioned_byVariable.groupby(i)
            
        
        
    

        