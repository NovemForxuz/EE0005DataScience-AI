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
Practise Data Preparation and Visualization techniques for Uni-Variate Statistics based on House Prices Competition from Kaggle.
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
Predict “SalePrice” of a house, based on the other variables given in the House Prices Competition from Kaggle.<br>
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
***
### Exercise 4: Linear Regression
Predict “SalePrice” using Linear Regression, based on numeric variables given in House Prices Competition from Kaggle.<br>
***
#### Problem 1: Predicting SalePrice using GrLivArea
>Predictor : `GrLivArea`<br>
>Response : `SalePrice`
- Plot predictor against response, note linear relationship (Jointplot, Correlation)
- Import Linear Regression model form Scikit-Learn
- Partition Dataset into Train and Test Sets
- Train the dataset
- Coefficients and plot using the standard slope-intercept form of straight line for Linear Regression model (Scatterplot)
- Predict SalePrice for Test Dataset usnig Linear Regression model and visualize predictions (Scatterplot)
- Explained Variance and Goodness of Fit of Model
#### Problem 2: Predicting SalePrice using Other Variables
>Predictor : `LotArea`,`TotalBsmtSF`,`GarageArea`<br>
>Response : `SalePrice`
- - *Same 7 points*   , and
+ Multi-Variate Linear Regression
