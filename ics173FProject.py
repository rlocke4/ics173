import pandas as pd
import matplotlib.pyplot as plt

#Reading in the csv data 
graphData = pd.read_csv('C:/Users/User/Downloads/COVID-19-master/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

#Grouping the data by Island 
graphData = graphData.groupby('Province_State').sum()

#Cleaning up - dropping columns that isn't needed 
graphData = graphData.drop(columns = ['UID', 'code3', 'FIPS', 'Lat', 'Long_'])

#Transpose of the dataframe
#Used the big 8 states 
graphData_transposed = graphData.T
graphData_transposed.plot(y = ['Arkansas', 'Hawaii', 'Texas', 'New York', 
                          'Virginia', 'California', 'Maine', 'North Dakota'], 
                     use_index = True, 
                     figsize = (6,6))

#Adding labels to the graph 
plt.title('COVID Cases in States of People I know', fontsize = 12)
plt.ylabel('Reported Cases', fontsize = 12)
plt.xlabel('Date which Number was Derived', fontsize = 12)
plt.xticks(rotation = 'vertical')
plt.show()
