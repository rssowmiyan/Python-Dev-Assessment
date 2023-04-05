# Importing required modules
import pandas as pd

def Transform(path1, path2):
    try:
        # Reading the file
        df = pd.read_csv(path1, dtype={'Name': 'string', 'Date':'string'})
        print("Column details : ",df.columns)
        print('No of rows in the input file: ',len(df))

        # converting date string to date obj for sorting purposes and storing it new column - We can store it Date column as well
        df['DateConverted'] = pd.to_datetime(df['Date'])

        # Deleting the duplicates
        new_df = df.drop_duplicates(subset='Name', keep="first", inplace=False).copy()
        print(new_df.dtypes)

        # sort the data by date desc
        new_df.sort_values(by='DateConverted', ascending = False, inplace = True) 

        today_str = pd.to_datetime('today').strftime('%d-%m-%Y')
        print(today_str)
        max_date =  new_df['DateConverted'][0]
        print("\nToday: ",today_str)
        print("Maximum date: ",max_date)

        for ind in new_df.index:
            if new_df['DateConverted'][ind] == max_date:
                new_df.loc[ind, 'Date'] = str(today_str)
            else:
                new_df.loc[ind, 'Date'] = new_df['DateConverted'][ind].strftime('%d-%m-%Y')

        new_df = new_df.drop(['DateConverted'], axis=1)
        new_df.to_csv(path2, index=False)
        # new_df.to_excel(path2, index=False)
        print(f"Successfully saved the output field to {path2}")

    except FileNotFoundError:
        print("Please ensure the path given is correct")

    except TypeError as e:
        print("Internal error while processing")
        print(str(e))

    except PermissionError:
        print("Please ensure that you have sufficient permission to access the files")
        


path1 = input("Enter the path of the input CSV: ").strip()
path2 = input("Enter the destination path: ").strip()
Transform(path1, path2)




