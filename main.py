from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
website = response.text

soup = BeautifulSoup(website, "html.parser")
article_text = []
article_links = []
article = soup.find_all(name="a", class_="storylink")
for tags in article:
    text = tags.getText()
    article_text.append(text)
    links = tags.get("href")
    article_links.append(links)

article_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_text)
print(article_links)
print(article_score)

maximum = article_score[0]
for x in article_score:
    if x > maximum:
        maximum = x
largest_index = article_score.index(maximum)
# print(largest_index)
print(article_text[largest_index])
print(article_links[largest_index])
print(maximum)
























"""
with open("website.html", encoding="utf8") as file:
    web = file.read()

soup = BeautifulSoup(web, "html.parser")
# print(soup)

all_tags = soup.find_all(name="a")
# print(class_heading)
# for tag in all_tags:
#     print(tag.getText()) #gettin the text in the anchor tags.
#     print(tag.get("href"))


id_heading = soup.find(name="h1", id="name") #getting hold of a particular id
# print(id_heading)

class_heading = soup.find(name="h3", class_="heading")
print(class_heading)
print(class_heading.name)    #o/p = h3
print(class_heading.getText())     #O/P as Books and Teaching
print(class_heading.get("class"))  #O/P as ['heading']

name = soup.select_one(selector="#name")
print(name)

company_url = soup.select_one("p a")
print(company_url)

a = soup.select(".heading")
print(a)
"""


