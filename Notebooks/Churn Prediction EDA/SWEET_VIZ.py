import os
import pandas as pd
import datetime as dt
import sweetviz as sv

# Set the directory path where the CSV files are located
dir_path = './Data'
df_cif = pd.read_csv('./Data/CUST_METRICS_DEMOGRAPHIC.csv')
df_cif['CIF_OPEN_DATE'] = pd.to_datetime(df_cif['CIF_OPEN_DATE'])
df_2022 = df_cif[df_cif['CIF_OPEN_DATE'].dt.year == 2022]
cif = df_2022['CLIENT_NO'].tolist()
del df_cif, df_2022
# Loop through all files in the directory
file_names =  [file_name for file_name in os.listdir(dir_path)  if file_name.endswith('.csv')]
for file in file_names:
    print(file)
    name = file.split('.')[0]
    file_path = os.path.join(dir_path, file)
    df = pd.read_csv(file_path, index_col=[0])
    df = df[df['CLIENT_NO'].isin(cif)]
    df['SYM_RUN_DATE'].unique()
    df_filter = df[df['SYM_RUN_DATE'] == '2023-09-30']
    my_report = sv.analyze(df_filter)
    my_report.show_html(f"{name}_sweetviz.html")  # Default arguments will generate to "SWEETVIZ_REPORT.html"