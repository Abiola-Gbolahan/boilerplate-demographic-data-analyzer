import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    data = pd.read_csv("adult.data.csv")

        # 1. How many people of each race are represented in this dataset?
    race_count = data['race'].value_counts()
    
    # 2. What is the average age of men?
    average_age_men = data[data['sex'] == 'Male']['age'].mean()
    
    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (data['education'] == 'Bachelors').mean() * 100
    
    # 4. Percentage of people with advanced education (Bachelors, Masters, Doctorate) who earn >50K
    advanced_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    advanced_education_high_income = data[advanced_education & (data['salary'] == '>50K')]
    percentage_advanced_high_income = (len(advanced_education_high_income) / len(data[advanced_education])) * 100
    
    # 5. Percentage of people without advanced education who earn >50K
    non_advanced_education = ~advanced_education
    non_advanced_education_high_income = data[non_advanced_education & (data['salary'] == '>50K')]
    percentage_non_advanced_high_income = (len(non_advanced_education_high_income) / len(data[non_advanced_education])) * 100
    
    # 6. What is the minimum number of hours a person works per week?
    min_hours_per_week = data['hours-per-week'].min()

    # 7. Percentage of people working the minimum hours per week who earn >50K
    min_hours_workers = data[data['hours-per-week'] == min_hours_per_week]
    percentage_min_hours_high_income = (min_hours_workers['salary'] == '>50K').mean() * 100
    
    # 8. Country with the highest percentage of people earning >50K
    country_earning_over_50k = data[data['salary'] == '>50K']['native-country'].value_counts()
    country_counts = data['native-country'].value_counts()
    country_percentage = (country_earning_over_50k / country_counts) * 100
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = country_percentage.max()

    # 9. Most popular occupation for those who earn >50K in India
    india_high_income = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
    top_occupation_india = india_high_income['occupation'].value_counts().idxmax()



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
