import requests


m3u8_url = 'https://example.com/video.m3u8'
r = requests.get(m3u8_url)
filename = 'raw-video.m3u8'
with open(filename, 'w+') as f:
    f.write(r.text)
    f.close()