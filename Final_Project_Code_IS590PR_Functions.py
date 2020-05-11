"""
IS590 PR  - University of Illinois - Urbana Champaign
This file is a list of functions that have been used for our project and are
Intended to support the jupyter notebook titled Final_Project_Code_IS590PR.ipynb

Name: NYC_Public_Safety_Functions.py
Team Members :
Megha Manglani (GitHub id – meghamm2)
Rahul Ohri (GitHub id- rahulrohri)

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dir = 'C:/Users/rahul/Downloads/UIUC/Sem 2 - Spring 2020/Courses/Programing Analytics/Final Project/DataSets/' #https://github.com/iSchool-590pr/PR_Sp20_examples/blob/master/week_07/class7_pandas_pt2.ipynb
NYPD_Arrests = my_dir +'NYPD_Arrests_Data__Historic_.csv' # Loading NYPD Arrest Data file
Complaints = my_dir +'NYPD_Complaint_Data_Historic.csv' # Loading NYPD Complaints Data file
EMS_incident = my_dir +'EMS_Incident_Dispatch_Data.csv' # Loading EMS incident dispatch Data file


def dataset_validation():
    """

    This function is used to check if the input data files are having the correct column headers that are needed
    for our hypotheses analysis. The files need to be loaded from the local computer directory since they are
    very large. If the files are not present , then the user can download it from a google drive link provided
    by our team or can go to the official website from which the data was downloaded.


    >>> NYPD_Arrests = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/Arrest_Correct.csv' # Loading NYPD Arrest Data file
    >>> Complaints = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/Complaints_Correct.csv' # Loading NYPD Complaints Data file
    >>> EMS_incident = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/EMS_Correct.csv' # Loading EMS incident dispatch Data file
    >>> dataset_validation()
    The columns necessary for analysis are present in the EMS data file
    The columns necessary for analysis are present in the Complaints data file
    The columns necessary for analysis are present in the Arrests data file
    """

    data_EMS = pd.read_csv(EMS_incident, nrows=1)
    data_Complaints = pd.read_csv(Complaints, nrows=1)
    data_Arrest = pd.read_csv(NYPD_Arrests, nrows=1)
    All_Col_list_EMS = list(data_EMS)
    All_Col_list_Complaints = list(data_Complaints)
    All_Col_list_Arrest = list(data_Arrest)

    Req_Complaints_cols = ['CMPLNT_NUM', 'CMPLNT_FR_DT', 'BORO_NM', 'VIC_RACE', 'OFNS_DESC']
    Req_Arrests_cols = ['ARREST_BORO', 'ARREST_DATE', 'ARREST_KEY']
    Req_EMS_cols = ['INCIDENT_RESPONSE_SECONDS_QY', 'INCIDENT_DATETIME', 'BOROUGH']

    check_EMS = all(item in All_Col_list_EMS for item in
                    Req_EMS_cols)  # https://www.techbeamers.com/program-python-list-contains-elements/
    if check_EMS is True:
        print("The columns necessary for analysis are present in the EMS data file")
    else:
        print(
            "The columns necessary for analysis are not present in the EMS data file. Kindly download the dataset files from - https://drive.google.com/open?id=1g_StaWiaWQyNjNOu3wlFKG2dsIJZjyjF or the latest file from https://data.cityofnewyork.us/Public-Safety/EMS-Incident-Dispatch-Data/76xm-jjuj")
    check_Complaints = all(item in All_Col_list_Complaints for item in
                           Req_Complaints_cols)  # https://www.techbeamers.com/program-python-list-contains-elements/
    if check_Complaints is True:
        print("The columns necessary for analysis are present in the Complaints data file")
    else:
        print(
            "The columns necessary for analysis are not present in the Complaints data file. Kindly download the dataset files from - https://drive.google.com/open?id=112LOH-fYjUn5AHVnFbgQYRAAhSCcXvjq or the latest file from https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i ")

    check_Arrests = all(item in All_Col_list_Arrest for item in
                        Req_Arrests_cols)  # https://www.techbeamers.com/program-python-list-contains-elements/
    if check_Arrests is True:
        print("The columns necessary for analysis are present in the Arrests data file")
    else:
        print(
            "The columns necessary for analysis are not present in the Arrests data file. Kindly download the dataset files from - https://drive.google.com/open?id=1g_StaWiaWQyNjNOu3wlFKG2dsIJZjyjF or the latest file from https://catalog.data.gov/dataset/nypd-arrests-data-historic")


def get_file(file, cols) -> pd.DataFrame:
    """
    This function produced a dataframe that consists of the columns that are needed fr analysis from a datafile.
    Since in our project we are using between 2 - 4 columns for each hypothesis analysis rather than loading the
    entire data file, the dataframe will end up containing only between 2-4 columns.
    >>> test_file = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/Airplane.csv'
    >>> print("Enter 'AircraftHex' and 'SessionID' as column names")
    Enter 'AircraftHex' and 'SessionID' as column names
    >>> answer = get_file(test_file,2)
    enter your column name 1 and press enter:enter your column name 2 and press enter:
    >>> answer.iloc[0]['AircraftHex']
    'A902B5'
    >>> test_file = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/Airplane.csv'
    >>> get_file(test_file,5)
    'Invalid number of columns'
    """

    if cols == 2:
        col1 = input('enter your column name 1 and press enter:')
        # print(type(col1))
        col2 = input('enter your column name 2 and press enter:')
        col_list = [col1, col2]
    elif cols == 3:
        col1 = input('enter your column name 1 and press enter:')
        # print(type(col1))
        col2 = input('enter your column name 2 and press enter:')
        col3 = input('enter your column name 3 and press enter:')
        col_list = [col1, col2, col3]
    elif cols == 4:
        col1 = input('enter your column name 1 inside and press enter:')
        col2 = input('enter your column name 2 inside and press enter:')
        col3 = input('enter your column name 3 inside and press enter:')
        col4 = input('enter your column name 4 inside and press enter:')
        col_list = [col1, col2, col3, col4]
    else:
        return "Invalid number of columns"
    data_file = pd.read_csv(file, usecols=col_list)  # Import only necessary columns from the dataset
    return data_file


# Extracting the Month and Year of the incident
def extract_year_month(x, old_col: str, month_column: str, year_column: str):
    """
    This function is used to extract the year and the month from an existing dataframe column that
    contains date values in the format mm/dd/yyyy. The extraction process results in the formation
    of two new columns in the dataframe - one containing only the months and the other containing only
    the year values.

    :param x: The dataframe on which opeartions are to be performed
    :param old_col: The dataframe column containing date in format mm/dd/yyyy
    :param month_column: The dataframe column to be created post extraction of the month from the column name old_col
    :param year_column: The dataframe column to be created post extraction of the year from the column name old_col
    >>> sample_csv = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/sample_date_func.csv'
    >>> sample_df = pd.read_csv(sample_csv)
    >>> answer = extract_year_month(sample_df,'Date','Month','Year')
    >>> answer.iloc[0]['Population'] #doctest: +NORMALIZE_WHITESPACE
    8300124
    """
    x[month_column] = x[old_col].str[:2]
    x[year_column] = x[old_col].str[6:10]
    return x


def get_arrest_or_crime_count(dfname, col_year, col_month, col_boro, col_key) -> pd.core.frame.DataFrame:
    """
    This function is used to create a multilevel index dataframe that groups the data by the
    neighbourhood, year , and month columns and finally produces a column of the aggragation
    type as count to display either the total count of arrests or the total count of complaints

    :param dfname: The dataframe on which opeartions are to be performed
    :param col_year: Column name containing year value
    :param col_month: Column name containing month value
    :param col_boro:Column name containing borough/area value
    :param col_key: Column name on which aggreagation has to be done
    :return: a dataframe containing year,month,neighbourhood,aggregated column count

    >>> sample_csv = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/arrest_crime_count_function.csv'
    >>> sample_df = pd.read_csv(sample_csv)
    >>> answer = get_arrest_or_crime_count(sample_df,'Complaint_Filed_Year','Complaint_Filed_Month','BORO_NM','CMPLNT_NUM')
    >>> answer.index.levels[1]
    Int64Index([2006, 2009, 2011, 2015], dtype='int64', name='Complaint_Filed_Year')
    """

    # replacing Borough initials with complete names
    dfname = dfname.dropna(subset=[col_year])
    dfname = dfname.astype({col_year: 'int64'})
    dfname = dfname[dfname[col_year] > 2005]
    data_count = dfname.groupby([col_boro, col_year, col_month]).agg({col_key: [
        'count']})  # https://pandas.pydata.org/pandas-docs/version/0.23.1/generated/pandas.core.groupby.DataFrameGroupBy.agg.html
    return data_count


def plot_graph(n, df, l, b, var1: str, var2: str, var3: str, var4: str, var5: str, constant: str):
    '''
    This function is used to plot a line graph for a multilevel index dataframe. The graph has multiple
    subplots as well depending upon the number of index groups in the first column of the dataframe. eg
    in one datframe we have 5 boroughs that are used as the grouping column and thus we will have 5
    subplots

    :param n: number of subplots
    :param df: the dataframe for which graphs have to be plotted
    :param l: length of the subplot figure
    :param b: breadth of the subplot figure
    :param var1: Index value to be plotted
    :param var2: Index value to be plotted
    :param var3: Index value to be plotted
    :param var4: Index value to be plotted
    :param var5: Index value to be plotted
    :param constant: Constant part of text to be displayed in the title of the subplot

    # https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
    >>> arrays = [np.array(['india', 'USA', 'italy', 'italy', 'india', 'canada', 'india', 'USA','australia']),np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two','one'])]
    >>> df_new = pd.DataFrame(np.random.randn(9, 5), index=arrays) #Creating a dummy multi-index dataframe
    >>> plot_graph(5,df_new,18,20,'india','USA','italy','australia','canada','Just testing')
    '''

    figure, axis = plt.subplots(n, 1, figsize=(
    l, b))  # https://stackoverflow.com/questions/25386870/pandas-plotting-with-multi-index
    df.xs(var1).plot(kind='line', ax=axis[0]).set_title(
        var1 + ' - ' + constant)  # https://pandas.pydata.org/pandas-docs/version/0.16.0/visualization.html
    df.xs(var2).plot(kind='line', ax=axis[1]).set_title(var2 + ' - ' + constant)
    df.xs(var3).plot(kind='line', ax=axis[2]).set_title(var3 + ' - ' + constant)
    df.xs(var4).plot(kind='line', ax=axis[3]).set_title(var4 + ' - ' + constant)
    df.xs(var5).plot(kind='line', ax=axis[4]).set_title(var5 + ' - ' + constant)


def race_percentage(row, colname) -> pd.core.series.Series:
    # https://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns-apply-a-function-o
    # https://worldpopulationreview.com/us-cities/new-york-city-population/
    # total NYC population = 8175133
    # Creating a function to add crime per capita values
    """
    This function is used to return a pandas series that has the race percentage value of all the different
    races present in NYC.


    :param row: denotes that the operation has to be performed across rows
    :param colname: Column name on which operation has to be done
    :return : a specific numeric value if a row match is found
    >>> data_dummy = {'Race':  ['AMERICAN INDIAN/ALASKAN NATIVE','ASIAN / PACIFIC ISLANDER', 'BLACK','BLACK HISPANIC','WHITE','WHITE HISPANIC','UNKNOWN/OTHER'],'Offense': ['FRAUDS', 'BURGLARY','HARRASSMENT 2','FORGERY','FRAUDS','FRAUDS','FRAUDS'],'Comp_no':[1,2,3,4,5,6,7]}
    >>> df_dummy = pd.DataFrame (data_dummy, columns = ['Race','Offense','Comp_no'])
    >>> df_dummy.apply (lambda row: race_percentage(row,'Race'), axis=1)
    0    0.0043
    1    0.1400
    2    0.2195
    3    0.0233
    4    0.3214
    5    0.1053
    6    0.1862
    dtype: float64



    """

    if row[colname] == 'AMERICAN INDIAN/ALASKAN NATIVE':
        return 0.0043
    if row[colname] == 'ASIAN / PACIFIC ISLANDER':
        return 0.14
    if row[colname] == 'BLACK':
        return 0.2195
    if row[colname] == 'BLACK HISPANIC':
        return 0.0233
    if row[colname] == 'WHITE':
        return 0.3214
    if row[colname] == 'WHITE HISPANIC':
        return 0.1053
    if row[colname] == 'UNKNOWN/OTHER':
        return 0.1862


def offense_per_victim_race(dataframe_name) -> pd.DataFrame:
    """
    This function returns a dataframe that contains the information pertaining to the offense committed
    and the victims. It also takes the victim race into consideration and has a column that has normalized
    complaint numbers based on that race percentage

    :param dataframe_name:
    >>> sample = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/offense_per_victim_race_sample.csv'
    >>> sample_df = pd.read_csv(sample)
    >>> ans = offense_per_victim_race(sample_df)
    >>> ans.iloc[0]['race_percentage']
    0.14
    """
    dataframe_name.VIC_RACE = dataframe_name.VIC_RACE.fillna('UNKNOWN')  # replacing nans with 'UNKNOWN'
    dataframe_name = dataframe_name.replace({'VIC_RACE': 'UNKNOWN'}, 'UNKNOWN/OTHER')
    dataframe_name = dataframe_name.replace({'VIC_RACE': 'OTHER'}, 'UNKNOWN/OTHER')
    # Selecting only a particular set of crimes that involve harming another human
    type_of_crime = ['HARRASSMENT 2', 'BURGLARY', 'ROBBERY', 'FELONY ASSAULT', 'SEX CRIMES', 'OFFENSES INVOLVING FRAUD',
                     'RAPE', 'THEFT-FRAUD', 'MURDER & NON-NEGL. MANSLAUGHTER', 'KIDNAPPING & RELATED OFFENSES',
                     'OFFENSES RELATED TO CHILDREN', 'KIDNAPPING', 'OTHER OFFENSES RELATED TO THEF', 'PETIT LARCENY',
                     'GRAND LARCENY', 'FORGERY', 'FRAUDS', 'ASSAULT 3 & RELATED OFFENSES']
    # https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
    dataframe_name = dataframe_name[dataframe_name.OFNS_DESC.isin(type_of_crime)]
    # race_count = complaints_df_new.groupby(['OFNS_DESC','VIC_RACE']).agg({'CMPLNT_NUM': ['count']}).reset_index()
    dataframe_name = dataframe_name.groupby(["OFNS_DESC", "VIC_RACE"], as_index=False).count()
    dataframe_name = dataframe_name[['OFNS_DESC', 'VIC_RACE', 'CMPLNT_NUM']]
    dataframe_name.apply(lambda row: race_percentage(row, 'VIC_RACE'),
                         axis=1)  # https://stackoverflow.com/questions/26886653/pandas-create-new-column-based-on-values-from-other-columns-apply-a-function-o
    dataframe_name['race_percentage'] = dataframe_name.apply(lambda row: race_percentage(row, 'VIC_RACE'), axis=1)
    # race_count_new['race_population'] = race_count_new['race_percentage']*8175133
    # race_count_new['race_population'] = race_count_new['race_population'].astype('int64')
    dataframe_name['Normalized results'] = dataframe_name['CMPLNT_NUM'] / dataframe_name['race_percentage']
    dataframe_name['Normalized results'] = dataframe_name['Normalized results'].astype('int64')
    return dataframe_name


def population_density_details(filename) -> pd.core.frame.DataFrame:
    '''
    This function returns a dataframe which contains the population density for each neighbourhood.
    The area in sq.km column is added manually.

    :param filename: The population CSV file from which dataframe needs to be created
    >>> nyc_population_sample = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/New_York_City_Population_sample.csv'
    >>> ans = population_density_details(nyc_population_sample)
    >>> ans.iloc[0]['Population']
    147388
    '''
    area_population = pd.read_csv(filename)
    area_population = area_population[area_population['Year'] > 2000]
    area_population_sum = area_population.groupby(['Borough'])['Population'].sum()
    borough_pop_df = area_population_sum.to_frame().reset_index()
    borough_pop_df['Area in sq. km'] = [109.04, 183.42, 59.13, 281.09,
                                        151.18]  # https://en.wikipedia.org/wiki/Demographics_of_New_York_City
    borough_pop_df['Population Density'] = borough_pop_df['Population'] / borough_pop_df['Area in sq. km']
    borough_pop_df['Borough'] = borough_pop_df['Borough'].str.upper()
    borough_pop_df = borough_pop_df.rename(columns={"Borough": "BORO_NM"})
    borough_pop_df['Population Density'] = borough_pop_df['Population Density'].astype('int64')
    return borough_pop_df


def corr_coeff(col1, col2) -> np.float64:
    """
    :param col1: The first dataframe column you want to use for correlation calculation
    :param col2: The second dataframe column you want to use for correlation calculation
    :return: The correlation value between the two columns which is of numpy float data type
    >>> sample_csv = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/Correlation_dummy.csv'
    >>> sample_df = pd.read_csv(sample_csv)
    >>> corr_coeff(sample_df['Age'],sample_df['Height(m)'])
    0.7723621551319031
    >>> data_dummy = {'Weight':  [55,66,77,88,99,33],'Age': [22,33,44,55,66,15]}
    >>> df_dummy = pd.DataFrame (data_dummy, columns = ['Weight','Age'])
    >>> corr_coeff(df_dummy['Weight'],df_dummy['Age'])
    0.9787474369757403

    """

    plt.scatter(col1, col2)
    correlation = col1.corr(col2)
    # rp_corr = rp.corr_pair(col1,col2)
    return correlation


# Selecting only a particular set of crimes that involve harming another human
NYC_Population = my_dir + 'New_York_City_Population.csv' # Loading NYPD Arrest Data file
Pop_density_df = population_density_details(NYC_Population)
def get_crime_results(dfname) -> pd.core.frame.DataFrame:
    '''
    This function returns a dataframe which has the complaints per capita for each borough and offense

    :param dfname: NYC complaints dataframe on which operations have to be performed

    >>> sample_NYC_csv = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/NYC_get_crime.csv'
    >>> sample_NYC_dframe = pd.read_csv(sample_NYC_csv)
    >>> Pop_density_csv = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/Dummy_pop_density.csv'
    >>> Pop_density_df = pd.read_csv(Pop_density_csv)
    >>> ans = get_crime_results(sample_NYC_dframe)
    >>> ans.iloc[0]['Population']
    2504700

    '''

    type_of_crime = ['HARRASSMENT 2', 'BURGLARY', 'ROBBERY', 'FELONY ASSAULT', 'SEX CRIMES', 'OFFENSES INVOLVING FRAUD',
                     'RAPE', 'THEFT-FRAUD', 'MURDER & NON-NEGL. MANSLAUGHTER', 'KIDNAPPING & RELATED OFFENSES',
                     'OFFENSES RELATED TO CHILDREN', 'KIDNAPPING', 'OTHER OFFENSES RELATED TO THEF', 'PETIT LARCENY',
                     'GRAND LARCENY', 'FORGERY', 'FRAUDS', 'ASSAULT 3 & RELATED OFFENSES']
    # https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
    dfname = dfname[dfname.OFNS_DESC.isin(type_of_crime)]
    # complaints_df_new.OFNS_DESC.unique()
    g1 = dfname.groupby(["OFNS_DESC", "BORO_NM"], as_index=False).count()
    g1 = g1[["OFNS_DESC", "BORO_NM", "CMPLNT_NUM"]]
    # merging with population density dataframe to add necessary density columns
    Crime_result_df = pd.merge(g1, Pop_density_df, how='left', left_on='BORO_NM', right_on='BORO_NM')
    # creating the per capita values by dividing complaint numbers and population
    Crime_result_df['complaints per capita'] = Crime_result_df['CMPLNT_NUM'] / Crime_result_df['Population']
    Crime_result_df['complaints per capita'] = Crime_result_df['complaints per capita'].astype('float64')
    return Crime_result_df



#EMS_incident_response_avg = EMS_Data[['INCIDENT_RESPONSE_SECONDS_QY','BOROUGH']]
def EMS_details(dfname) -> pd.DataFrame:
    
    '''
    This function returns a dataframe containing details of the incident response time, incident datetime, borough
    There are also details pertaining to the population density , which is a result of the 2 dataframes being joined
    
    :param dfname: EMS dataframe to be passed as input
    >>> ems_sample_csv = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/EMS_incidentResponse.csv'
    >>> ems_sample_df = pd.read_csv(ems_sample_csv)
    >>> Pop_density_csv = 'https://raw.githubusercontent.com/rahulrohri/final_project_2020Sp/master/DocTest%20Dummy%20Files/Dummy_pop_density.csv'
    >>> Pop_density_df = pd.read_csv(Pop_density_csv)
    >>> ans = EMS_details(ems_sample_df)
    >>> ans.iloc[0]['Population']
    2504700
    '''
   
    EMS_incident_response_avg = dfname
    EMS_incident_response_avg = EMS_incident_response_avg.groupby(['BOROUGH','Incident_Year','Incident_Month'],as_index = False)['INCIDENT_RESPONSE_SECONDS_QY'].mean()
   
    EMS_incident_response_avg['AVG_INCIDENT_RESPONSE (Minutes)'] = EMS_incident_response_avg['INCIDENT_RESPONSE_SECONDS_QY']/60
    #Renaming the index to Staten Island
    EMS_incident_response_avg = EMS_incident_response_avg.replace({'BOROUGH': 'RICHMOND / STATEN ISLAND'}, 'STATEN ISLAND')
    result_inc_resp_df = pd.merge(Pop_density_df, EMS_incident_response_avg, how='inner', left_on='BORO_NM', right_on='BOROUGH')
    return result_inc_resp_df