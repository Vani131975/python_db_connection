import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Replace the following with your database connection details
username = 'root'  # Your MySQL username
password = '1234'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = 'vani'  # Your MySQL database name

# Create a connection string using SQLAlchemy
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

# Create an engine
engine = create_engine(connection_string)

# Read data from MySQL into a pandas DataFrame
df_candidates = pd.read_sql('SELECT * FROM Candidates', engine)

csv_file_path = "C:/Users/CVR/Desktop/6655/jobs_data.csv"
df_jobs = pd.read_csv(csv_file_path)

df_application='C:/Users/CVR/Desktop/6655/applications_data.xlsx'

print(df_candidates['Age'].dtype)
print("memory usage ",df_candidates.memory_usage(deep=True))
df_candidates['Age'] = df_candidates['Age'].astype(np.int16)
print(f"Memory Usage: {df_candidates.memory_usage(deep=True)}")
print(df_candidates['Age'].dtype)

