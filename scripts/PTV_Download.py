import os
import zipfile
from urllib.request import urlretrieve

# this script will download the PTV data file





# make directory
output_relative_dir = '../data/landing/'

if not os.path.exists(output_relative_dir):
    os.makedirs(output_relative_dir)
    

target_dir = 'PTV DATA'
if not os.path.exists(output_relative_dir + target_dir):
    os.makedirs(output_relative_dir + target_dir)

# download file with the url from Victoria Datashare
url = 'https://s3.ap-southeast-2.amazonaws.com/cl-isd-prd-datashare-s3-delivery/Order_HI08BK.zip' 

print(f"Begin download PTV data")
output_dir = f'{output_relative_dir}{target_dir}/'
zip_path, _ = urlretrieve(url)
print(f"complete download PTV data")

# unzip the file 
print(f"Begin unzip PTV data")
with zipfile.ZipFile(zip_path, "r") as f:
    f.extractall(output_dir)
print(f"complete unzip PTV data")