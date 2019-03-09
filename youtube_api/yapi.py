import requests
import json
import random
import string


class Yapi:
    def __init__(self):
        self.api_key = "AIzaSyBjNnc9OF04Y7t9GpqrspGIrquYN79pwpc"

    def get_video(self):
        letters = string.ascii_letters
        r_word = ''.join(random.choice(letters) for i in range(random.randint(3, 6)))
        print(r_word)
        url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + r_word \
              + "&maxResults=1&type=video&key=" + self.api_key
        return requests.get(url=url, stream=True)

    def get_video_id(self):
        try:
            video_id = json.loads(self.get_video().text)['items'][0]['id']['videoId']
        except:
            return self.get_video_id()

        return video_id

