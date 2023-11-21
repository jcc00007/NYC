
import os
import requests

## This script will download crime statistic from Crime Statistics Agency Victoria
## the download url is  https://files.crimestatistics.vic.gov.au/2023-06/Data_Tables_LGA_Criminal_Incidents_Year_Ending_March_2023.xlsx


# Specify the download folder
download_folder = "../data/landing/crime_stat"  
# Create the download folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# URL of the file to download
url = "https://files.crimestatistics.vic.gov.au/2023-06/Data_Tables_LGA_Criminal_Incidents_Year_Ending_March_2023.xlsx"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Specify the local file path where you want to save the downloaded file
    file_path = "../data/landing/crime_stat/crime_stat_2023.xlsx"

    # Save the content of the response (the file) to the specified local file
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"File '{file_path}' downloaded successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")