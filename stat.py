import pandas as pd
from datetime import datetime

#Import data, seperator ,
df = pd.read_csv('NQlongterm.csv', sep=',')

#Create 3 lists to store weekly data inn
week_data_high =[]
week_day=[]
week_data_low =[]
last_day = 0
first_day = True
waiting_for_calc = False
calc = False

#A counter to count data points per week. One week has 121 trading hours
count_week = 0

#Data that will be outputed. Dict with lists that will cointain values from each week with Day and hour of high and low
df_out={'Day_High':[],'Hour_High':[], 'Day_Low':[], 'Hour_Low':[]}

#Itterate over every row in data
for index, row in df.iterrows():
    day = df.loc[index,'Gmt time']
    date_day = day.split(' ')[0]
    dt_day = datetime.strptime(date_day, "%d.%m.%Y").date()
    date_number = int(datetime.strftime(dt_day,'%w'))

    #First day we need to add a value to last day
    if first_day:
        last_day = date_number
        first_day = False
    #If monday-friday we know a new week has started
    if date_number <=5 and not date_number ==0:
        waiting_for_calc = True

    #When we are waiting for a new week we are looking for either saturday/sunday or lastday>current date
    if waiting_for_calc:
        if date_number > 5 or (last_day>date_number and date_number<6):
            waiting_for_calc = False
            calc = True


    if calc:

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
        df_out['Hour_Low'].append(week_day[min_index].split(' ')[1])
        #Clearing lists for next week
        week_data_high.clear()
        week_data_low.clear()
        week_day.clear()
        calc=False

    last_day=  int(datetime.strftime(dt_day,'%w'))
    week_data_high.append(df.loc[index,'High'])
    week_day.append(str(df.loc[index,'Gmt time']))
    week_data_low.append(df.loc[index,'Low'])


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
df_out['Hour_Low'].append(week_day[min_index].split(' ')[1])
#Clearing lists for next week
week_data_high.clear()
week_data_low.clear()
week_day.clear()
#Output result to excel document named "out"
out=pd.DataFrame(df_out)

out.to_excel('out_test.xlsx')


