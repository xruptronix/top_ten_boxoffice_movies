from bs4 import BeautifulSoup
import csv
import requests

url = "http://www.imdb.com/chart/boxoffice"

r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")

titles = soup.find_all("td",{"class":"titleColumn"})

with open("boxoffice.csv","w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Movie","Director","Actors"])
    for title in titles:
        movie_name = title.text.strip().encode("utf-8")
        actor_director = title.find("a")["title"].strip().encode("utf-8").split(",")

        director = actor_director[0].split("(")[0]
        actors = ",".join(actor_director[1:])
        print movie_name,director,actors
        writer.writerow([movie_name,director,actors])
