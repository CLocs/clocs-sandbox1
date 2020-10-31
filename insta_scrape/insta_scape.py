import requests as req
from bs4 import BeautifulSoup

insta_page = req.get("https://www.instagram.com/p/CDyyMVpi3gp/?igshid=i3pvm7t1uoos")

file = open("page.html", "w", encoding="utf-8")
file.write(insta_page.text)
file.seek(0)  # = open("page.html", "r", encoding="utf-8")
soup = BeautifulSoup(file, 'html.parser')

colin = 10

# <video class="tWeCl" playsinline="" poster="https://instagram.fdet1-1.fna.fbcdn.net/v/t51.2885-15/fr/e15/p1080x1080/117469087_811891142884798_1928829667388499519_n.jpg?_nc_ht=instagram.fdet1-1.fna.fbcdn.net&amp;_nc_cat=110&amp;_nc_ohc=UaeXj5QTdkoAX_cn_EX&amp;oh=5fa33393b3db77034ba09cf3da883fd1&amp;oe=5F3D6D50" preload="none" type="video/mp4" src="https://instagram.fdet1-1.fna.fbcdn.net/v/t50.2886-16/117225611_305182027462261_1891872087427818470_n.mp4?_nc_ht=instagram.fdet1-1.fna.fbcdn.net&amp;_nc_cat=101&amp;_nc_ohc=27whVzMgjRwAX_dLLcg&amp;oe=5F3D4CA3&amp;oh=0c362230daadf356a789dc5775deae0d"></video>


