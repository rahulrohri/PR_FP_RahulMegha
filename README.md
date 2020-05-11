## Final Project for IS590PR  - University of Illinois - Urbana Champaign
## Analysis of Public Safety Trends in New York City

## Project Overview
New York City is considered to be the 'Dream City' by people all across the globe. It is home to some of the most iconic attractions like the Empire State building, Times Square, Brooklyn Bridge and the Broadway theater to name a few. NYC majorly comprises of 5 boroughs, Bronx, Brooklyn, Manhattan, Queens and Staten Island out of which Manhattan is among the world’s major commercial, financial and cultural centers. Being avid admirers of The Big Apple ourselves, both of us were very intrigued to know more about how habitable this city is, in terms of the safety aspect. We took into consideration a variety of elements relating to public safety like the Crime and Arrest data, various social aspects like 'Racism Prevalent' and how quickly or slowly emergency services assist people. Our analysis will prove to be beneficial to anyone who is planning to move to NYC as it will enable you to weigh factors that contribute in making a city amicable. Our results are depicted per borough that will facilitate you in concluding which borough will be the most pertinent to your preferences.


## Team Members
1) Megha Manglani (GitHub id – meghamm2)
2) Rahul Ohri (GitHub id- rahulrohri)

## Files and Folders in our GitHub Repository
### 1. [Final_Code_IS590PR_Import_Func.ipynb](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Code_IS590PR_Import_Func.ipynb)
 - In this notebook we are not explicitly creating functions. It is rather importing our already developed functions from the   [Final_Project_Code_IS590PR_Functions.py](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Project_Code_IS590PR_Functions.py) file. Please ensure both these files are located in the same folder.There is another jupyter notebook named [Final_Project_Code_IS590PR.ipynb](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Project_Code_IS590PR.ipynb) which contains the entire code (including functions, graphs and doctests).
### 2. [Final_Project_Code_IS590PR.ipynb](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Project_Code_IS590PR.ipynb)
 - In this notebook we are explicitly creating functions, writing doctests and checking if the doctests passed or not. There is another jupyter notebook named [Final_Code_IS590PR_Import_Func](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Code_IS590PR_Import_Func.ipynb) which contains the entire code without explicit function creation. In that notebook, the functions are being imported from the Final_Project_Code_IS590PR_Functions.py file.
### 3. [Final_Project_Code_IS590PR.py](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Project_Code_IS590PR.py)
 - The file is exactly same as the notebook file above. It is just included for convenience as a .py version in case the user directly wants to run it in pycharm or any other software. Running this can get a bit complicated , so we would advise that the user referes to our file  - [How_to_run_Final_Project_Code_IS590PR.pdf](https://github.com/rahulrohri/final_project_2020Sp/blob/master/How%20to%20run%20Final_Project_Code_IS590PR.pdf) for ease of use. We strongly suggest that the user runs our code using either files [Final_Project_Code_IS590PR.ipynb](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Project_Code_IS590PR.ipynb) or [Final_Code_IS590PR_Import_Func.ipynb](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Code_IS590PR_Import_Func.ipynb)
### 4. [Final_Project_Code_IS590PR_Functions.py](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Project_Code_IS590PR_Functions.py)
 - This file can be used to check doctest coverage. This file serves as an input to the notebook [Final_Code_IS590PR_Import_Func.ipynb](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Code_IS590PR_Import_Func.ipynb) and needs to be imported at the start to load all necessary functions
### 5. [How to run Final_Project_Code_IS590PR.pdf](https://github.com/rahulrohri/final_project_2020Sp/blob/master/How%20to%20run%20Final_Project_Code_IS590PR.pdf)
 - This instruction files is used as a reference to run the [Final_Project_Code_IS590PR_Functions.py](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Final_Project_Code_IS590PR_Functions.py) file
### 6. [Older Versions of Code](https://github.com/rahulrohri/final_project_2020Sp/tree/master/Older%20Versions%20of%20Code)
 - This folder was used to track the version control for our project. It contains all the notebooks our team made throughout this project. These files should not be downloaded as they are incomplete versions of our code.
### 7. [Images](https://github.com/rahulrohri/final_project_2020Sp/tree/master/Images)
 - This folder contains all the images that were generated for our hypotheses. They just serve as a reference to be imported for our Read.me file
### 8. [DocTest Dummy Files](https://github.com/rahulrohri/final_project_2020Sp/tree/master/DocTest%20Dummy%20Files)
 - The folder contains all the dummy csv files that we had created to test our doctests across the numerous functions that we created. These dummy files hold no significance in the actual code for our project.

## Datasets used for our analysis
Since the files are over 6.5 gb , we could not upload them on github and have hence provided a google drive link from where the datasets used for our project can be downloaded -> https://drive.google.com/open?id=1g_StaWiaWQyNjNOu3wlFKG2dsIJZjyjF


## Updated datasets can be downloaded from these official data sources
https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i<br /> 
https://catalog.data.gov/dataset/nypd-arrests-data-historic<br /> 
https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Neighborhood-Tabulatio/swpk-hqdp<br /> 
https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj<br /> 
https://worldpopulationreview.com/us-cities/new-york-city-population/ <br/>
https://en.wikipedia.org/wiki/Demographics_of_New_York_City<br/> 


## Hypothesis 1:
The number of crimes decreased in neighborhoods where the previous number of arrests is high indicating that maybe the police force is handling the situations better.

![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%201%20-%20Part%201.PNG?raw=true)
![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%201%20-%20Part%202.PNG?raw=true)

### Conclusion: 
The graphs indicate that in majority of the boroughs , as the number of crimes decrease, the number of arrests decrease as well. Thus, our hypothesis does not stand true.


## Hypothesis 2:
There exist certain types of crimes where there is prejudice against the victims of a race

![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%202%20-%20Part%201.PNG?raw=true)
![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%202%20-%20Part%202.PNG?raw=true)
![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%202%20-%20Part%203.PNG?raw=true)
![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%202%20-%20Part%204.PNG?raw=true)

### Conclusion: 
In majority of the crimes we analyzed (for example Larceny, Felony, Assault etc.) Black and White Hispanics in general have been targeted the most. Thus, our hypothesis does stand true.

## Hypothesis 3:
The population density of a neighborhood impacts the number of complaints/crimes reported there.(E.g. Is there an inverse trend of the number of crimes with the population density or not).

![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%203.PNG?raw=true)

### Conclusion: 
Despite there being a relatively strong correlation of 0.7275 between the population density and crime per capita, we did not see an inverse trend across all boroughs. Thus, our hypothesis does not stand true.

## Hypothesis 4:
There exists a trend between the type of crimes reported in NYC and the neighborhood they occurred in. (e.g. There are a greater number of theft cases in Brooklyn than any other region)

![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%204%20-%20Part%201.PNG?raw=true)
![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%204%20-%20Part%202.PNG?raw=true)

### Conclusion: 
We observed that in Brooklyn , burglary crime count was relatively the highest whereas Felony Assault was relatively the highest in Bronx. Frauds in general were very low compared to other crimes in NYC

## Hypothesis 5:
The population density is directly proportional the average response time taken by an emergency unit to respond to that incident. (E.g. Are the instances of the vehicle taking more time to reach the emergency spot greater in densely populated neighborhoods?).

![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%205%20-%20Part%201.PNG?raw=true)
![alt text](https://github.com/rahulrohri/final_project_2020Sp/blob/master/Images/Hypothesis%205%20-%20part%202.PNG?raw=true)



### Conclusion: 
The graphs indicate that in majority of the boroughs , The average incident time was higher for boroughs with a higher population density. Staten Island has the fastest average response time whereas Manhattan had an average response time of over 12 minutes over the past one year.


## References:<br /> 
https://github.com/iSchool-590pr/PR_Sp20_examples/blob/master/week_07/class7_pandas_pt2.ipynb <br /> 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html <br /> 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html <br /> 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_index.html <br /> 
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html <br /> 
https://stackoverflow.com/questions/41800424/remove-rows-in-python-less-than-a-certain-value <br /> 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html <br /> 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html <br /> 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html <br />
https://stackoverflow.com/questions/25386870/pandas-plotting-with-multi-index<br />
https://stackoverflow.com/questions/49350445/correlation-coefficient-of-two-columns-in-pandas-dataframe-with-corr<br/> 
https://pandas.pydata.org/pandas-docs/version/0.16.0/visualization.html<br />
https://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns-apply-a-function-o
https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/<br/>   


