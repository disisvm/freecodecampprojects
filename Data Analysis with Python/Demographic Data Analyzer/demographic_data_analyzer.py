import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df1 = df['race']
    race_count = df1.value_counts()

    # What is the average age of men?
    df2 = df[df['sex'] == 'Male']
    average_age_men = round(df2['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    df3 = df['education']
    total = df['education'].count()
    bach = df3[df['education'] == 'Bachelors'].count()
    percentage_bachelors = round(bach * 100 / total, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df4 = df[['education', 'salary']]
    h_total = df4[df4['education'].isin(['Bachelors', 'Masters','Doctorate'])].count()
    l_total = df4[~df4['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()
    
    higher_education = df4[
        df4['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
        & df4['salary'].isin(['>50K'])].count()
    lower_education = df4[
        ~df4['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
        & df4['salary'].isin(['>50K'])].count()

    # percentage with salary >50K
    higher_education_rich = round(
        higher_education['education'] * 100 / h_total['education'], 1)
    lower_education_rich = round(
        lower_education['education'] * 100 / l_total['education'], 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]['salary'].count()
    rich_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min() & df['salary'].isin(['>50K'])]['salary'].count()

    rich_percentage = round(rich_min_workers * 100 /num_min_workers)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df
    # Grouping rows by countries
    .groupby('native-country')['salary']
    # For each country calculate their percentage of people who earn >50K   
    .value_counts(normalize=True)[:,'>50K']
    # Sort values from the biggest
    .sort_values(ascending=False)
    # Return name of country which is first
    .index[0])
    
    highest_earning_country_percentage = (round((df
    .groupby('native-country')['salary']
    .value_counts(normalize=True)[:,'>50K']
    .sort_values(ascending=False)[0])*100,1))

    # Identify the most popular occupation for those who earn >50K in India.
    # Create a mask to choose only rows about people from India which earns >50K
    mask = (df['salary'] == '>50K') & (df['native-country'] == 'India')

    # Use mask to dataset
    top_IN_occupation = (df[mask]['occupation']
    # Count values in column 'occupation'
    .value_counts()[:1]
    # Return occupation with highest number
    .index[0])

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
