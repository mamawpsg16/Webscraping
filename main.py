from bs4 import BeautifulSoup
import requests
import csv
from collections import deque

def main():
    try:
        # url = 'https://quotes.toscrape.com/'
        url = 'https://myanimelist.net/topanime.php?type=bypopularity'
        response = requests.get(url)

        if response.status_code == 200:
            print("Successfully retrieved the page.")
        else:
            print(f"Error: {response.status_code}")
            exit()  # Exit the script if there is an error
            
        html = BeautifulSoup(response.text, 'html.parser')
        important_details = deque([]) 
        ranks = html.select('td.rank span.top-anime-rank-text')
        titles = html.select('h3.anime_ranking_h3 a')
        details = html.select('div.information')
        scores = html.select('td.score span.score-label')
       
        for detail in details:
            infos = detail.text.strip().split("\n")
            data = f"{infos[0].strip()}, {infos[1].strip()}"
            important_details.append(data)
        
        with open('top50anime.csv','w', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            field = ["rank", "title", "details", "scores"]
            writer.writerow(field)
            for rank, title, detail, scores in zip(ranks, titles, important_details, scores):
                writer.writerow([rank.text, title.text, detail, scores.text])

        # TOSCRAPE WEBSITE:
        # response = requests.get('https://quotes.toscrape.com/')
        # html = BeautifulSoup(response.text, 'html.parser')
        # authors = html.select('small', class_="author")
        # quotes = html.select('span.text')
        
        # with open('profiles1.csv', 'w', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file)
        #     field = ["author", "quote"]
        #     writer.writerow(field)
        #     for author, quote in zip(authors, quotes):
        #         writer.writerow([author.text, quote.text])

    except:
        raise("SHEESH")
    # print(html)

if __name__ == "__main__":
    main()