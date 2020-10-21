import time
import pandas as pd
import numpy as np
import os
#from collections import Counter

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """path
    
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\nPlease choose the city:')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("which city you would like to go for? Chicago,New York City, Washington\n")
    city = city.lower()
    while city not in CITY_DATA.keys ():
        city = input("Oops, please select the city from the list:")
        city = city.lower()
    
    FilterRange={"month","day","none"}
    Filter = input('Would you like to filter the data by month, day or not at all? Type None for for no time filter:\n')
    Filter = Filter.lower()

    while Filter not in FilterRange:
        Filter = input('Please type month, day or none:')
        Filter = Filter.lower()
    if Filter =="month":
    # TO DO: get user input for month (all, january, february, ... , june)
        day=7;#7=all
        month_range=np.linspace(1,12,12,dtype=np.int) 
        #try:
        month = int(input("0-all, 1-Jan, 2-Feb, 3-March, 4-April, 5-May, 6-June,7-July, 8-Aug ,9-Sep, 10-Oct , 11-Nov, 12-Dec\n which month you would like to go for:"))
       
        while month not in month_range:
           month_range=np.linspace(0,12,13,dtype=np.int) 
           month = int(input("Oops, please type an interger from 0 to 12:"))
        
    elif Filter =="day":
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        month=0;#0=all
        day = int(input("0-Sunday,1-Monday,2-Tuesday,3-Wednesday,4-Thursday, 5-Friday, 6-Saturday, 7-all \n which day you would like to go for?"))
        day_range=np.linspace(0,7,8,dtype=np.int) 
        while day not in day_range:
            day = int(input("Oops, please type an interger from 0 to 6:"))

    elif Filter =="none":
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        month=0;#0=all
        day=7;#7=all     
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


     # load data file into a dataframe
    #df = pd.read_csv(CITY_DATA[city])
    filepath=os.path.join(os.path.dirname(__file__))
    filename=CITY_DATA[city]
    df = pd.read_csv(filepath + "/data/"+filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 0:#0=all
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 7:#7=all
        # filter by day of week to create the new dataframe
        Weekday=["Sunday","Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday"]
        df = df[df['day_of_week'] == Weekday[day]]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_counts = df['month'].value_counts()
    months = ['January', 'February', 'March', 'April', 'May', 'June',"July","August"]
    common_month_word = months[month_counts.index[0]-1]
    print("the most common month is: {}".format(common_month_word)+"  Count:{}".format(month_counts.values[0]))
    
    # TO DO: display the most common day of week
    weekday_counts = df['day_of_week'].value_counts()
    print("the most common day of week is:{}".format(weekday_counts.index[0])+"  Count:{}".format(weekday_counts.values[0]))
    # TO DO: display the most common start hour
    df["hour"] = df['Start Time'].dt.hour
    common_used_value(df,"hour") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_used_value(df,'Start Station') 
 

    # TO DO: display most commonly used end station
    common_used_value(df,'End Station') 

    # TO DO: display most frequent combination of start station and end station trip
    top = df.groupby(['Start Station', 'End Station']).size().idxmax()   
    print("The most frequent combination of start station and end station trip is {} to {}".format(top[0], top[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time    
    # TO DO: display mean travel time
    TotalTravelTime=np.sum(df["Trip Duration"])
    MeanTravelTime=np.mean(df["Trip Duration"]) 
    print("Total Travel Time:{}".format(TotalTravelTime)+"s")
    print("Mean Travel Time:{}".format(MeanTravelTime)+"s")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if "User Type" in df:   
        UserType_counts = df["User Type"].value_counts().dropna(axis = 0)
        print("Subscriber number:{}".format(UserType_counts.get("Subscriber")))
        print("Customer number:{}".format(UserType_counts.get("Customer")))

    # TO DO: Display counts of gender
    if "Gender" in df:
        
        Gender_counts = df["Gender"].value_counts().dropna(axis = 0)
        print("Male number:{}".format(Gender_counts.get("Male")))
        print("Female number:{}".format(Gender_counts.get("Female"))) 

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print ("The earlist year of birth:", min(df["Birth Year"].dropna(axis = 0)))
        print ("The recent year of birth:", max(df["Birth Year"].dropna(axis = 0)))
        common_used_value(df,"Birth Year") 
    if "User Type" or "Gender" or "Birth Year" not in df:
        print("Sorry. No Info. for User type.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def common_used_value(df,parameter):
    
    parameter_counts = df[parameter].value_counts()

    
    common_parameter_list=[]
    for a in range(0,len(parameter_counts)):
        if parameter_counts.values[a]==parameter_counts.values[0]:
            common_parameter_list.append(parameter_counts.index[a])
    print("the most common {} is: {}".format(parameter.lower(),parameter_counts.index[0])+"   Count:{}".format(parameter_counts.values[0]))
 
     
    
    
    
def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
    
    
    

