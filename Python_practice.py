counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print("The " + str(county)+ " county has " +str(voters)+ " rsgistered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for i in range(len(voting_data)):

      print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for county_dict in voting_data:

     print(county_dict['registered_voters'])


for county_dict in voting_data:
    print(county_dict['county'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

