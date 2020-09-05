# Python for Healthcare

## 500 Cities Linear Regression

### Import Standard Libraries
import os # Inlcuded in every script DC!
import pandas as pd # Incldued in every code script for DC!
import numpy as np # Incldued in every code script for DC!

### Set working directory to project folder
os.chdir("C:/Users/drewc/GitHub/python-for-healthcare/pylessons/pymodule4") # Set wd to project repository

### Verify
print("Ready") # Print result

#################### Break ####################

# Section A: 500 Cities Analysis
print("Section A: Start") # Print result

## Step 1: Import Libraries and Data

### Import Statistics Packages
import statsmodels.api as sm # Regression modeling in scipy

### Import Visualization Packages
import matplotlib.pyplot as plt # Comprehensive graphing package in python

### Import 500 Cities Data
df_five = pd.read_csv("_data/fivecities_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

## Step 2: Prepare Data for Analysis

### Select only State and Measure
df_filter = df_five.filter(["Diabetes", "ChildAsthma"]) # Keep only selected columns

### Drop NA values
df_na = df_filter.dropna() # Drop all rows with NA values

### Rename Dataframe
df_dmca = df_na # Rename sorted dataframe as MSPB for clarity

### Verify MSPB
df_dmca.info() # Get class, memory, and column info: names, data types, obs.
df_dmca.head() # Print first 5 observations

## Step 3: Conduct Analysis and Tests

### Linear Regression Model
x = df_dmca["ChildAsthma"] # features as x
y = df_dmca["Diabetes"] # Save outcome variable as y
model = sm.OLS(y, x).fit() # Run Linear Regression Model This may but most likely wont take time
result = model.summary() # Create Summary of final model

### Create Results Text File
text_file = open("_fig/diabetes_asthma_model.txt", "w") # Open text file and name with subproject, content, and result suffix. To write or overwrite a new file, type "w". To append, type "a".
text_file.write(str(result)) # Line of text with string version of a data object
text_file.close() # Close file

### Verify Regression
print(result) # Print result to verify

## Step 4: Create Visuals and Outputs

### Create Figure
plt.figure() # Create blank figure before creating plot

### Create Scatter Plot
plt.scatter(df_dmca["ChildAsthma"], df_dmca["Diabetes"], c = "b") # Create scatter plot with (x axis, y axis, color)

### Set Labels and Titles
plt.ylabel("Estimated Prevalence of Type 2 Diabetes") # Label Y axis
plt.xlabel("Estimated Prevalence of ChildAsthma") # Label for X Axis
plt.title("CDC 500 Cities 2019 Data: Child Asthma and Diabetes") # Title above the plot

### Save to figure file
plt.savefig("_fig/diabetes_asthma_scatter.jpeg", bbox_inches = "tight") # Save figure file to _fig in directory, use tight to make a good looking image

### Verify
plt.show() # Show plot