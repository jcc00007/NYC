[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/SGWUF1eE)
# Generic Real Estate Consulting Project

## Group 20
- Members: 
  - `Ke (Nicole) Lin 1253385`
  - `JinCong Chen 1264476`
  - `Jinchen (Sarah) Yuan 1174082`
  - `Zihan Zhang 1238857`
  - `Jialei Wu 1266384`


**Research Goal:** 
This industry project aims to predict rental prices for both residential properties and apartments throughout Victoria, Australia

We aimed to answer the following three questions:

1. What are the most important internal and external features in predicting rental prices? (This can be at the granularity of the groups’ choosing)
2. What are the top 10 suburbs with the highest predicted growth rate?
3. What are the most liveable and affordable suburbs according to your chosen metrics?


**Timeline:** 
* We scraped the rental price data that are currently listing on the domain website


**Data Source:**
* Property datasets: data scraped from www.domain.com.au
* To download the data, please run `scrape_domain.py` in the `scripts` folder

* External datasets:
1. SA2_(EN)_by_FNOF_Family_Number.csv
2. SA2_(EN)_by_STRD_Dwelling_Structure.csv
3. SA2 (UR) by 1-digit level OCCP Occupation.csv
4. SA2_(EN)_by_CPRF_Count_of_Persons_in_Family.csv
5. inflation: https://www.macrotrends.net/countries/AUS/australia/inflation-rate-cpi
6. historical rental by suburb: https://discover.data.vic.gov.au/dataset/rental-report-quarterly-moving-annual-rents-by-suburb
7. Public transport data (with geospatial location) from Victoria Datashare (https://datashare.maps.vic.gov.au/).
        Download url = "https://s3.ap-southeast-2.amazonaws.com/cl-isd-prd-datashare-s3-delivery/Order_HI08BK.zip"
        Important notice:
        If The link is expired, please follow the instruction to reorder the dataset
        
        It is free data, however, you need to create an account first access (also free to register)
                    1. go to https://datashare.maps.vic.gov.au/ and search "Public Transport a collection of PTV datasets"
                    2. Press "Add to order" and "proceed to order configuration" buttom
                    3. Scroll down and change the data options to: (Projection: Geographicals on GDA94
                                                                    Buffer: No buffer
                                                                    File Format: ESRI File Geodatabase
                                                                    Select map area: Custom Cookie-  VICTORIA_BUFF (make sure press apply))
                    4. The data will be sent by email within 24 hours


8. Victoria's Crime statistic from Crime Statistics Agency Victoria
        download url  = https://files.crimestatistics.vic.gov.au/2023-06/Data_Tables_LGA_Criminal_Incidents_Year_Ending_March_2023.xlsx

9. Australian Postcode data
        download url = https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv


   

**Notebook Summary:**
To run the pipeline, please visit the `scripts` and `notebook` directory and run the files in order:

1. Run the `1.15 Preprocessing_public_transport.ipynb` in `notebook` folder which will download PTV data and preprocess both SAL and SA2 shapefile data. Processed data will be located in `data/raw/victoria_region_gdf`
2. Run the `1.18 Preprocessing_SA2_to_SAL.ipynb` in the `notebook` folder which will create a file that give a one to one correspondance between SAL and SA2 regions. Output file will be stored in `/curated/SA2_to_SAL.csv`

3. Run the `1.1 Preprocessing_domain_1.ipynb` in the `notebook` folder which will do column information extraction for the listing data from domain. Processed file will be located in `data/raw/listings.csv`
4. Run the `1.2 Preprocessing_domain_2.ipynb` in the `notebook` folder which will apply business rule to the listing data and get geographic information for each property. Processed file will be available in two format. csv: `data/curated/listings_suburbs_SA2.csv` and shapefile: `data/curated/listings_suburbs_SA2.shp`
5. Run the `3.4 Geovisualisation_rent.ipynb` in the `notebook` folder which will visualise the median price for different SA2 regions 

6.  Run `1.15 Preprocessing_public_transport.ipynb` which will run the script of `PTV_Download.py` in `scripts` to download PTV data to `data/landing` and Preprocess the each Train, Bus and Tram data and determine which SAL region each public transport stations belong to. Data saved in `data/raw/PTV/`
7.   Run `1.16 Preprocessing_aggregating_PTV.ipynb` which will apply data aggregation to PTV data and combining data for all public transport (tram, train and bus) find total public transport station count in each suburb region (SAL). Final data will be saved as PTV_count_with_SAL.csv in `data/curated` folder
8.   Run `3.1 Visualising_public_transport.ipynb` which will generate a visualisation of public transport station count within each suburb(SAL). The visual will be saved as Public_transport_count_SAL.html in `plots` folder
9.    Run `1.10 Preprocessing_postcode.ipynb` which will run the script of `Postcode_Download.py` to downlaod Victoria's postcode. Data will then be save in raw as location_postcode.csv

10. Run `1.14 Preprocessing_crime.ipynb` which will run the script of `Crime_Download.py` in `script` to download Victoria's Crime statistic/count in each locality. This notebook will then continue to preprocess the data, grouping/counting number of crime instance by year,postcode,suburb and join with victoria's postcode data we obtian previous then save the data `crime_count_with_point_geo.geojson` in raw folder
11. Run `2.4 Preliminary_Visualisation_Crime_SAL.ipynb` which will first join the crime data with SAL data. Then determine crime rate (number of crime instance per population) within each SAL/suburb region saved as crime_rate.csv in `curated`folder.
12. Run `2.6 Analysing_crime_rate.ipynb` which will generate a map that display the crime rate of indvidual suburb and save the visual as crime_rate_visual.html in `plots` folder

13. Run `3.2 Visualising_school.ipynb` will generate visualisation teh school count in each suburb
14. Run `Livability.ipynb` in the `notebook` folder which will calculate the most livable and affordable suburbs as well as some geovisualisations for those suburbs
15. Run `Regression.ipynb` in the `Model` folder which will run a linear regression model which will present the most relevant internal and external features for predicting rent price.
16. Run `Time Series Regression.ipynb` in the `Model` folder which will run a time series regression model that will predict the rent price for all the suburbs with some visualisations.



**Assumption:**
1. We predicted the rental price for the traditional residential houses or apartments on a weekly basis.
2. For the rental prices that are listed in the range on www.domain.com, we took the lowest price as the price data.
3. Cells in the table that were downloaded from the ABS, some of them have been randomly adjusted to avoid the release of confidential data. Therefore, we treated those "hidden" data as 0.
4. To improve efficiency of downloading the useful datasets, we used the internal tool called "TableBuilder" to extract and download relevant datasets. Since it is an internal tool, it cannot be accessed after 28days, therefore, we directly saved the ABS datasets to the Landing folder.
5. We decided the melbourne cbd is "Melbourne Central Station", geometry is "37.8102° S, 144.9628° E" by google.
6. Assume every suburb in Victoria has similar crime rate as the overall crime rate in victoria, that we will estimate those suburb with missing value to have same crime rate as the victoria state.
