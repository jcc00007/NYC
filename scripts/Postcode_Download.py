from urllib.request import urlretrieve
import requests
import os


# This notebook will download postcode data inclding geometry within victoria 

# Define the URL of the CSV file you want to download
url = 'https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv'

# Specify the folder where you want to save the downloaded file
download_folder = '../data/landing/postcode'

# Ensure the download folder exists, create it if necessary
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Extract the file name from the URL
file_name = url.split('/')[-1]

# Define the complete path to save the file
file_path = os.path.join(download_folder, file_name)

# Send an HTTP GET request to the URL to download the file
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open the file in binary write mode and save the content
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f'File downloaded and saved as: {file_path}')
else:
    print(f'Failed to download the file. Status code: {response.status_code}')
