# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
plt.scatter(lwd["year"],lwd["EI_women_fridge_p"],color="blue")

# add a title to the plot
plt.title("Percent of Women with a Fridge")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women with a Fridge (%)")

# show the plot
plt.show()
