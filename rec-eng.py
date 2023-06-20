import pandas as pd
import csv
import requests

api_key="0c4f22fd5b4f44fd8c56d18f277a1a8c"

def news():
    try:
        main_url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key
        news=requests.get(main_url).json()
        article=news["articles"]
        news_url=[]
        news_article=[]
        news_csv=[]
        for arti in article:
            news_article.append(arti['title'])
            news_url.append(arti['url'])
        for i in range(len(news_article)):
            #print(i+1,news_article[i], "\n", news_url[i], "\n\n")
            news_csv.append([news_article[i], news_url[i]])
        with open("rec.csv", 'w') as csvfile:  
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(['Latest News Articles', 'Links']) 
            for i in news_csv:
                csvwriter.writerow(i) 
    except:
        ...

    
news()

def writer():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(
        r"rec.csv"
    )
    print(df)
    # Convert the DataFrame to an HTML table string
    html_table = df.to_html()

    # Save the HTML table string to a file
    with open("rec-eng.html", "w") as f:
        f.write(html_table)

writer()