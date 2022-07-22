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
    city = input('please write the city name (chicago, new york city, washington)').lower()
    while city not in CITY_DATA.keys():
        print('please enter correct city')
        city = input('please choose the city (chicago, new york city, washington)').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month_name=['january', 'february', 'march', 'april' ,'may', 'june', 'all']
    while True:
        month = input('please write the month name (january, february, ... , june, all)').lower()
        if month in month_name:
            break
        else:
            print('please enter valid month name')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name=['saturday', 'sunday', 'monday', 'tuesday' ,'wednesday', 'thursday','friday','all']
    while True:
        day = input('please enter the day name ( monday, tuesday, ... sunday,all)').lower()
        if day in day_name:
            break
        else:
            print('please enter valid day name')
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
    df['start hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month_name=['january', 'february', 'march', 'april' ,'may', 'june']
        month = month_name.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('the most common month is :', common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('the most common day of week is :', common_day)
    # TO DO: display the most common start hour
    common_hour = df['start hour'].mode()[0]
    print('the most common hour is :', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('the most common start station : ',common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('the most common end station : ', common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + df['End Station']
    print('the most frequent combination is :' + df['route'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('total travel time is :',travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('total mean travel time is :',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users = df['User Type'].value_counts()
    print('number of users are : ',count_users)
    # TO DO: Display counts of gender
    #gender = df['Gender'].value_counts()
    if 'gender' in df :
        print('\n count of gender is :\n',gender())
    # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        print('the common year of birth is :',int(birth_year.mode()[0]))
        print('the most recent year of birth is :',int(birth_year.max()))
        print('the earliest year of birth is :',int(birth_year.min()))
    else:
        print('sorry there is no birth year')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print('your raw data is available')
    i = 0
    input_message = input('did you want to display 5 rows of data ? please type Yes or No \n').lower()
    pd.set_option('display.max_columns',None) # display all columns if None
    if input_message not in ['yes','no']:
        print("invalid choice please type 'yes' or 'no'")
        input_message = input('did you want to display 5 rows of data ? please type Yes or No \n').lower()
    elif input_message != 'yes':
        print('thank you')
    else:
        while i+5 < df.shape[0]:
            print(df[i:i+5]) # display only next five rows
            i+=5
            input_message = input('did you want to display next 5 rows of data ? please type Yes or No \n').lower()
            if input_message == 'no':
                print('thank you')
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
