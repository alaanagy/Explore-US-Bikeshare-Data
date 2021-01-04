import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago' , 'new york city', 'washington']
    global city
    while (True):
        city = input('Enter the city name to analyze from the three above :')
        if city.lower() in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    days = ['saturday', 'sunday', 'monday' , 'tuesday','wednesday','thursday','friday','all']
    filter_types = ['month', 'day','both','none']
    while (True):
    
        x = input('Would you like to filter data by month, day , both or not any thing ? type none for nothing to filter:')
        x = x.lower()
        #print(x)
        if x  in filter_types or x.lower()=='none':
            month , day = 'all', 'all'
            break
    if x.lower() == 'month':    
        while(True):
            month = input('Enter the month name to analyze from the six above in months list :')
            if month.lower() in months:
                day= 'all'
                break
    if x.lower() == 'day':
        while(True):
            day = input('Enter the day name to analyze from days list :')
            if day.lower() in days:
                month='all'
                break
    if x.lower() == 'both':
        while(True):
            month = input('Enter the month name to analyze from the six above in months list :')
            if month.lower() in months :            
                while(True):
                    day = input('Enter the day name to analyze from days list :')
                    if day.lower() in days:
                        break
                break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    print(city,month,day)
    
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
    #print(city)
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    #print(df.head(2))
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)
    
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day of the Week:', common_day_of_week)
    
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nMost Common Start Hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station is:', common_start_station)

    # TO DO: display most commonly used end station
    common_End_station = df['End Station'].mode()[0]
    print('Most Common End Station is:', common_End_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] +' , '+ df['End Station']
    Common_trip = df['trip'].mode()[0]
    print('Most Common Trip is:',Common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time   
    total_teavel_time =df['Trip Duration'].sum()
    print('Total Travel Time is: ',total_teavel_time)

    # TO DO: display mean travel time
    total_average_time =df['Trip Duration'].mean()
    print('Total Average Time is: ',total_average_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df['User Type'].value_counts() 
    print('\nThe Count of User Types is:\n',count_of_user_types)

    # TO DO: Display counts of gender
    #check = ['chicago', 'new york city']
    #print(city)
    #print(type(city))
    
    #if city.lower() not in check:
    
        
    #else:
    try:
        count_of_gender = df['Gender'].value_counts() 
        print('The Count of Gender is:\n',count_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    
        common_birth_year = df['Birth Year'].mode()[0] 
        print('The Most Common Birth Year is:',common_birth_year)
    except:
        print('\nthere is no Gender or Birth Year columns in washington.csv file')
            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    check = ['yes' , 'no']
    while True:
        a = input("Would you like to view individual trip data? Enter yes or no\n.")
        a = a.lower()
        if a.lower() == 'yes':
            print(pd.read_csv(CITY_DATA[city.lower()]).sample(5))
        elif a.lower() == 'no':
            break
        elif a not in check:            
            continue                                                                  
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
     
if __name__ == "__main__":
	main()
