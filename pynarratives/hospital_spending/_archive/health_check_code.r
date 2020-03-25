#### Healthy Neighborhoods Project: Using Ecological Data to Improve Community Health
### Neville Subproject: Using Random Forestes, Factor Analysis, and Logistic regression to Screen Variables for Imapcts on Public Health
## National Health and Nutrition Examination Survey: The R Project for Statistical Computing Script by DrewC!
# Detecting Prediabetes in those under 65

#### Section A: Prepare Code

### Step 1: Import Libraries and Import Dataset

## Import Hadley Wickham Libraries
library(tidyverse) # All of the libraries above in one line of code

## Import Data
setwd("C:/Users/drewc/GitHub/Data_Club") # Set wd to project repository
df_check = read.csv("_data/health_check_stage.csv") # Import dataset from _data folder

## Verify
dim(df_check)

model_linear <- lm(MSPB~ Case_Mix_Index + Mean_Physician_Income + Percent_For_Profit, data = df_check)
summary(model_linear)

model_linear <- lm(MSPB~ Mean_Physician_Income + Percent_For_Profit, data = df_check)
summary(model_linear)
