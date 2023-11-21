import re
import pandas as pd
from json import dump
from bs4 import BeautifulSoup
import requests

#start a request session
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})

# link from which to retrieve informations
URL = "https://www.australia-shoppings.com/malls-centres/victoria"

bs_object = BeautifulSoup(session.get(URL).text, "lxml")

# a dictionary to store informations 
shopping_centers = {}

# name of the shopping centers 
shopping_centers['name'] = [shopping_centers.text for shopping_centers in bs_object\
                            .find("ul", {"class": "malls-list"})\
                            .findAll("h3", {"class": "tit"})] 


#relevant information for the shopping center
shopping_centers['information'] = [info.text for info in bs_object\
                                  .find("ul", {"class" : "malls-list"})\
                                  .findAll("p", {"class" : "st"})]

shopping_center_df = pd.DataFrame(shopping_centers)
# save the downloaded file to landing
shopping_center_df.to_csv('../data/landing/shopping_center.csv', index=False)
