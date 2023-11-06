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

# Part 7 Step 2
print("Senegal is classified as a heavily indebted poor country. Overall, the country experiences a Sahelian climate of hot temperatures and high aridity. Even though Senegal is not a leading contributor to greenhouse gas emissions, it is one of the countries most vulnerable to climate change. Average temperature is expected to increase 1.5 to 4 degrees celsius by 2050, and average rainfall is projected to decrease. \n")
input("Press enter to continue. \n")

print("The traditional social status of women in Senegal is shaped by local custom and religion. Hence, many of them are responsible for household tasks such as cooking, cleaning, and childcare. On the bright side, women in rural Senegal are becoming increasingly involved in managing their community, and some women in urban Senegal, despite social expectations, have begun working in the labor market. \n")
input("Press enter to continue. \n")

print("Although the constitution of Senegal prohibits discrimination by sex, women in Senegal still face prejudice. Traditional religious beliefs prohibit women in many regions from owning tracts of land, and society recognizes men as the heads of households. As polygenous marriages are common, households comprise of a man and his multiple wives and children. \n")

# Add Step 1 code here:
lwd=pd.read_csv("livwell135.csv")
oneCountryBooleanList = (lwd["country_name"]=="Senegal") & lwd["year"].between(0,10000)
oneCountryData = lwd.loc[oneCountryBooleanList]
oneCountryBooleanList2 = (lwd["country_name"]=="Indonesia") & lwd["year"].between(0,10000)
oneCountryData2 = lwd.loc[oneCountryBooleanList2]

plt.scatter(x = "HD_women_size_mean", y = "HH_time_water_mean", data = oneCountryData, label='Senegal')
plt.scatter(x = "HD_women_size_mean", y = "HH_time_water_mean", data = oneCountryData2, label='Indonesia')
plt.legend(loc='upper left')
plt.xlim(0, 15)
plt.xlabel("Household Size")
plt.ylabel("Time to get drinking water (minutes)")
plt.show()
#