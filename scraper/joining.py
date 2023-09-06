import pandas as pd

if __name__ == "__main__":
    # Read data from the first CSV file (smashbook_urls_1001.csv)
    df1 = pd.read_csv("smashbook_details1.csv")

    # Read data from the second CSV file (smashbook_urls_2001.csv)
    df2 = pd.read_csv("smashbook_details_2.csv")


    # Concatenate both dataframes
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Save the merged dataframe to a new CSV file
    merged_df.to_csv("book_details_3merged.csv", index=False)
