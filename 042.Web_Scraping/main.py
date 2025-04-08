from bs4 import BeautifulSoup

with open(r"D:\Python Code\Programming-in-Python\042.Web_Scraping\HTML-Personal_Site\index.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
print(heading)