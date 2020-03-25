#### Project Severus: A Pilot Curriculum for Narrative Instruction in Data Science
### Wealth and Health: The Data Narrative in Charles Dicken's Teh Tale of Two Cities
## The Python Programming Langauge - Code Script by DrewC!

#### Section A: Import Libraries and Datasets and Prepare Data

### Step 1: Import Libraries and Data

## Import Standard Libraries
import os # Inlcuded in every script DC!
import pandas as pd # Incldued in every code script for DC!
import numpy as np # Inclduded in every code script DC!
import scipy as sp  # Incldued in every code script for DC!

## Improt Statistics Libraries
import scipy.stats as st # Basic statitsics package

## Import Graphical Output Libraries
import matplotlib.pyplot as plt

## Import Datasets
os.chdir("C:/Users/drewc/GitHub/_severus") # Set wd to project repository
df_oecd = pd.read_csv("_data/wealth_oecd_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder
df_health = pd.read_csv("_data/wealth_health_stage.csv", encoding = "ISO-8859-1") # Import dataset saved as csv in _data folder

#### Section B: Gini Coefficient and Inequality

### Step 1: Use the OECD data to rank Countries by wealth concentration

## Subset by Gini Coefficient
df_str = df_oecd[df_oecd["Subject"].str.contains("Gini")] # Susbet by column string value
df_wide = df_str.pivot_table(index = "Country", columns = "Year", values = "Value") # Convert from long to wide
df_index = df_wide.reset_index("Country") # Reset index so that country is a column
df_index.head() # Print first 5 observations

## Create list of countires
df_index["Avg"] = df_index.mean(axis = 1) # Create column for mean value in Column
df_fil = df_index.filter(["Avg", "Country"]) # Filter by average value and Country
df_gini = df_fil.sort_values(by = ["Avg"]) # Sort by column value
print(df_gini) # Print output

## Discussion
# 1. What do you notice in the list sorted by Gini coefficient?
# 2. What countires suprise you? What countries did you expect?
# 3. What would be the upside and downside of using one measure to calculate wealht concentration?

### Step 2: Make a Plot to Compare France and UK

## Subset Data for Selected Column Value
df_fr = df_gini[df_gini["Country"] == "France"] # Subset by string value
df_med = df_gini["Avg"].median() # Subset by string value

## Create bar chart with Matplotlib
plt.bar(1, df_fr["Avg"], color = "blue") # Create bar for column in data frame
plt.bar(2, df_uk["Avg"], color = "red") # Create bar for column in data frame
plt.bar(3, df_med, color = "grey") # Create bar for column
plt.ylabel(0, 0.5, 'Gini Coefficient')
plt.tick_params(bottom = False, labelbottom = False) # Remove ticks from x-axis
plt.ylim(bottom = 0.2, top = 0.4) # Set space from top and bottom of figure
plt.legend(["France", "UK", "OECD Median"]) # Set legend lables manually by order
plt.title("Inequality Measure Average 2011-2015") # Set plot title
plt.savefig("_fig/wealth_fruk_bar.jpeg") # Save plot as fighure in _fig file

## Discussion
# 1. What does this plot show?
# 2. In comparison to France and UK in the late 18th century, what may be different about their economy in the conemporary context?
# 3. What historical elements and major policy transitions may have led to this transiton?

#### Section C: Wealth Inequality and Health Outcomes

### Step 1: Combine Wealth and Health Data

## Join wealth and health datasets
df_hlth = df_health.pivot_table(index = "Country", columns = "Variable", values = "Value") # Convert from long to wide
df_wlth = df_oecd.pivot_table(index = "Country", columns = "Subject", values = "Value") # Convert from long to wide
df_merge = pd.df_merge(df_hlth, df_wlth, on = "Country", how = "inner") # Inner join datasets by column value
df_life = df_merge.filter(["Total population at birth"]) # Drop all columns except for selected
df_life = df_life.reset_index() # Reset Index

# Join life and gini datasets
df_lg = pd.merge(df_life, df_gini, on = "Country", how = "inner") # Inner join datasets by column value
df_lg["LifeExpectancy"] = df_lg["Total population at birth"] # Rename column
df_lg["Gini"] = df_lg["Avg"] # Rename column
df_final = df_lg.drop(columns = ["Total population at birth", "Avg"]) # Drop old columns
df_final.head() # Print first 5 observations

### Step 2: Create scatterplot and perfrom regression

## Create Scatterplot
plt.scatter(final.Gini, final.LifeExpectancy) # Scatter plot with X and Y values
plt.xlabel("Gini Coefficient") # Set X label
plt.ylabel("Life Expectancy at Birth (Years)") # Set y label
plt.legend() # Set legend
plt.title("Life Expectancy and Income Inequality among OECD Countries") # Set plot title
plt.savefig("_fig/wealth_ginilife_scatter.jpeg") # Save plot as fighure in _fig file

## Conduct linear regression with Scipy
x = np.array(final["Gini"]).reshape((-1, 1)) # Reshape column with numpy
y = np.array(final["LifeExpectancy"]).reshape((-1, 1)) # Reshape column with numpy
spearman = spearmanr(x, y) # Conduct Spearman's rank (data is not parametric)
print("rsq =", (spearman[0]), "p-Value =", (spearman[1])) # Print Rsq and p-value

## Discussion
# 1. What does this statistical anaylsis indicate?
# 2. How would you describe the impact of income inequality and life expectancy?
# 3. Where does this statistical relationship come from? How could one effect the other?

### Conclusions

## How data can help us understand the effects of inequality
# Gini Coefficient Data in France and UK
# While the violence of the French revolution was indiciative of the ineqaulity during the time of the novel, over time France and England have diverged in one significant measure for how much wealth is controlled by the elites. It is possible that recent developments in French and British politics (Brexit) indictae that more inequality relates to a different type of political instability.

## Life Expectancy and Wealth Inequality.
# Under old assumptions, more health led to higher wealth due to less time and resources spent on being sick. However, among OECD countries more inequality leads to lower life expenctancy. This indicates that more economic equality within a certain level of development may lead to better health outcomes.
# It is possible that there may be confoundign elements or other items that are necessary to control. These associations could be the products of more specific correlations that are unrelated when analyzed in a more precise way.

## Discussion
# 1. What other economic and health measures would you look at in order to find a more robust or precise analysis of the connection of economic inequaliy and health outcomes?
# 2. Does this analysis change your perspective on public health policy? Do you think this confirms or denies some of your original thinking on the subject of publci health impacts from economcis?
# 3. If you were to compose a novel like Dicken's Tale of Two Cities now, what two cities would you include? What crisis would you highlight? What position on the effect of inequality would you take?

#### Section D: Wealth Inequality in Gainesville, FL

### Challenge: Compare social charatceristics and mortality data for census tracts

## Import data
df_flch = pd.read_csv("_data/wealth_gnv_health_stage.csv", encoding = "ISO-8859-1")
df_acs = pd.read_csv("_data/wealth_gnv_income_stage.csv", encoding = "ISO-8859-1")

## Merge Health and Income data
df_merge = pd.merge(df_flch, df_acs, on = "Tract", how = "inner") # Join by column
df_merge["Income"] = df_merge["median_household_income"] # Rename selected columns
df_merge["Mortality"] = df_merge["Mortality Rate"] # Rename selected columns
df_gnv = df_merge.filter(["Mortality", "Income", "Tract"]) # Drop all but selected columns
df_gnv.head() # Show top 5 observations
df_gnv.info()

## Create Line Graph of individual column
plt.scatter(df_gnv.Income, df_gnv.Mortality) # Create plot of column and set color
plt.ylabel("per 100k") # Set Y label
plt.xlabel("Dollars") # Set X label
plt.title("Mortality Rate and Median Household Income by Census Tract in Alachua County") # Set title
plt.savefig("_fig/wealth_gnv_scatter.jpeg") # Save plot as fighure in _fig file

## Conduct linear regression with Spearman's Rank
x = np.array(df_gnv["Income"]).reshape((-1, 1)) # Reshape column with numpy
y = np.array(df_gnv["Mortality"]).reshape((-1, 1)) # Reshape column with numpy
spearman = st.spearmanr(x, y) # Conduct Spearman's rank (data is not parametric)
print("rsq =", (spearman[0]), "p-Value =", (spearman[1])) # Print Rsq and p-value

