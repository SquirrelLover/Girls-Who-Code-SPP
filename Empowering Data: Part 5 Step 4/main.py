# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell135.csv")


oneCountryBooleanList = lwd["country_name"]=="Senegal"
oneCountryData = lwd.loc[oneCountryBooleanList]

# Add Step 4 code here:
plt.scatter(x = "year", y = "HD_women_size_mean", data = oneCountryData)
plt.ylim(0,14)
plt.show()
