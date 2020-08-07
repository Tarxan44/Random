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
    5. Vision for the code is to have have a table like below uploaded to SQl database
    Table Should look:
    Level 1{Name, Subcategory Names, Market info}
    Level 2{Name, Subcategory Names, Market info}
    ...
    Invisible Level 6(categories from BLS survey){Categories,}


    Level 1 Categories{
        "Property",
        "Expenses/Income",
        "Clothing, Fabric, Accessories",
        "Other"
    }

    Level 2 Categories{
        Property{Vehicles, Housing Expenses, Physical Assets, Real Estate}
        Expenses/Income{Leisure, Financial Assets, Transport, Education, Health, Income, Other Expenditures, Consumables}
        Other{Catch all for things that dont fit anywhere else/Irrelevant/Errors}
        Clothing, Fabric, Accessories{Clothing, Accessories, Fabric}
    }
    Changes: Savings, Stocks&Bonds combined to Financial Assets, Food/Drink changed to Consumables

    Level 3 Categories{
        Other Expenditures{Fees, Insurance}
        Consumables{Food, Drinks, Alcohol}
        Vehicles{Car, Car Upkeep, Other Vehicles}
        Housing Expenses{Utilities, Construction, House Upkeep, Furniture}
        Income{Employment, Government Assistance}
        Health{Health Insurance, Clinical Action, Health Equipment}
        Clothing{Men's Clothes, Women's Clothes, Other Clothing, Youth Clothing}
        Accessories{Jewelery, Headwear, Shoes, Electronics, Cosmetics, Hygiene}
        Transport{Rental, Fares}
    }

    Level 4 Categories{
        Youth Clothing{Boys Clothing, Girls Clothing, Infants Clothing}
        Car{Acura, Alfa Romeo, AMC, Aston Martin, Audi, Austin, Bentley, BMW,
        Buick, Cadillac, Chevrolet, Checker, Chrysler, Citroen,Daihastu, Datsun, Dodge,
        Eagle, English Ford, Ferrari, Fiat, Ford, Geo, GMC, Honda, Hyundai, Infiniti,
        International, Isuzu, Jaguar, Jeep, Jensen, Kia, Lancia, Land Rover, Lexus, Lincoln, Lotus,
        Maserati, Mazda, Mercedes, Mercury, MG, Mitsubishi, Mini, NSU, Oldsmobile, Opel, 
        Pace, Packard, Peugot, Plymouth, Pontiac, Porche, Ram, Rambler, Range, Renault,
        Rolls Royce, Rover, SAAB, Saturn, Shelby, Simca, Studebaker, Suburu, Sunbeam, Suzuki, Toyota, Triumph,
        Volkswagen, Volvo, Willys, Winnebago,Other}
        Employment{Government Employment, Regular Employment}
        
    Other Categories{
        NaN - not applicable
        Question - unsure where to place/new category needed
        Air Condition combo? Row 371 -Heating, AC
        Dishwasher combo row 1313
        Downloading Audio/Video Row 1386
        Stove and oven? 3217, 3236, 4355
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
            
        
        
    

        