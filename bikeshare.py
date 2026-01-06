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
    print('Hello! Let\'s explore some US bike share data for 2017!')
    
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Get user input for city (with validation and case-insensitivity)
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington? ').strip().lower()
        if city in cities:
            break
        else:
            print('Invalid input. Please enter one of the following cities: Chicago, New York City, Washington.')

    # Get user input for filter type (month, day, or no)
    while True:
        filter_by = input('Would you like to filter the data by month, day, or not at all? (month/day/no) ').strip().lower()
        if filter_by in ['month', 'day', 'no']:
            break
        else:
            print('Invalid input. Please enter: month, day, or no.')
    
    month = 'all'
    if filter_by == 'month':
        # Get user input for month
        while True:
            month = input('Which month - January, February, March, April, May, or June? ').strip().lower()
            if month in months:
                break
            else:
                print('Invalid input. Please enter one of the months from January to June.')
    
    day = 'all'
    if filter_by == 'day':
        # Get user input for day
        while True:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').strip().lower()
            if day in days:
                break
            else:
                print('Invalid input. Please enter one of the days of the week.')

    print('-'*60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city: name of the city to analyze
        (str) month: name of the month to filter by, or "all"
        (str) day: name of the day of week to filter by, or "all"
    Returns:
        df: Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month, day of week, and hour from 'Start Time'
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour
    
    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\n### Popular Travel Times ###')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0].capitalize()
    print(f"* Most Common Month: **{most_common_month}**")

    # Display the most common day of week
    most_common_day = df['day_of_week'].mode()[0].capitalize()
    print(f"* Most Common Day of Week: **{most_common_day}**")

    # Display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print(f"* Most Common Start Hour: **{most_common_hour}:00**")

    print(f"\n[Operation took {time.time() - start_time:.3f} seconds]")
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\n### Popular Stations and Trip ###')
    start_time = time.time()

    # Display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"* Most Common Start Station: **{most_common_start_station}**")

    # Display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"* Most Common End Station: **{most_common_end_station}**")

    # Create a combined column for the trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    
    # Display most frequent combination of start and end station
    most_common_trip = df['Trip'].mode()[0]
    print(f"* Most Common Trip: **{most_common_trip}**")

    print(f"\n[Operation took {time.time() - start_time:.3f} seconds]")
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\n### Trip Duration Statistics ###')
    start_time = time.time()

    # Display total travel time
    total_duration_seconds = df['Trip Duration'].sum()
    
    # Convert total duration to Days, Hours, Minutes, Seconds for readability
    minutes, seconds = divmod(total_duration_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    print(f"* Total Travel Time: **{days} days, {hours} hours, {minutes} minutes, and {int(seconds)} seconds**")

    # Display mean travel time
    average_duration_seconds = df['Trip Duration'].mean()
    
    # Convert average duration to Minutes and Seconds
    avg_minutes, avg_seconds = divmod(average_duration_seconds, 60)
    
    print(f"* Average Travel Time: **{int(avg_minutes)} minutes and {int(avg_seconds)} seconds**")

    print(f"\n[Operation took {time.time() - start_time:.3f} seconds]")
    print('-'*60)


def user_stats(df, city):
    """Displays statistics on bike share users."""
    
    print('\n### User Statistics ###')
    start_time = time.time()

    # Display counts of user types
    print("\n* User Type Counts:")
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts.to_string())

    # Display counts of gender and birth year stats for non-Washington cities
    if city != 'washington':
        # Display counts of gender
        print("\n* Gender Counts:")
        gender_counts = df['Gender'].value_counts().dropna()
        print(gender_counts.to_string())

        # Display earliest, most recent, and most common year of birth
        print("\n* Birth Year Statistics:")
        
        # Remove NaN values before calculating min/max/mode
        birth_year_data = df['Birth Year'].dropna()

        if not birth_year_data.empty:
            earliest_year = int(birth_year_data.min())
            most_recent_year = int(birth_year_data.max())
            most_common_year = int(birth_year_data.mode()[0])

            print(f"  - Earliest Year of Birth: **{earliest_year}**")
            print(f"  - Most Recent Year of Birth: **{most_recent_year}**")
            