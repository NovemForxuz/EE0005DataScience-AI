# EE0005DataScience-AI
Archive of Introduction to Data Science &amp; Artificial Intelligence (EE0005) using `Python`.  
### Exercise 1: Data Acquisition
Practise Data Acquisition and Preparation techniques
***
#### Problem 1
>House Prices Competition : https://www.kaggle.com/c/house-prices-advanced-regression-techniques
- Import Dataset (csv)
- Check the vital statistics of the dataset (`shape` attribute)
- Check the variables and their types (`dtypes` attribute, `info` function)
- Summary Statistics of variables (`describe` function) 
#### Problem 2
>Summer Olympic 2016 medal tally : https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table
- Import Dataset (html)
- Check length and type of imported data (`len()`, `type()`)
- Storing data as Pandas DataFrame
- Extract limited set of data
***
### Exercise 2: Basic Statistics
Practise Data Preparation and Visualization techniques for Uni-Variate Statistics based on Housing Data from Kaggle.
***
#### Problem 1: Data Preparation
- Import Dataset (csv)
- List Data types of the variables
- Extract Integer(int64) only data types
- Drop non-Numeric variables
#### Problem 2: Statistical Summary (Uni-Variate, Bi-Variate)
>`SalePrice`, `LotArea`
- Summary Statistics of variable
- Visualization of Distribution of variable (Boxplot, Histogram, KDE)
- Correlation between "SalePrice" and "LotArea" (Jointplot, Heatmap)
***
### Exercise 3: Exploratory Analysis
Predict “SalePrice” of a house, based on the other variables given in the Housing Data from Kaggle.<br>
***
#### Problem 1: Numeric Variables
>`LotArea`, `GrLivArea`, `TotalBsmtSF`, `GarageArea`, `SalePrice`
- Summary Statistics of Numeric Variables <br>
- Visualization of Distribution of all variables (Boxplots, Histograms, Violinplots) <br>
- Correlation amongst Variables (Heatmaps) <br>
- Relationship of "SalePrice" against each numeric variables (Pairplots) <br>
#### Problem 2: Statistical Summary (Bi-Variate, Multi-Variate)
>`MSSubClass`, `Neighborhood`, `BldgType`, `OverallQual`
- Summary Statistics of Categorical Variables <br>
- Visualization of Distribution of all variables (Catplots) <br>
- Relationship amongst Variables (Heatmap of counts) <br>
- Relationship of "SalePrice" against each categorical variables (Boxplots)
