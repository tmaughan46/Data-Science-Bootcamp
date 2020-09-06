# Data-Science-Bootcamp Texas A&M Kingsville
## This repository contains the projects I completed as part of the Data Science certification program offered through Texas A&M Kingsville.
## A total of five projects were completed during this course, and requirements for each project is listed below.  


# Project #1 Exploratory Data Analysis: Work Place Fatality Data Set
Your report will be evaluated on how well it meets the following criteria:
 
Summarizes descriptive statistics about the data, including at least one descriptive visualization, such as a box-and-whisker plot or histogram displaying the distribution of a variable
Contains an interactive element that lets a user cut into the data, e.g., an Excel pivot table with slicers
Generates interesting questions about the data and explores those questions with two or more visualizations that highlight an insight about the data, possibly applying transformations to the data. For example, a scatter or line plot showing the relationship between two variables.
Effectively uses of analytical storytelling to convey insight(s), including good practices for visualizations

As part of these criteria, your report should answer at least the following questions:
 
Which program, state or federal, has the highest rate of fatalities?
Which state with a state program has the highest number of injuries/illnesses?
What is the relationship, if any, between “Average of Years to Inspect Each Workplace Once” and “Rate of Fatalities”?

# Project #2 Data Querying And Cleaning: Lahman's Baseball Data Set
Connects to an SQL database file and queries for all players who have played at least 50 games and are still active.  Use the “finalGame” field from the “People” table to determine if a player is active. Retrieve weight, throws, bats, throws, all birth-related and all name-related columns from the “People” table and retrieve all columns from the “Batting” table.
Converts this data into either an R data frame or a pandas data frame.
Adds a calculated column with the player’s age and a calculated column with each player’s first and last name concatenated.
Once the calculated columns are added, drops the other columns related to birth date and name.
Deletes any rows with missing values
Answers the following questions:
 
Which active player had the most runs batted in (“RBI” from the Batting table) from 2015-2018?
How many double plays did Albert Pujols ground into (“GIDP” from Batting table) in 2016?
 
Creates the following plots:
 
A histogram of triples (3B) per year.
Create a scatter plot relating triples (3B) and steals (SB).
 
Comes up at least three additional questions about the data and answers them. At least one should be a question about the relationship between two variables, e.g., triples and steals, as above.

# Project #3 Data Science Research Methods: Bostson Housing Price Data Set 
For this project you should produce a Python or R notebook. There are two sets of specific questions as well as an open-ended experimental design. Your project will be evaluated on how well it answers the questions and on the quality of the experimental design:
 

1.  Choose a variable other than CHAS and MEDV (the target, median home price).
  1. Compute the mean and standard deviation of the variable.
  2. Plot a histogram of the variable.
  3. What is the sample correlation between your chosen variable and median home price?
  4. Perform a regression, predicting MEDV from your chosen variable.
 
2. You have a theory that tracts that border the Charles River (CHAS) will have higher median price (MEDV or target) than those that do not.
  1.What is the null hypothesis?
  2. Calculate the p-value. Use the sample mean of the target as an estimate of the population mean.
  3. What is the 90% confidence interval for the target (price) of tracts that border the Charles River?
  4. Assume an effect size (Cohen’s d) of 0.6. If you want 80% power, what group size is necessary?
 
3. Imagine you are the city planner of Boston and can add various new features to each census tract, such as a park. Be creative with your new “features” – we use the term loosely. You can assume that none of the tracts contained your features previously. Design an experiment to explore the effects of these features on the media house price in census tracts. You should include an explanation of the experimental design as well as a plan of analysis, which should include a discussion of group size and power. Be sure to apply the knowledge you learned in the Data Science Research Methods courses.

# Project #4 Machine Learning: Bank Marketing Data Set (Portuguese banking institution) 
You need to produce an R or Python notebook that builds a classifier from the given dataset. Please provide explanations of each step of the process, from data exploration to the final model evaluation.
 

Data Cleaning and Preparation: In this case the data is relatively clean, but you may still need some preprocessing, such as scaling.
Model Selection: Train at least two models on the dataset. Clearly indicate which metrics you used and the performance of each model. Be sure to address any imbalance in the data, as well as using an appropriate train/test data split.
Performance Optimization: Use regularization, hyperparameter tuning, or other techniques to further optimize your chosen model and/or help select the best model.
 
At the end of your notebook, provide a brief summary (one paragraph) of your model – what it is, what preprocessing and optimization you did, and the final accuracy (or another appropriate metric).

# Project #5 Course Capstone: Data Set choice(Census Income,California Housing, Thyroid Disease, Insurance Company)
You need to produce an R or Python notebook that covers the full scope of the data science courses, from exploring data to optimizing machine learning model performance. Throughout each stage of the process, thoroughly explain your thought process. For example, perhaps you chose to ignore a certain variable because it is too related to another feature, or because regularization indicated it was not useful.
 

Exploratory Data Analysis: Summarize variables, visualize distributions and relationships. Generate a few interesting questions about the data and explore them with some visualizations.
Research Methods: Calculate the sample correlation between at least one pair of variables. Come up with a hypothesis and calculate the p-value.
Data Cleaning and Preparation: Apply any appropriate preprocessing steps, such as removing duplicates, missing values, outliers, and scaling data as appropriate (note that which model(s) is/are chosen may determine whether scaling is necessary).
Feature Engineering: Create new features or transform existing ones to improve performance. Even if you decide not to use these features (e.g., they don’t affect performance or make it worse), keep the code and an explanation of what you tried in your notebook.
Model Selection: Try various models (at least 3), showing your evaluation process. Clearly indicate which metrics you used and the performance of each model. Be sure to address any imbalance in the data, as well as using an appropriate train/test data split.
Performance Optimization: Use regularization, hyperparameter tuning, or other techniques to further optimize your chosen model and/or help select the best model.
 
At the end of your notebook, provide a brief summary (one paragraph) of your model – what it is, what preprocessing, feature engineering, and optimization you did, and the final accuracy (or another appropriate metric). Finally, briefly provide three ideas that could improve the model, which may include collecting additional variables.




