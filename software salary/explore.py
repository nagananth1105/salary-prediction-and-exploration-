import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to categorize countries based on count threshold
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Other"
    return categorical_map

# Function to clean experience data
def clean_experience(x):
    if x == "More than 50 years":
        return 50
    if x == "Less than 1 year":
        return 0.5
    return float(x)

# Function to clean education levels
def clean_education(x):
    if "Bachelor’s degree" in x:
        return "Bachelor’s degree"
    if "Master’s degree" in x:
        return "Master’s degree"
    if "Professional degree" in x or "Other doctoral" in x:
        return "Post grad"
    return "Less than a Bachelors"

# Cache the dataset loading function for performance
@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")

    # Select relevant columns
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    
    # Handle missing values
    df = df.dropna(subset=["ConvertedCompYearly"])
    df = df.dropna()

    # Filter only full-time employees
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    # Categorize countries with a cutoff threshold of 400 responses
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)

    # Filter salary range for realistic values
    df = df[df["ConvertedComp"].between(10000, 250000)]
    df = df[df["Country"] != "Other"]

    # Apply data cleaning functions
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)

    # Rename salary column
    df = df.rename(columns={"ConvertedCompYearly": "Salary"})
    return df

df = load_data()

# Function to display explore page
def show_explore_page():
    st.title("💼 Explore Software Engineer Salaries 🌍")
    st.write("### 📊 Stack Overflow Developer Survey 2024")

    # Pie chart of respondents per country
    st.write("#### 🌎 Data Distribution by Country")
    data = df["Country"].value_counts()
    
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio for a perfect circle
    st.pyplot(fig1)

    # Bar chart of mean salary by country
    st.write("#### 💰 Mean Salary by Country")
    country_salary_data = df.groupby("Country")["Salary"].mean().sort_values()
    st.bar_chart(country_salary_data)

    # Line chart of mean salary based on experience
    st.write("#### 📈 Mean Salary by Experience Level")
    experience_salary_data = df.groupby("YearsCodePro")["Salary"].mean().sort_values()
    st.line_chart(experience_salary_data)

# Run the explore page function
show_explore_page()
