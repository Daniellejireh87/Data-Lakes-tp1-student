import os
import pandas as pd
import re

def unpack_data(input_dir, output_file):
    """
    Unpacks and combines multiple CSV files from a directory into a single CSV file.

    Parameters:
    input_dir (str): Path to the directory containing the CSV files.
    output_file (str): Path to the output combined CSV file.
    """

    # Step 1: Initialize an empty list to store DataFrames
    DataFrames=[]
    

    # Step 2: Loop over files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
    
        # Step 3: Check if the file is a CSV or matches a naming pattern
        for filename in os.listdir(input_dir):
            file_path = os.path.join(input_dir, filename)
            try:
        # Attempt to read the file as a CSV regardless of its extension
               df = pd.read_csv(file_path)
               DataFrames.append(df)  # Step 5: Append the DataFrame to the list
               print(f"Successfully read file: {filename}")
            except pd.errors.EmptyDataError:
               print(f"Skipped empty file: {filename}")
            except Exception as e:
               print(f"Error reading file {filename}: {e}")
        
        

        # Step 4: Read the CSV file using pandas
       

        # Step 5: Append the DataFrame to the list
        
        

   # Step 6: Concatenate all DataFrames
    if DataFrames:  # Check if the list is not empty
        combined_df = pd.concat(DataFrames, ignore_index=True)
    # Step 7: Save the combined DataFrame to output_file
        combined_df.to_csv(output_file, index=False)
        print(f"Combined DataFrame saved to {output_file}")
    else:
        print("No valid CSV files found in the input directory. No output file was created.")
    
    pass


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Unpack and combine protein data")
    parser.add_argument("--input_dir", type=str, required=True, help="")
    parser.add_argument("--output_file", type=str, required=True, help="")
    args = parser.parse_args()

    unpack_data(args.input_dir, args.output_file)
