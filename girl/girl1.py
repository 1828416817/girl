import requests
import re
import time
url = 'https://www.vmgirls.com/13970.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36',
}
response = requests.get(url, headers=headers)
html = response.text
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
# print(urls)
for url in urls:
    time.sleep(0.5)
    fine_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    with open(fine_name, 'wb')as f:
        f.write(response.content)




