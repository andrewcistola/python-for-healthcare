# Data for Everyone

## Data Stories - Hospital Spending

### Import Standard Libraries
import os # Inlcuded in every script DC!

### Set WD to Data club folder
os.chdir("C:/Users/drewc/GitHub/python-for-healthcare/hospital_spending") # Set wd to project repository

#################### Break ####################

# Section A: 2018 MSPB by State (EDA)
print("Section Start") # Print result

## Step 1: Import Libraries and Data

### Import Libraries
import pandas as pd # Incldued in every code script for DC!
import numpy as np # Incldued in every code script for DC!

import geopandas as gp # Simple mapping with pandas like syntax
import matplotlib.pyplot as plt # Comprehensive graphing package in python

### Import CMS Data
df_cms = pd.read_csv("_data/health_mspb_hospital_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Import State Shape File
gdf_state = gp.read_file("_data/health_maps_state_stage.shp")

### Verify CMS
df_cms.info() # Get class, memory, and column info: names, data types, obs.
df_cms.head() # Print first 5 observations

## Step 2: Prepare Data for Analysis

### Select only State and Measure
df_filter = df_cms.filter(["State", "Score"]) # Keep only selected columns

### Group by State
df_group = df_filter.groupby(["State"], as_index = False).mean() # Group data By Columns and Sum

### Rename Score as MSPB
df_rename = df_group.rename(columns = {"Score": "MSPB"}) # Rename column

### Drop NA values
df_na = df_rename.dropna() # Drop all rows with NA values

### Rename Dataframe
df_mspb = df_na # Rename sorted dataframe as MSPB for clarity

### Verify MSPB
df_mspb.info() # Get class, memory, and column info: names, data types, obs.
df_mspb.head() # Print first 5 observations

## Step 3: Conduct Analysis and Tests

### Summary Statistics for States
df_mspb.describe() # Get summary statistics for numerical columns in data frame

### Top 5 States for MSPB
df_mspb = df_mspb.sort_values(by = ["MSPB"], ascending = False) # Sort Columns by Value

### Verify MSPB
df_mspb.head() # Print first 5 observations

## Step 4: Create Visuals and Outputs

### Inner Join State and Geometry
gdf_join = pd.merge(gdf_state, df_mspb, on = "State", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Create Map fig
gdf_join.plot(column = "MSPB", cmap = "Blues", legend = False).set_axis_off() # Create simple choropleth map in geopandas

## Verify
plt.show() # Show created plots

# End Section
print("THE END") # Print result

#################### Break ####################

# Section B: MSPB by State and Policy (C-Q)
print("Section Start") # Print result

## Step 1: Import Data and Libraries

## Import Statistics Libraries
import scipy.stats as st # Basic statitsics package

### Import Expansion Data
df_policy = pd.read_csv("_data/health_policy_state_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Verify MSPB
df_policy.info() # Get class, memory, and column info: names, data types, obs.
df_policy.head() # Print first 5 observations

## Step 2: Prepare Data for Analysis

### Inner Join Expansion Status
df_join = pd.merge(df_mspb, df_policy, on = "State", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Drop Values with NA
df_na = df_join.dropna() # Drop all rows with NA values, 0 = rows, 1 = columns

### Rename Dataframe
df_poly = df_na # Rename sorted dataframe as poly for clarity

### Verify MSPB
df_poly.info() # Get class, memory, and column info: names, data types, obs.

## Step 3: Conduct Analysis and Tests

### T-Test to Compare Means for Medicaid Expansion
a = df_poly["MSPB"][df_poly.Medicaid == 0] # Save dependent variable column for population means while subsetting by dependent varible column
b = df_poly["MSPB"][df_poly.Medicaid == 1] # Save dependent variable column for population means while subsetting by dependent varible column
result_medicaid = st.ttest_ind(a, b) # Scipy T-test for independent samples, return will be (t-statisitic, p-value)

### T-Test to Compare Means for Nurse Practicioners
a = df_poly["MSPB"][df_poly.NP == 0] # Save dependent variable column for population means while subsetting by dependent varible column
b = df_poly["MSPB"][df_poly.NP == 1] # Save dependent variable column for population means while subsetting by dependent varible column
result_np = st.ttest_ind(a, b) # Scipy T-test for independent samples, return will be (t-statisitic, p-value)

# Verify
print("Medicaid Expansion", result_medicaid) # Print result
print("Nurse Practicioners", result_np) # Print result

## Step 4: Create Visuals and Outputs

### Inner Join State and Geometry
gdf_join = pd.merge(gdf_state, df_poly, on = "State", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Create Map fig
gdf_join.plot(column = "NP", cmap = "Blues", legend = False).set_axis_off() # Create simple choropleth map in geopandas

### Create Axes
fig, (ax1, ax2) = plt.subplots(ncols = 2)

### Plot Axis 1
gdf_join.plot(column = "NP", ax = ax1, categorical = True, legend = False).set_axis_off() 
ax1.set_title("Restricted Scope")

### Plot Axis 2
gdf_join.plot(column = "MSPB", cmap = "Blues", ax = ax2, legend = False).set_axis_off() # Create simple choropleth map in geopandas
ax2.set_title("Mean MSPB")

fig.suptitle("Nurse Practicioner Scope and MSPB in 2018")
fig.savefig("_fig/health_np_stae_map.jpeg", bbox_inches = "tight")

### Verify
plt.show() # Show created plots

#################### Break ####################

# MSPB by State and Money (Q-Q)
print("Section Start") # Print result

## Step 1: Import Libraries and Data

### Import Statistics Packages
import statsmodels.api as sm # Regression modeling in scipy

### Import Money Data
df_money = pd.read_csv("_data/health_money_state_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Verify Money
df_money.info() # Get class, memory, and column info: names, data types, obs.
df_money.head() # Print first 5 observations

## Step 2: Prepare Data for Analysis

### Inner MSPB
df_join = pd.merge(df_mspb, df_money, on = "State", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options
df_join.info() # Get class, memory, and column info: names, data types, obs.

### Drop Values with NA
df_na = df_join.dropna() # Drop all rows with NA values, 0 = rows, 1 = columns

### Drop State
df_drop = df_na.drop(columns = ["State"]) # Drop Unwanted Columns

### Rename to Regression
df_reg = df_drop

### Verify MSPB
df_reg.info() # Get class, memory, and column info: names, data types, obs.
df_reg.head() # Print first 5 observations

## Step 3: Conduct Analysis and Tests

### Linear Regression Model
features = df_reg.columns.drop(["MSPB"]) # Drop outcome variable and Geo to isolate all predictor variable names as features
x = df_reg[features] # features as x
y = df_reg["MSPB"] # Save outcome variable as y
model = sm.OLS(y, x).fit() # Run Linear Regression Model This may but most likely wont take time
result = model.summary() # Create Summary of final model

### Verify Regression
print(result) # Print result to verify

## Step 4: Create Visuals and Outputs

### Inner Join State and Geometry
gdf_join = pd.merge(gdf_state, df_na, on = "State", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Create Map fig
fig, (ax1, ax2, ax3) = plt.subplots(ncols = 3)

### Create 1st axis
gdf_join.plot(column = "MDIncome", cmap = "Greens", ax = ax1, legend = False).set_axis_off() 
ax1.set_title("Mean Physician Income")

### Create 2nd axis
gdf_join.plot(column = "ForProfit", cmap = "Reds", ax = ax2, legend = False).set_axis_off() 
ax2.set_title("Percent of Hospitals that are For Profit")

### Create 3rd axis
gdf_join.plot(column = "MSPB", cmap = "Blues", ax = ax3, legend = False).set_axis_off() # Create simple choropleth map in geopandas
ax3.set_title("Mean MSPB")

### Save to figure file
fig.suptitle("For Profit Hospitals, Physician Income, and MSPB in 2018")
fig.savefig("_fig/health_money_state_map.jpeg", bbox_inches = "tight")

### Verify
plt.show() # Show created plots

# The End
print("THE END")

#################### Break ####################

# VBP Penalty and Hospitals (Q-Q)

# Section A: 2018 MSPB by State
print("Section Start") # Print result

## Step 1: Import Libraries and Data
from scipy import stats as st

### Import Hospital Data
df_hosp = pd.read_csv("_data/health_hospital_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Import Penalty Data
df_vbp = pd.read_csv("_data/health_penalty_hospital_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

### Verify Hospital
df_hosp.info() # Get class, memory, and column info: names, data types, obs.
df_hosp.head() # Print first 5 observations

### Penalty Hospital
df_vbp.info() # Get class, memory, and column info: names, data types, obs.
df_vbp.head() # Print first 5 observations

## Step 2: Prepare Data for Analysis

### Inner Join State and Geometry
df_join = pd.merge(df_hosp, df_vbp, on = "NPI", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Select only State and Measure
df_filter = df_join.filter(["Penalty", "Ownership"]) # Keep only selected columns

### Subset Dataframe by No Penalty, group by and count
df_nopen = df_filter[(df_filter["Penalty"] == 0)].groupby(["Ownership"], as_index = False).count() # Subset data frame by value

### Subset Dataframe by Penalty of 1%, group by and count
df_pen = df_filter[(df_filter["Penalty"] == 1)].groupby(["Ownership"], as_index = False).count() # Subset data frame by value

### Move No Column to Data Frame
df_pen["NoPenalty"] = df_nopen["Penalty"]

### Calcualte Totals and Percents
df_pen["Total"] = df_pen["NoPenalty"] + df_pen["Penalty"]
df_pen["PrcntPenalty"] = df_pen["Penalty"] / df_pen["Penalty"].sum(axis = 0)
df_pen["PrcntTotal"] = df_pen["Total"] / df_pen["Total"].sum(axis = 0)
df_pen["Expected"] = df_pen["PrcntTotal"] * df_pen["Penalty"].sum(axis = 0)
df_pen["Observed"] = df_pen["Penalty"]

### Select only State and Measure
df_filter1 = df_pen.filter(["Ownership", "Expected", "Observed"]) # Keep only selected columns

### Rename to Regression
df_chsq = df_filter1

### Verify Penalty
df_chsq # Print Dataframe

## Step 3: Conduct Analysis and Tests

### Conduct ChiSq in SciPy
obs = df_chsq["Observed"]
exp = df_chsq["Expected"]
st.chisquare(obs, exp) # ChiSq with obs = observed and exp = observed

## Step 4: Create Visuals and Outputs

## Create Side by Side barplot
plt.figure()
plt.bar((1 - 0.2), df_chsq.loc[0, "Expected"], color = 'b', width = 0.4)
plt.bar((1 + 0.2), df_chsq.loc[0, "Observed"], color = 'r', width = 0.4)
plt.bar((2 - 0.2), df_chsq.loc[1, "Expected"], color = 'b', width = 0.4)
plt.bar((2 + 0.2), df_chsq.loc[1, "Observed"], color = 'r', width = 0.4)
plt.bar((3 - 0.2), df_chsq.loc[2, "Expected"], color = 'b', width = 0.4)
plt.bar((3 + 0.2), df_chsq.loc[2, "Observed"], color = 'r', width = 0.4)
plt.bar((4 - 0.2), df_chsq.loc[3, "Expected"], color = 'b', width = 0.4)
plt.bar((4 + 0.2), df_chsq.loc[3, "Observed"], color = 'r', width = 0.4)
plt.bar((5 - 0.2), df_chsq.loc[4, "Expected"], color = 'b', width = 0.4)
plt.bar((5 + 0.2), df_chsq.loc[4, "Observed"], color = 'r', width = 0.4)
plt.bar((6 - 0.2), df_chsq.loc[5, "Expected"], color = 'b', width = 0.4)
plt.bar((6 + 0.2), df_chsq.loc[5, "Observed"], color = 'r', width = 0.4)
plt.bar((7 - 0.2), df_chsq.loc[6, "Expected"], color = 'b', width = 0.4)
plt.bar((7 + 0.2), df_chsq.loc[6, "Observed"], color = 'r', width = 0.4)
plt.xticks((1, 2, 3, 4, 5, 6, 7), df_chsq["Ownership"], rotation = 90)
plt.legend(["Expected", "Observed"])
plt.title("Expected and Observed Counts of VBP Penalties over 1 Percent by Hospital Type 2019")
plt.savefig("_fig/health_penalty_hospital_bar.jpeg", bbox_inches = "tight")

## Verify
plt.show() # Show created plots

# End Section
print("THE END") # Print result

#################### Break ####################

# MSPB and Readmission Penalty (Q-C)
print("Section Start") # Print result

## Step 1: Import Libraries and Data

### Import Statistics Packages
import statsmodels.api as sm # Regression modeling in scipy

## Step 2: Prepare Data for Analysis

### Inner Join State and Geometry
df_join = pd.merge(df_hosp, df_vbp, on = "NPI", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Inner Join State and Geometry
df_join2 = pd.merge(df_join, df_cms, on = "NPI", how = "inner") # Join by column while keeping only items that exist in both, select outer or left for other options

### Subset Data Frame by ForProfit and NonProfit
df_str = df_join2[df_join2["Ownership"].str.contains("Profit")]

### Select only State and Measure
df_filter = df_str.filter(["Ownership", "Penalty", "Score"]) # Keep only selected columns

### Rename Score as MSPB
df_rename = df_filter.rename(columns = {"Score": "MSPB"}) # Rename column

### Drop NA values
df_na = df_rename.dropna() # Drop all rows with NA values

### Rename to Regression
df_log = df_na

### Verify MSPB
df_log.info() # Get class, memory, and column info: names, data types, obs.
df_log.head() # Print first 5 observations

## Step 3: Conduct Analysis and Tests

## Logisitc Regression in Scikit Learn
x = df_log["MSPB"] # features as x
y = df_log["Penalty"] # Save outcome variable as y
result = sm.Logit(y, x).fit() # Create logisitc regression model

### Verify Regression
result.summary() # Print summary of regression model
np.exp(result.params) # Print Odd's Ratio from coefficeint by taking e to the coefficients power

## Step 4: Create Visuals and Outputs

### Subset by Hospital Type
df_np = df_log[df_log["Ownership"].str.contains("NonProfit")]
df_fp = df_log[df_log["Ownership"].str.contains("ForProfit")]

### Create Scatter Plot
plt.scatter((df_np["Penalty"]-0.5), df_np["MSPB"], c = "b")
plt.scatter(df_fp["Penalty"], df_fp["MSPB"], c = "red")
plt.xticks((-0.25, 0.75), ("No Penalty over 1%", "Penalty over 1%"))
plt.legend(["Non-Profit", "For-Profit"])
plt.title("MSPB and VBP Penalties over 1 percent by Hospital Type 2019")
plt.savefig("_fig/health_penalty_hospital_scatter.jpeg", bbox_inches = "tight")

## Verify
plt.show() # Show created plots

# The End
print("THE END")


















