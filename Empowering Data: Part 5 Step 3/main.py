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

# Add Step 1 code here:
largeHouseholdsBooleanList = lwd["HD_women_size_mean"].between(8,13)
largeHouseholdsData = lwd.loc[largeHouseholdsBooleanList]
print(largeHouseholdsData.shape)
# 
