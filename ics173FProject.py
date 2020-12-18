#Ryan W. Locke
#ICS 173: Introduction to Data Science
#12/17/2020

#Importing from library necessary functions
import pandas as pd
import matplotlib.pyplot as plt

#Read data from Excel sheet to plot
graphData = pd.read_csv('C:/Users/User/Downloads/COVID-19-master/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

#Group the data by State within Provinces
graphData = graphData.groupby('Province_State').sum()

#Take only the columns that are necessary for plotting
graphData = graphData.drop(columns = ['UID', 'code3', 'FIPS', 'Lat', 'Long_'])

#Took states that are important to my life and plotting those states.  Also transposing them.
graphData_transposed = graphData.T
graphData_transposed.plot(y = ['Arkansas', 'Hawaii', 'Texas', 'New York', 'Virginia', 'California', 'Maine', 'North Dakota'], use_index = True, figsize = (6,6))

#Add labels to graph
plt.title('COVID Cases in States of People I know', fontsize = 12)
plt.ylabel('Reported Cases', fontsize = 12)
plt.xlabel('Date which Number was Derived', fontsize = 12)
plt.xticks(rotation = 'vertical')

#Graph the plot graph
plt.show()