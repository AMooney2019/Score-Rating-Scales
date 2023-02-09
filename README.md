# Rating Scale Scoring
A Python script for calculating the confidence intervals for ratings data.

  * Script: Score_Rating_Scales.py
  * Sample Data: Fake_Ratings_Data.csv

## About
Scoring ratings data in a spreadsheet can be tedious. After each test, you may find 
yourself making many spreadsheet adjustments. Data samples are rarely the same size, 
and columns, rows, and formulas frequently need readjustment. It can take a lot of 
time and effort.

The intent of this script is to ease the scoring process by allowing you to point to a 
column of data within a .csv file and score it with minimal spreadsheet manipulation.
The script works for samples of any size, and is appropriate for samples obtained 
during moderated and unmoderated testing sessions.

## Data Preparation
The datafile should be devoid of extra columns and rows. The column names should 
exist within a single header row. The participant or sample number should exist in 
a single header column.

The data values must be numeric, either as integers (e.g. 60) or decimal values (60.0).
All cells must contain a value. Blank or text-filled cells will result in a failed script.

## Usage
You will need a Python 3.10 or greater installation in order to use this script. 

1. Convert your test data file to a .csv file, and locate which column(s) contain
the task time data you would like to score. Ideally, your column names do not contain spaces. 

2. Find the desired column and modify the name to remove spaces. For example 'Task Ratings' could be modified to 'Task_Ratings'.
    * Be sure to resave your .csv file after you make adjustments!

3. Save the data file to the same directory where your script is located.

4. Open the script. Find the line **infile = 'Fake_Ratings_Data.csv'** near the bottom of the page. 

5. Replace the 'Fake_Ratings_Data.csv' with the name of your file. Be sure to include the '' around the entire file name and the '.csv' extension!

6. Find the line **scores = df['Ratings_1']** at the bottom of the page. Copy the column name from your file and paste it into the brackets. Be sure to include '' surrounding the column name. 

7. Run the script. A set of descriptive statistics and the confidence interval for the scored values should appear in the Output panel. 

## Limitations
The script will fail if the sample cells contain blanks or text values. 


#### References
 Sauro, J., &; Lewis, J. R. (2016). In Quantifying the user experience: 
 Practical statistics for user research (pp. 19–60). essay, Morgan Kaufmann.



