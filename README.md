# Video-game-Sales-EDA
Applying a EDA on a data set of video game sales and predicting the sales of the games depending on specific features

# EDA

After cleaning up the data, let's look at some trends.

## Publishers with most Releases from 1980 - 2016
![alt text](https://github.com/jbofill10/Video-game-Sales-EDA/blob/master/Charts/All_Time_Platform_Releases.png)

Having played on all playstation consoles up to date, I found it interesting that PS2 had the most sales of all the other consoles in the PlayStation and Xbox brand.

## Global Sales of Games Over the Years
![alt text](https://github.com/jbofill10/Video-game-Sales-EDA/blob/master/Charts/Yearly_Global_Sales.png)

Interesting that there was a large spike in 2010-2012 and then it just falls off. I would've expected it to increase more due to many games being on the "online store" and people don't have to go out to the local GameStop to buy a game. 

## Genres with Most Revenue Globally
![alt text](https://github.com/jbofill10/Video-game-Sales-EDA/blob/master/Charts/GlobalSales_ofGenres.png)
Interesting to see that Action games are the most successful.

## Top 5 Genres and their Revenue Respective to their Country
![alt text](https://github.com/jbofill10/Video-game-Sales-EDA/blob/master/Charts/CountryRespectiveSales.png)
What's interesting here is that Action is never any countries favorite genre, except for the spike in EU from 1990-1995 -- yet it has the most global sales out of all the genres.

## Correlation between Publisher and Global Sales
I split the top 10 publishers with the most global sales into two graphs and see if there were any trends among them.
![alt text](https://github.com/jbofill10/Video-game-Sales-EDA/blob/master/Charts/GlobalSalesPublishers.png)
Pretty interesting to see how close all the publishers' global sales were all close to each other, but near 2015 and 2016, you can see Sony and Ubisoft beginning to take off, while all the others fall.

# Modeling

## Using Linear Regression to predict Global Sales based on Features (Not forecasting)
So I took the features "Platform", "Genre", and "Publisher" and encoded them into numbers so the machine could interpret them.

I dropped the rank, year, and name column as I believed year would cause overfitting and the rest wouldn't contribute at all to accuracy.

The target label is: Global Sales  

My next step was to implement cross validation to get a more realistic result of how my model would perform.
Here are the results:  
![alt text](https://github.com/jbofill10/Video-game-Sales-EDA/blob/master/model_results/LinearRegression.png)

So obviously, the scores worsened, but not by a large margin.  
The target's unit is in millions, so on average, we are getting values incorrect by ~$700,000. This isn't terrible. Ideally, I would like the margin to be smaller, but considering the fact that it can still provide some idea of how good a game will do depending on the Platform, Genre, and Publisher, I think this is a good start.






