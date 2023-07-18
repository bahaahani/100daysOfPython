# import requests
# from bs4 import BeautifulSoup
# requests = requests.get("https://news.ycombinator.com/")
# #print(requests.text)


# soup = BeautifulSoup(requests.text, "html.parser")
# articles = soup.find_all(name="span", class_="titleline")

# # article_tag= soup.find(name="span", class_="titleline")
# # print(article_tag.getText())

# # article_link = article_tag.find(name="a")
# # print(article_link.get("href"))
# # article_upvote = soup.find(name="span", class_="score")
# # print(article_upvote.getText())
# articles_text = []
# articles_link = []

# for article_tag in articles:
#     text = article_tag.getText()
#     articles_text.append(text)
#     link = article_tag.find(name="a")
#     articles_link.append(link.get("href"))
    
    

# # articles_text = [article.getText() for article in articles]
# # articles_link = [articles.get("href") for articles in articles]

# articles_upvote = [int(score.getText().split()[0]) for score in  soup.find_all(name="span", class_="score")]
# largest_number = max(articles_upvote)
# print(articles_text)
# print(articles_link)
# print(articles_upvote)

# print(f"{articles_text[articles_upvote.index(largest_number)]}\n{articles_link[articles_upvote.index(largest_number)]}")

url = "https://www.empireonline.com/movies/features/best-movies-2/"
import requests
from bs4 import BeautifulSoup
response = requests.get(url=url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
 
allmovies= soup.find_all(name="h3", class_="jsx-1913936986")

print(allmovies)