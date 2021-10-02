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
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Get user input for any selected city
    while True:
        city = input("Please enter the city name. Choose a city from Chicago, New York or Washington \n").lower()
        city_name_list = ['chicago','new york','washington']
        if city in city_name_list:
            print("The city name you have chosen is " + city + "\n")
            break;
        else:
            print("Try again. Please enter a valid name. \n")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    #get user input for a valid month
    while True:
        month = input("Please enter the month. Enter a month from all, january, february, march, april, may or june \n").lower()
        month_name_list = ['all','january','february','march','april','may','june']
        if month in month_name_list:
            print("The month you have chosen is " + month + "\n")
            break;
        else:
            print("Try again. Please enter a valid month from the given options. \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #get user input for a valid day 
    while True:
        day = input("Please enter the weekday. Enter a weekday from all, monday, tuesday, wednesday, thrusday, friday, saturday or sunday \n").lower()
        weekday = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if day in weekday:
            print("The weekday you have chosen is " + day + "\n")
            break;
        else:
            print("Try again. Please enter a valid weekday from the given options. \n")

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
    #filtering data
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
 

    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
   
    most_common_month = df['month'].mode()[0]
    print("Most common month is:", most_common_month)
    print("\n")

    # TO DO: display the most common day of week
    
    most_common_weekday = df['day_of_week'].mode()[0]
    print("Most common Weekday is:", most_common_weekday)
    print("\n")

    # TO DO: display the most common start hour
    
    most_common_hour = df['hour'].mode()[0]
    print("Most common hour is:", most_common_hour)
    print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is: ", most_common_start_station)
    print("\n")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station is:", most_common_end_station)
    print("\n")

    # TO DO: display most frequent combination of start station and end station trip
    filter_station = df.groupby(['Start Station','End Station']).size().sort_values(ascending = False).head(1)
    print("Most frequent combination of start station and end station is:\n ", filter_station)
    print("\n")
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_total = df['Trip Duration'].sum()
    print("Total travel time is: ", travel_time_total)
    print("\n")


    # TO DO: display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print("Mean travel time: ", travel_time_mean)
    print("\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("Number of user types are:\n ", user_types_count)
    print("\n")
    # TO DO: Display counts of gender
    if city != 'washington':
        gender_counts = df['Gender'].value_counts()
        print("Number of people with different genders:\n ", gender_counts)
        print("\n")

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        print("Earliest year of birth is: ", earliest_year_of_birth)
        print("\n")

        most_recent_year_of_birth = int(df['Birth Year'].max())
        print("Most recent year of birth is:",most_recent_year_of_birth)
        print("\n")

        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("Most common year of birth is: ",most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_check(df):
    # Get to know if user wants to input raw data
    
    while (True):
            view_raw_data = input("Would you like to view 5 rows of data? Enter yes or no \n")
            start_loc = 0
            if view_raw_data == "yes":
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                view_display = input("Do you wish to continue?, You can check more 5 more five rows of raw data. Enter yes, to view further 5 rows or else choose no \n").lower()
                if view_display == "yes":
                    continue
                elif view_display == "no":
                    print("You've chosen not to view the further 5 rows of data \n ")
                    break
                else:
                    print("Please enter yes or no. Any other input is invalid. \n ")
                    continue
            elif view_raw_data == "no":
                print("You've chosen not to view the first 5 rows of raw data \n")
                break
            else:
                print("Try again. Please input as yes or no, any other input is not valid.")
                continue
                break
                
                
                      
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data_check(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
