import urllib.request
import requests
from bs4 import BeautifulSoup
import instascrape
import os
from selenium.webdriver import Chrome

base_path = "D:\\.shortcut-targets-by-id\\1AaU7tepla52aaPuBkOxwl2g-hq-sHtfP\\S&C Wedding\\S&C Wedding - Choreo"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "cookie": "session_id=407087917%3AlbbGcKlMdmFCTX%3A4%3AAYd-0EEXrv--4hSPUz8Vi7rmf4--uZtGKv7o9Iq2HA"
}
# executable_path="C:/Users/dasco\Downloads/chromedriver-win64/chromedriver.exe"
webdriver = Chrome()

# insta_url = "https://www.instagram.com/p/CDyyMVpi3gp/?igshid=i3pvm7t1uoos"
insta_url = "https://www.instagram.com/p/CnR-iT1DPII/"
insta_filename = "pretty_girls_walk.mp4"
insta_reel_url = "https://www.instagram.com/reel/CnR-iT1DPII/"
profile_name = "iman1013"

# Straight from post
dl_filepath = os.path.join(base_path, insta_filename)
insta_profile = instascrape.Profile(profile_name)
insta_profile.scrape(headers=headers)
# post = instascrape.scrapers.post.Post(insta_url)
posts = insta_profile.get_posts(webdriver=webdriver, login_first=True)
scraped_posts, unscraped_posts = instascrape.scrape_posts(posts, headers=headers, pause=10, silent=False)


billy = 1


# post.download(dl_filepath)

# Profile debug
recent_posts = insta_profile.get_recent_posts()


# Reel scrape
# posts = insta_profile.get_recent_posts()
# google_reel = instascrape.Reel(insta_reel_url)
# google_reel.scrape()

# urllib Requests
page = urllib.request.urlopen(insta_url)
html = page.read()

# Requests
r = requests.get(insta_url)
soup = BeautifulSoup(r.content, 'html5lib')

# file = open("page.html", "w", encoding="utf-8")
# file.write(insta_page.text)
# file.seek(0)  # = open("page.html", "r", encoding="utf-8")

# soup = BeautifulSoup(html, 'html.parser')

colin = 10
video = soup.find("video")

# <video class="tWeCl" playsinline="" poster="https://instagram.fdet1-1.fna.fbcdn.net/v/t51.2885-15/fr/e15/p1080x1080/117469087_811891142884798_1928829667388499519_n.jpg?_nc_ht=instagram.fdet1-1.fna.fbcdn.net&amp;_nc_cat=110&amp;_nc_ohc=UaeXj5QTdkoAX_cn_EX&amp;oh=5fa33393b3db77034ba09cf3da883fd1&amp;oe=5F3D6D50" preload="none" type="video/mp4" src="https://instagram.fdet1-1.fna.fbcdn.net/v/t50.2886-16/117225611_305182027462261_1891872087427818470_n.mp4?_nc_ht=instagram.fdet1-1.fna.fbcdn.net&amp;_nc_cat=101&amp;_nc_ohc=27whVzMgjRwAX_dLLcg&amp;oe=5F3D4CA3&amp;oh=0c362230daadf356a789dc5775deae0d"></video>


