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
    
    city = input('please enter the city name : ').lower()
    print('please make sure the name of the city is valid')
    while city not in ['chicago', 'new york city', 'washington'] : 
        city = input('sorry ,  choose one of these cities : chicago - new york city - washington ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('please enter the month : ').lower()
    while month not in ['all' , 'january' ,'february' , 'march ' ,'april' , 'may' , 'june']:
        month = input('sorry , please enter a month like : all, january, february, ... , june').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input('please enter a day : ').lower()
    while day not in ['all','monday', 'tuesday', 'sunday', 'wednesday', 'friday', 'thursday' , 'saturday']:
        day = input('sorry , please enter a day like :all, monday, tuesday, ... sunday').lower()

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
    
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if it's speicfied 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 # since it's zero indexed

        df = df[df['month'] == month]

        # filter by day if it's speicfied 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0] ; 
    print('most common month : ' , common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0] ; 
    print('most common day : ' , common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0] 
    print('most common hour : ' , common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('most popular start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('most popular end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    
    combination_of_start_station_and_end_station = df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination of start station and end station trip :', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total travel time is : ' , total_time)


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean travel time is : ' , mean_time)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user types : '  , user_types)

    # TO DO: Display counts of gender
    try :
        user_gender = df['Gender'].value_counts()
        print('user gender : ' , user_gender)
    except KeyError:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    try : 
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].value_counts().idxmax())
        print("the earliest year of birth is: ",earliest_year,
              " / most recent year of birth is: ",most_recent_year,
               "/ most common year of birth is:  ",most_common_year)
        
    except KeyError:
        print('cannot be shown because it does not appear in the dataframe')

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    # this function asks the user wether he wanna view more data or not 
def display_data(df):
    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?').lower()
    start_loc = 5
    while (view_data!='no'):
        print(df.iloc[0:start_loc])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
