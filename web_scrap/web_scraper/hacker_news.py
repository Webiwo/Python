from bs4 import BeautifulSoup
import requests

def scrap_hacker_news():
    try:
        response = requests.get("https://news.ycombinator.com/news")

        content = BeautifulSoup(response.text, "html.parser")
        article_links = []
        article_titles = []
        articles = content.select("span.titleline > a")
        for article in articles:
            article_links.append(article.get("href"))
            article_titles.append(article.getText())

        article_votes = [int(score.getText().split()[0]) for score in content.find_all(name="span", class_="score")]
        max_votes = max(article_votes)
        max_votes_index = article_votes.index(max_votes)
        return article_titles[max_votes_index], article_links[max_votes_index], max_votes

    except Exception as e:
        print(f"❌ Error while downloading data: {e}")
        return None, None, 0
