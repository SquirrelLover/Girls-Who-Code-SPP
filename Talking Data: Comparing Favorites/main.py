#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Dr Seuss' The Lorax"

print("My favorite movie is " + favMovie)

#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])


#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)
favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre
animationBooleanMovieList = movieData["genres"].str.contains("Animation")

animationMovieData = movieData.loc[animationBooleanMovieList]

numOfMovies = animationMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Animation in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Animation.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = animationMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated " + str(int(favMovieData["audience_rating"])-min) + " points higher than the lowest rated movie.")
print()

#find max
max = animationMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(max-int(favMovieData["audience_rating"])) + " points lower than the highest rated movie.")
print()

#find mean
mean = animationMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " lower than the mean movie rating.")

#find median
median = animationMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is lower than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(animationMovieData["audience_rating"], range = (0, 100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Animation Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Animation Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, 75-80 is the most common audience rating for animation movies"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = animationMovieData, x = "audience_rating", y = "critic_rating", label = "Animation Movies")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

plt.scatter(data = favMovieData, x = "audience_rating", y = "critic_rating", label = favMovie)
plt.legend()

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between audience rating and critic rating."
)
print(
  favMovie + " follows the overall pattern."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
