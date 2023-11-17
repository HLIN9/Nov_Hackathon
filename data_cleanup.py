import pandas as pd

# Read the Excel file into a DataFrame
file_path = 'archive/CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx'
sheet_name = 'FULL'  

# Columns of interest
columns_of_interest = [
    'Name (English)',
    'Region of Focus',
    'Language',
    'Entity owner (English)',
    'Parent entity (English)',
    'X (Twitter) handle',
    'X (Twitter) URL',
    'X (Twitter) Follower #',
    'Facebook page',
    'Facebook URL',
    'Facebook Follower #',
    'Instragram page',
    'Instagram URL',
    'Instagram Follower #',
    'Threads account',
    'Threads URL',
    'Threads Follower #',
    'YouTube account',
    'YouTube URL',
    'YouTube Subscriber #',
    'TikTok account',
    'TikTok URL',
    'TikTok Subscriber #'
]

try:
    # Read the specified columns from the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns_of_interest)

    # Display the first few rows 
    print(df.head())


except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
