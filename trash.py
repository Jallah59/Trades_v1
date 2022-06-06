import pandas as pd

# making data frame 
data = pd.read_csv("live_data.csv", sep=";") 
  
# iterating the columns
for col in data.columns:
    print(col)