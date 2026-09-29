import keras
import pandas as pd

# Read the data file
data = pd.read_csv('Life Expectancy Data.csv')

# Rename some columns. The original names are appallingly inconsistent with respect to capitalization and
# extra spaces and the beginning, at the end, and even in the middle of column names.
data = data.rename(columns={'Life expectancy ':'Life Expectancy',
                            'infant deaths':'Infant Deaths',
                            'percentage expenditure':'Percentage Expenditure',
                            'Measles ':'Measles',
                            ' BMI ':'BMI',
                            'under-five deaths ':'Under-five Deaths',
                            'Total expenditure':'Total Expenditure',
                            'Diphtheria ':'Diphtheria',
                            ' HIV/AIDS':'HIV/AIDS',
                            ' thinness  1-19 years':'Thinness 1-19 Years',
                            ' thinness 5-9 years':'Thinness 5-9 Years',
                            'Income composition of resources':'Income Composition of Resources'
                            })

# Keep only the columns we're interested in
data = data[['Life Expectancy', 'Alcohol', 'Hepatitis B', 'Polio', 'Diphtheria', 'GDP', 'Schooling']]

# Discard any rows containing missing values
data.dropna(how='any', inplace=True)

# Shuffle the data for good measure
data = data.sample(frac=1)  # See https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows

# Scale the outputs
data['Life Expectancy'] /= 100

# Extract the correct answers
labels = data.pop('Life Expectancy')

# TODO
# Extract training, validation, and test sets. These should comprise 60%, 20%, and 20% of the data, respectively.
# You'll be defining variables X_train, y_train, X_valid, y_valid, X_test, and y_test.

# Normalize all three sets, but based on the mean and standard deviation of the training data only to avoid snooping.

# Define the network

# Compile the network

# Train the network

# ONLY AFTER YOU HAVE MADE ALL OF YOUR CHANGES, uncomment this section to test your network
# # Test the network
# print('\nTesting trained model:')
# model.evaluate(X_test, y_test, verbose=2)
