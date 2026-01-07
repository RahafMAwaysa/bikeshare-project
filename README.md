# Bikeshare Project 🚲

## Introduction
The Bikeshare Project is a Python-based data analysis program that explores bikeshare usage data in the United States.  
The project allows users to interactively analyze bikeshare data for three major cities: **Chicago**, **New York City**, and **Washington**.

This project was completed as part of the **Udacity Git & GitHub course**, with a strong focus on:
- Writing clean and readable Python code
- Proper documentation using README.md
- Using Git for version control
- Working with branches and commits

---

## Project Motivation
Bike-sharing systems generate large amounts of data that can be analyzed to understand user behavior and travel patterns.  
This project helps answer important questions such as:
- When do people use bikeshare the most?
- Which stations are the most popular?
- What is the average duration of a trip?
- What types of users use bikeshare services?

The project is designed to strengthen skills in **data analysis, problem solving, and software documentation**.

---

## Project Description
The program uses Python to load bikeshare data from CSV files and allows the user to filter the data based on:
- City
- Month
- Day of the week

After filtering, the program calculates and displays meaningful statistics related to bikeshare usage.

The program runs entirely in the terminal and interacts with the user through text input.

---

## Dataset
The analysis is based on bikeshare data from the following cities:
- Chicago
- New York City
- Washington

Each dataset contains information such as:
- Start time
- End time
- Trip duration
- Start and end stations
- User type
- Gender and birth year (not available for all cities)

> **Note:** The CSV data files are not included in this repository and are ignored using `.gitignore`.

---

## Files in the Repository
| File Name | Description |
|----------|------------|
| `bikeshare.py` | Main Python script that performs data loading and analysis |
| `README.md` | Project documentation |
| `.gitignore` | Prevents CSV data files from being tracked by Git |

---

## How the Program Works
1. The program asks the user to select a city.
2. The user chooses a time filter:
   - By month
   - By day
   - No filter
3. The program loads the appropriate dataset.
4. Data is filtered based on the user’s selection.
5. The program calculates and displays statistics in the following categories:
   - Time statistics
   - Station statistics
   - Trip duration statistics
   - User statistics
6. The user can choose to restart the program or exit.

---

## Statistics Calculated

### Time Statistics
- Most common month
- Most common day of the week
- Most common start hour

### Station Statistics
- Most commonly used start station
- Most commonly used end station
- Most frequent trip combination

### Trip Duration Statistics
- Total travel time
- Average travel time

### User Statistics
- Counts of user types
- Counts of gender (if available)
- Earliest, most recent, and most common birth years (if available)

---

## How to Run the Program

### Prerequisites
- Python 3
- Pandas
- NumPy

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/RahafMAwaysa/bikeshare-project.git
   ```
2. Navigate to the project folder:
    ```bash
     cd bikeshare-project
    ```
3. Run the program:
    ```bash
    python bikeshare.py
    ```

