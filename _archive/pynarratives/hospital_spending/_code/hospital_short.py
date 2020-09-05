# Python for Healthcare
## Hospital Spending

### Import Libraries
import pandas as pd
import statsmodels.api as sm

### Import Data
df_cms = pd.read_csv('C:/Users/drewc/GitHub/python-for-healthcare/pynarratives/hospital_spending/_data/cms_mspb_stage.csv')
df_money = pd.read_csv('C:/Users/drewc/GitHub/python-for-healthcare/pynarratives/hospital_spending/_data/money_state_stage.csv')

### Select only State and Measure
df_filter = df_cms.filter(["State", "Score"])

### Group by State
df_group = df_filter.groupby(["State"], as_index = False).mean()

### Rename Score as MSPB
df_rename = df_group.rename(columns = {"Score": "MSPB"})

### Inner MSPB
df_join = pd.merge(df_rename, df_money, on = "State", how = "inner")

### Drop Values with NA
df_na = df_join.dropna()

### Rename to Regression
df_reg = df_na

### Verify MSPB
df_reg.info()
df_reg.head()

### Linear Regression Model
features = df_reg.columns.drop(["MSPB", "State"])
x = df_reg[features]
y = df_reg["MSPB"]
model = sm.OLS(y, x).fit()
result = model.summary()

### Verify Regression
print(result)