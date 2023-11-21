import re
import pandas as pd
from json import dump
from collections import defaultdict
from bs4 import BeautifulSoup
import requests


#start a request session
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})

# constants
BASE_URL = "https://www.domain.com.au"
N_PAGES = range(1, 51)
postcodes = range(3000, 4000)# VIC postcode range

# postcodes = range(3000, 4000) # VIC postcode range


# begin code
url_links = []
property_metadata = defaultdict(dict)


# generate list of urls to visit
for postcode in postcodes:
    # check the number of hourses in that region
    url = BASE_URL + f"/rent/?sort=default-desc&postcode={postcode}"
    print(f"Visiting {url}")
    bs_object = BeautifulSoup(session.get(url).text, "lxml")


    try:
        # check the number of properties in the region
        num_properties = bs_object \
        .find('h1',{"class":"css-ekkwk0"}).text
    
        num_properties = int(re.findall('(\d+) (?:Properties|Property)', num_properties)[0])

        N_PAGES = range(1, num_properties // 20 + 2) # there are roughly 20 properties per page
    except AttributeError:
        print(f'AttributeError visiting {url}')


    
    if num_properties >= 1:
        for page in N_PAGES:   
            url = BASE_URL + f"/rent/?sort=default-desc&postcode={postcode}&page={page}"
            print(f"Visiting {url}")
            bs_object = BeautifulSoup(session.get(url).text, "lxml")
            
            # find the unordered list (ul) elements which are the results, then
            # find all href (a) tags that are from the base_url website.
            try:
                index_links = bs_object \
                    .find(
                        "ul",
                        {"data-testid": "results"}
                    ) \
                    .findAll(
                        "a",
                        href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
                    )
               
                for link in index_links:
                    # if its a property address, add it to the list
                    if 'address' in link['class']:
                        url_links.append(link['href'])
            except AttributeError:
                print(f'{url} Attribute Error')

    
    
    for page in N_PAGES:   
        url = BASE_URL + f"/rent/?sort=default-desc&postcode={postcode}&page={page}"
        print(f"Visiting {url}")
        bs_object = BeautifulSoup(session.get(url).text, "lxml")
       
        # find the unordered list (ul) elements which are the results, then
        # find all href (a) tags that are from the base_url website.
        index_links = bs_object \
            .find(
                "ul",
                {"data-testid": "results"}
            ) \
            .findAll(
                "a",
                href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
            )
       
        for link in index_links:
            # if its a property address, add it to the list
            if 'address' in link['class']:
                url_links.append(link['href'])



# for each url, scrape some basic metadata
for property_url in url_links[1:]:
    print(f'visiting {property_url}')
    bs_object = BeautifulSoup(session.get(property_url).text, "lxml")
    try: 

        # Street Address
        property_metadata[property_url]['Location'] = bs_object\
        .find('h1', {"class": "css-164r41r"}).text


    except AttributeError:
        print("Address Attribute Error")
        
    try:

        # Type of property
        property_metadata[property_url]['type_property'] = bs_object\
        .find('div', {"data-testid" : "listing-summary-property-type"})\
        .find('span', {"class" : "css-in3yi3"}).text

    except AttributeError:
        print("Property Type Attribute Error")

    try:
        # Price
        property_metadata[property_url]['price'] = bs_object \
        .find('div',{"class" : "css-1texeil"}).text
        
    except AttributeError:
        print("Price Attribute Error")
    try:
        # Schools
        property_metadata[property_url]['school_names'] = [school.text for school in bs_object \
        .find('div', {"data-testid": "listing-details__school-catchment-content"})\
        .findAll("h5", {"data-testid": "fe-co-school-catchment-school-title"})]

        property_metadata[property_url]['school_distance'] = [school.text for school in bs_object \
        .find('div', {"data-testid": "listing-details__school-catchment-content"})\
        .findAll("div", {"data-testid": "fe-co-school-catchment-schoolDistance"})]
    except AttributeError:
        print("School Attribute Error")

    try:
        # Long term residency percentage
        property_metadata[property_url]['LT_resident_pcg'] = bs_object\
        .find('div',{"class":"css-ibsnk8"}).text
    except AttributeError:
        print("residency PCG Attribute Error")

    
    try:
        # Owner and family percentage
        property_metadata[property_url]['owner_pcg'] = [pcg.text for pcg in bs_object\
        .find('div',{"data-testid":"neighbourhood-insights__types"})\
        .findAll('span',{"data-testid":"left-value"})][0]
        
        property_metadata[property_url]['family_pcg'] = [pcg.text for pcg in bs_object\
        .find('div',{"data-testid":"neighbourhood-insights__types"})\
        .findAll('span',{"data-testid":"left-value"})][1]

    except AttributeError:
        print("Owner/Family Percentage Error")

    except IndexError:
        print("Owner/Family Index Error")

        
    # State
    # not all postcodes strictly follows the 3000-3999 in VIC thus need to be checked
    # list of possible contract types and states
    
    states = ['VIC', 'NSW', 'QLD', 'TAS', 'WA', 'SA', 'ACT', 'NT']
    try:


        # Price
        property_metadata[property_url]['price'] = bs_object \
        .find('div',{"class" : "css-1texeil"}).text

        
        # State
        # not all postcodes strictly follows the 3000-3999 in VIC thus need to be checked
        # list of possible contract types and states
        states = ['VIC', 'NSW', 'QLD', 'TAS', 'WA', 'SA', 'ACT', 'NT']
        

        property_type = bs_object \
       .find('nav', {"data-testid":"breadcrumbs"}) \
       .findAll("span", {"class": "css-0"})

        for feature in property_type:
            if feature.text in states:
                property_metadata[property_url]['state'] = feature.text


    except AttributeError:
        print("State Attribute Error")

    try:

        # get rooms and parking
        rooms = bs_object \
                .find("div", {"data-testid": "property-features"}) \
                .findAll("span", {"data-testid": "property-features-text-container"})

        # rooms
        property_metadata[property_url]['rooms'] = [
            re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Bed' in feature.text
        ]
        
        property_metadata[property_url]['bath'] = [
            re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Bath' in feature.text
        ]

        # parking
        property_metadata[property_url]['parking'] = [
            re.findall(r'\S+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Parking' in feature.text
        ]

    except AttributeError:
        print("rooms and parking Attribute Error")


    except AttributeError:
        print('attribute error')





# Save the metadata to a parquet file
data = pd.DataFrame.from_dict(property_metadata).transpose()

data.to_parquet('../data/landing/listings.parquet', engine = 'pyarrow')

data.to_parquet('../data/raw/listings.parquet', engine = 'pyarrow')
            

