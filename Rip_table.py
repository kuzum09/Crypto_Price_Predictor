import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(
    r"C:\Users\Asus\Desktop\IIIT NR\2nd Sem\AIML Files\final project\RippleFinalCSV.csv"
)
print(df)
# Convert the DataFrame to an HTML table string
html_table = df.to_html()

# Save the HTML table string to a file
with open("Rip_Table.html", "w") as f:
    f.write(html_table)
