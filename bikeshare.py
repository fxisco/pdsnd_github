import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
VALID_MONTHS_VALUES = {
    'all': -1,
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
}

VALID_WEEK_DAY_VALUES = [
    'all',
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        try:
            city = input('Write the name of the city to analyze (chicago, new york city, washington): ').lower()

            if city in CITY_DATA:
                print('Valid city :)')
                break
            else:
                print('Please enter a valid value')

        except:
            print('That\'s not a valid input')

    while True:
        try:
            month = input('Write the name of the month to analyze (all, january, february, ... , june): ').lower()

            if month in VALID_MONTHS_VALUES:
                print('Valid month :)')
                break
            else:
                print('Please enter a valid value')
        except:
            print('That\'s not a valid input')

    while True:
        try:
            day = input('Write the name of the week to analyze (all, monday, tuesday, ... sunday): ').lower()

            if day in VALID_WEEK_DAY_VALUES:
                print('Valid month :)')
                break
            else:
                print('Please enter a valid value')
        except:
            print('That\'s not a valid input')

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

    if month != 'all':
        df = df[df['Start Time'].dt.month == VALID_MONTHS_VALUES[month]]

    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode = df['Start Time'].dt.month.mode()[0]
    month_name = ''

    for name, value in VALID_MONTHS_VALUES.items():
        if value == month_mode:
            month_name = name

    print('The most common month: {}'.format(month_name.title()))

    # TO DO: display the most common day of week
    month_mode = df['Start Time'].dt.weekday_name.mode()[0]


    print('The most common day of week: {}'.format(month_mode.title()))

    # TO DO: display the most common start hour
    hour_mode = df['Start Time'].dt.hour.mode()[0]

    print('The most common start hour: {}'.format(hour_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('The most commonly used start station: {}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('The most commonly used end station: {}'.format(df['End Station'].mode()[0]))

    most_frequent_combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip: {} - {}'.format(most_frequent_combination.index.get_level_values('Start Station')[0], most_frequent_combination.index.get_level_values('End Station')[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('Total travel time: {}'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('Total travel time: {}'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:')
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender

    if 'Gender' in df:
        print('Counts of gender:')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest year of birth:')
        print(df['Birth Year'].sort_values().iloc[0])

        print('Most recent year of birth:')
        print(df[df['Birth Year'].notnull()].sort_values('Birth Year', ascending=False)['Birth Year'].iloc[0])

        print('Most common year of birth:')
        print(df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    page = 0
    PAGE_SIZE = 5

    while True:
        try:
            condition = input('Would you like to see raw data (yes/no): ').lower()
            starting_index = page * PAGE_SIZE

            if condition == 'yes' and starting_index < df.shape[0] :
                print('Display items ({} - {}) page({} / {})'.format(starting_index + 1,  starting_index + PAGE_SIZE, page + 1, int(df.shape[0] / PAGE_SIZE)))
                print(df[starting_index: starting_index + PAGE_SIZE + 1])

                page += 1
            else:
                break
        except:
            print('That\'s not a valid input')

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()