class dictionary():
    def dictionary():
      cat_info_dict = [
         { 
            """ Will need to manualy make top 4 categories lvl 1 """
            'category_name': 'categories',
            'level_data': [ 
               #Property
                  { 
                     'level': 2,
                     'level_name':'Property',
                     'sub_categories': ['Vehicles','Housing Expenses','Physical Assets', 'Real Estate'],
                  },
                  { 
                     'level': 3,
                     'level_name': 'Vehicles',
                     'sub_categories': ['Cars','Car Upkeep', 'Other Vehicles'],
                  },
                  { 
                     'level': 4,
                     'level_name': 'Cars',
                     'sub_categories': ['Acura', 'Alfa Romeo','AMC', 'Aston Martin', 'Audi', 'Austin', 'Bentley', 'BMW',
                     'Buick', 'Cadillac', 'Chevrolet', 'Checker', 'Chrysler', 'Citroen','Daihastu', 'Datsun','Dodge',
                     'Eagle', 'English Ford', 'Ferrari', 'Fiat', 'Ford', 'Geo', 'GMC', 'Honda', 'Hyundai', 'Infiniti',
                     'International', 'Isuzu', 'Jaguar', 'Jeep', 'Jensen', 'Kia', 'Lancia', 'Land Rover', 'Lexus', 'Lincoln', 'Lotus',
                     'Maserati', 'Mazda', 'Mercedes', 'Mercury', 'MG', 'Mitsubishi', 'Mini', 'NSU', 'Oldsmobile', 'Opel', 
                     'Pace', 'Packard', 'Peugot', 'Plymouth', 'Pontiac', 'Porche', 'Ram', 'Rambler', 'Range', 'Renault',
                     'Rolls Royce', 'Rover', 'SAAB', 'Saturn', 'Shelby', 'Simca', 'Studebaker', 'Suburu', 'Sunbeam', 'Suzuki', 'Toyota', 'Triumph',
                     'Volkswagen', 'Volvo', 'Willys', 'Winnebago','Other'],
                  },
                  {
                     'level': 3,
                     'level_name': 'Housing Expenses',
                     'sub_categories': ['Utilities', 'Construction', 'House Upkeep', 'Furniture']
                  },

                  #Begin Income/Expenses
                  {
                     'level': 2,
                     'level_name': 'Expenses/Income',
                     'sub_categories': ['Leisure', 'Financial Assets', 'Transport', 'Education', 'Health', 'Income', 'Other Expenditures', 'Consumables'],
                  },
                  {
                     'level': 3,
                     'level_name': 'Transport',
                     'sub_categories': ['Rental', 'Fares'],
                  },
                  { 
                     'level': 3,
                     'level_name': 'Health',
                     'sub_categories': ['Health Insurance', 'Clinical Action', 'Health Equipment', 'Fares'],
                  },
                  {
                     'level': 3,
                     'level_name': 'Income',
                     'sub_categories': ['Employment', 'Government Assistance'],
                  },
                  {
                     'level': 3,
                     'level_name': 'Other Expenditures',
                     'sub_categories': ['Fees', 'Insurance'],
                  },
                  {
                     'level': 3,
                     'level_name': 'Consumables',
                     'sub_categories': ['Food', 'Drinks', 'Alcohol'],
                  },
                  {
                     'level': 3,
                     'level_name': 'Consumables',
                     'sub_categories': ['Food', 'Drinks', 'Alcohal'],
                  },
                  #Clothing, Fabric, and Accessories 
                  {
                     'level': 2,
                     'level_name': 'Clothing, Fabric, Accessories',
                     'sub_categories': ['Clothing', 'Accessories', 'Fabric'],
                  },
                  {
                     'level': 3,
                     'level_name': 'Clothing',
                     'sub_categories': ["Men's Clothes", "Women's Clothes", 'Other Clothing', 'Youth Clothing'],
                  },
                  {
                     'level': 3,
                     'level_name': 'Clothing',
                     'sub_categories': ["Men's Clothes", "Women's Clothes", 'Other Clothing', 'Youth Clothing'],
                  },
                  {
                     'level': 4,
                     'level_name': 'Youth Clothing',
                     'sub_categories': ["Boy's Clothing", "Girl's Clothing", "Infant's Clothing"],
                  },
                  {
                     'level': 3,
                     'level_name': 'Accessories',
                     'sub_categories': ['Jewelry', 'Headwear', 'Shoes', 'Electronics', 'Cosmetics', 'Hygiene'],
                  },
                  
                  #Other
                  {
                     'level': 2,
                     'level_name': 'Other',
                     'sub_categories': ['NaN', 'Question'],
                  }

            ] 
         }
      ]
            
      return cat_info_dict

""" REFERENCE COMMENTARY """
""" NOTE: Because of the dictionary setup, the four primary categories: [ Property, Expenses/Income, 'Clothing, Fabric, Accessories', Other ]
            are all Level 1 Categories, and need to be assigned at the moment of column (level[#]) assignment"""
"""
    Level 1 Categories{
        "Property",
        "Expenses/Income",
        "Clothing, Fabric, Accessories",
        "Other"
    }

    Level 2 Categories{
        Property{Vehicles, Housing Expenses, Physical Assets, Real Estate}
        Expenses/Income{Leisure, Financial Assests, Transport, Education, Health, Income, Other Expenditures, Consumables}
        Other{Catch all for things that dont fit anywhere else/Irrelevant/Errors}
        Clothing, Fabric, Acessories{Clothing, Accessories, Fabric}
    }

    Level 3 Categories{
        Other Expenditures{Fees, Insurance}
        Consumables{Food, Drinks, Alcohol}
        Vehicles{Car, Car Upkeep, Other Vehicles}
        Housing Expenses{Utilities, Construction, House Upkeep, Furniture}
        Income{Employment, Government Assitance}
        Health{Health Insurance, Clinical Action, Health Equipment}
        Clothing{Men's Clothes, Women's Clothes, Other Clothing, Youth Clothing}
        Accessories{Jewlery, Headwear, Shoes, Electronics, Cosmetics, Hygiene}
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