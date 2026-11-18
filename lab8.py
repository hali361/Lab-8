import pandas as pd


def task1_load_explore():
    print("Task 1: Load and Explore Dataset")

    df = pd.read_csv('labor.csv')

    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    print("\nColumn names:")
    print(df.columns)

    print("\nDataFrame dimensions:")
    print(df.shape)

    print("\nColumn data types:")
    print(df.dtypes)

    wage_series = df["wage-increase-first-year"]

    print("\nWage Increase First Year Series:")
    print(wage_series)

    return df

def task2_access_data(df):
    print("\nTask 2: Access Data")

    #Select the first year wage increase column as a Series
    wage_series = df["wage-increase-first-year"]
    print("\nFirst year wage increase Series:")
    print(wage_series)

    #Retrieve the first value using iloc and loc
    print("\nFirst value using iloc:")
    print(wage_series.iloc[0])

    print("\nFirst value using loc:")
    print(wage_series.loc[0])

    #Display the first five rows using iloc
    print("\nFirst five rows using iloc:")
    print(df.iloc[:5])

    #Select first year and second year wage increase columns
    print("\nFirst year and second year wage increases:")
    print(df[["wage-increase-first-year", "wage-increase-second-year"]])

    #Retrieve a specific value using loc
    print("\nSpecific value using loc:")
    print(df.loc[2, "wage-increase-first-year"])

    #Select multiple rows and columns using loc
    print("\nMultiple rows and columns using loc:")
    print(df.loc[0:4, ["wage-increase-first-year", "wage-increase-second-year"]])

    #Select multiple rows and columns using iloc
    print("\nMultiple rows and columns using iloc:")
    print(df.iloc[0:5, 1:3])

def task3_filter_data(df):
    print("\nTask 3: Filter and analyze data")

    #Select all disputes with a good outcome
    good = df[df["class"] == "good"]
    print("\nDisputes with good outcomes:")
    print(good)

    #Select all disputes with a bad outcome
    bad = df[df["class"] == "bad"]
    print("\nDisputes with bad outcomes:")
    print(bad)

    #Select disputes with first year wage increase greater than 2.5
    wage = df[df["wage-increase-first-year"] > 2.5]
    print("\nFirst year wage increases greater than 2.5:")
    print(wage)

    #Select disputes with more than 10 statutory holidays
    holidays = df[df["statutory-holidays"] > 10]
    print("\nStatutory holidays greater than 10:")
    print(holidays)

    #Select disputes satisfying both conditions
    both = df[(df["wage-increase-first-year"] > 2.5) &
              (df["statutory-holidays"] > 10)]
    print("\nDisputes satisfying both conditions:")
    print(both)

    #Calculate the average first year wage increase
    average = df["wage-increase-first-year"].mean()
    print("\nAverage first year wage increase:")
    print(average)

    #Calculate the maximum first year wage increase
    maximum = df["wage-increase-first-year"].max()
    print("\nMaximum first year wage increase:")
    print(maximum)

if __name__ == "__main__":
    df = task1_load_explore()
    task2_access_data(df)
    task3_filter_data(df)