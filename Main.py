from bs4 import BeautifulSoup
import requests
import lxml
import time
import random

episode = 1

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

while episode <= 500:
    url = f"https://jut.su/naruuto/season-2/episode-{episode}.html"
    sleep_time = random.randint(1, 5)

    req = requests.get(url=url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    vid_link = soup.find('source')['src']

    video_req = requests.get(url=vid_link, headers=headers)

    with open(f"All_ep's/S2E{episode}.mp4", 'wb+') as file:
        file.write(video_req.content)

    print(f'Серия № {episode} скачана...')
    episode += 1
    time.sleep(sleep_time)
