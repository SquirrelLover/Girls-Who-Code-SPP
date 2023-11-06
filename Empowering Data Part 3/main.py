# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
# Step 1: If you wish to use a larger dataset that may contain data that could be potentially sensitive or difficult to interpret, do that here: 
lwd=pd.read_csv("livwell175.csv")
print(lwd.shape)
# Add Step 2 code here:
print(util.vformat_list(lwd.columns))

# 
