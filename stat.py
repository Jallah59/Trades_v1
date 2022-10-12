from turtle import pd
import pandas as pd
from datetime import datetime

#Import data, seperator ,
df = pd.read_csv('GUH1.csv', sep=',')

#Create 3 lists to store weekly data inn
week_data_high =[]
week_day=[]
week_data_low =[]

#A counter to count data points per week. One week has 121 trading hours
count_week = 0

#Data that will be outputed. Dict with lists that will cointain values from each week with Day and hour of high and low
df_out={'Day_High':[],'Hour_High':[], 'Day_Low':[], 'Hour_Low':[]}

#Itterate over every row in data
for index, row in df.iterrows():
    print(index)
    #Function for adding weekly data to lists
    if count_week <=120:
        week_data_high.append(df.loc[index,'High'])
        week_day.append(str(df.loc[index,'Gmt time']))
        week_data_low.append(df.loc[index,'Low'])
        count_week = count_week+1

        if count_week == 120: #When week is over reset count week and calculate day hour of high and low
            count_week=0
            
            #Calculate day hour of high
            max_value = max(week_data_high)
            max_index = week_data_high.index(max_value)
            date_high = week_day[max_index].split(' ')[0]
            dt_datehigh = datetime.strptime(date_high, "%d.%m.%Y").date()

            #Add day hour of high to output
            df_out['Day_High'].append(datetime.strftime(dt_datehigh,'%A'))
            df_out['Hour_High'].append(week_day[max_index].split(' ')[1])
            #Calculate day hour of low
            min_value = min(week_data_low)
            min_index = week_data_low.index(min_value)
            date_high = week_day[min_index].split(' ')[0]
            dt_datehigh = datetime.strptime(date_high, "%d.%m.%Y").date()
            
            #Add day hour of low
            df_out['Day_Low'].append(datetime.strftime(dt_datehigh,'%A'))
            df_out['Hour_Low'].append(week_day[max_index].split(' ')[1])
            #Clearing lists for next week
            week_data_high.clear()
            week_data_low.clear()
            week_day.clear()

#Output result to excel document named "out"
out=pd.DataFrame(df_out)

out.to_excel('out.xlsx')


