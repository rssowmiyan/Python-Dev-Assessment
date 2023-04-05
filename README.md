### Assessment

Input: two paths (path1, path2). Path1 has an input file named file.csv.

Objective:  To write a function

Transform(path1, path2) that does the following
Read the CSV file from path1
- Remove all duplicate rows keeping only the first row based on column1.
- Sort the whole file datewise descending order on column2.
- Copy the existing data of the maximum date from column2 and change the date to today's date and append it to the file.
- Change the date format of the entitre file to dd-mm-yyyy.
- Write the file to path2.


#### Note
- Please make sure that while opening CSV your excel software is not striping the leading zeroes in date column and changing the alignment and format.
- Please import the data from CSV properly.
- Check the raw csv file to verify any discrepancies.
- I have attached a converted excel sheet because of this problem