"""
You must use Pandas to answer the following questions:

- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
- What country has the highest percentage of people that earn >50K and what is that percentage?
- Identify the most popular occupation for those who earn >50K in India.
"""

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the
    # index labels.
    race_count = df['race'].value_counts()  # index = 'race'

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    num_bach = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((num_bach / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    num_high = len(df[df['education'] == 'Bachelors']) + len(df[df['education'] == 'Masters']) + len(
        df[df['education'] == 'Doctorate'])
    num_paid_high = len(df.loc[(df['education'] == 'Bachelors') & (df['salary'] == '>50K')] + df.loc[
        (df['education'] == 'Doctorate') & (df['salary'] == '>50K')] + df.loc[
                            (df['education'] == 'Masters') & (df['salary'] == '>50K')])
    num_paid_low = len(df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (
            df['education'] != 'Doctorate') & (df['salary'] == '>50K')])

    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = num_high
    lower_education = len(df) - num_high
    higher_education_rich_ = ((num_paid_high) / higher_education) * 100
    lower_education_rich_ = ((num_paid_low) / lower_education) * 100
    # percentage with salary >50K
    higher_education_rich = round(higher_education_rich_, 1)
    lower_education_rich = round(lower_education_rich_, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    sum_min_hours_rich = len(df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])
    num_min_workers = len(df.loc[df['hours-per-week'] == min_work_hours])

    rich_percentage = round((sum_min_hours_rich / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_paid_list = df['native-country'].unique()

    store_current_count = None

    for i in highest_paid_list:
        current_count = len(df.loc[(df['native-country'] == i) & (df['salary'] == '>50K')])
        per_current_count = current_count / len(df.loc[df['native-country'] == i])

        if store_current_count is None or per_current_count > store_current_count:
            store_current_count = per_current_count
            count_per_name = i

    highest_earning_country = count_per_name
    highest_earning_country_percentage = round(store_current_count * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')].value_counts('occupation')

    top_IN_occupation = india_df.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
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


calculate_demographic_data()
