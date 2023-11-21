# import python packages
import urllib.request
import ssl
import requests, zipfile
from io import BytesIO
import os
print(os.getcwd())
print("Creating folders started")

# os.mkdir("../data/landing/ABS_data")


# os.mkdir("../data/raw/ABS_data")


# os.mkdir("../data/curated/ABS_data")



print("Creating folders completed")

print('Downloading started')

# This can be used to download of the the data from the github into the landing data page
# urllib.request.urlretrieve("https://raw.githubusercontent.com/kllin2/project2_group20/main/SA2%20(EN)%20by%20CPRF%20Count%20of%20Persons%20in%20Family.csv",
#                            "../data/landing/ABS_data/SA2_(EN)_by_CPRF_Count_of_Persons_in_Family.csv"
#                            )
# urllib.request.urlretrieve("https://raw.githubusercontent.com/kllin2/project2_group20/main/SA2%20(EN)%20by%20RNTRD%20Rent%20(weekly)%20Ranges%20and%20HIND%20Total%20Household.csv",
#                             "../data/landing/ABS_data/SA2_(EN)_by_RNTRD_Rent_(weekly)_Ranges_and_HIND_Total_Household.csv"
#                            )
# urllib.request.urlretrieve("https://raw.githubusercontent.com/kllin2/project2_group20/main/SA2%20(EN)%20by%20STRD%20Dwelling%20Structure.csv",
#                            "../data/landing/ABS_data/SA2_(EN)_by_STRD_Dwelling_Structure.csv"
#                            )
# urllib.request.urlretrieve("https://raw.githubusercontent.com/kllin2/project2_group20/main/SA2%20(EN)%20by%20FNOF%20Family%20Number.csv",
#                            "../data/landing/ABS_data/SA2_(EN)_by_FNOF_Family_Number.csv"
#                            )


urllib.request.urlretrieve("https://github.com/kllin2/project2_group20/blob/main/"
                           "2021SA2%20(UR)%20by%20HRWRP%20Hours%20Worked%20(ranges).csv",
                            "../data/landing/ABS_data/2021SA2 (UR) by HRWRP Hours Worked (ranges).csv"
                           )
urllib.request.urlretrieve("https://github.com/kllin2/project2_group20/blob/main/"
                           "2021SA2%20(UR)%20by%201-digit%20level%20OCCP%20Occupation.csv",
                           "../data/landing/ABS_data/2021SA2 (UR) by 1-digit level OCCP Occupation.csv"
                           )
urllib.request.urlretrieve("https://github.com/kllin2/project2_group20/blob/main/"
                           "SA2%20by%20HCFMD%20Family%20Household%20Composition%20(Dwelling).csv",
                           "../data/landing/ABS_data/SA2 by HCFMD Family Household Composition (Dwelling).csv"
                           )

print('Downloading Completed')

# https://github.com/kllin2/project2_group20/blob/main/SA2%20(EN)%20by%20CPRF%20Count%20of%20Persons%20in%20Family.csv