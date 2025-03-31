import requests
import bs4
import pandas as pd
import urllib.request
import urllib.parse
from urllib.parse import urljoin
from urllib.error import HTTPError

### ATTEMPT THREE ###

response = requests.get("https://www.prisonpolicy.org/blog/2020/07/27/disparities/")

soup = bs4.BeautifulSoup(response.text, "html.parser")

images = soup.select('img')

image_links = []
for img in images:
    src = img.get("src")
    if src:
    
        full_url = urljoin(response.url, src)
        image_links.append(full_url)
        print(full_url)

for index, url in enumerate(image_links):
    file_name = 'img_' + str(index) + '.jpg'
    file_path = 'hwimages/'    
    full_path = '{}{}'.format(file_path, file_name)

    try:
        urllib.request.urlretrieve(url, full_path)
        print(f"Downloaded {file_name}")
    except HTTPError as err:
        print(f"HTTPError: {err.code} for {url}")
    except Exception as e:
        print(f"Error: {str(e)}")


### ATTEMPT THREE ###

# response = requests.get("https://gijn.org/stories/10-visualizations-about-criminal-justice/")

# soup = bs4.BeautifulSoup(response.text, "html.parser")

# images = soup.select('img')

# image_links = []
# for img in images:
#     src = img.get("src")
#     if src:
    
#         full_url = urljoin(response.url, src)
#         image_links.append(full_url)
#         print(full_url)

# for index, url in enumerate(image_links):
#     file_name = 'img_' + str(index) + '.jpg'
#     file_path = 'hwimages/'    
#     full_path = '{}{}'.format(file_path, file_name)

#     try:
#         urllib.request.urlretrieve(url, full_path)
#         print(f"Downloaded {file_name}")
#     except HTTPError as err:
#         print(f"HTTPError: {err.code} for {url}")
#     except Exception as e:
#         print(f"Error: {str(e)}")

### ATTEMPT TWO ###

# url = "https://medium.com/swlh/visualizing-the-us-mass-incarceration-problem-699fc1129cf0"

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }

# session = requests.Session()
# session.headers.update(headers)

# response = session.get(url)

# soup = bs4.BeautifulSoup(response.text, "html.parser")

# images = soup.select('img')

# image_links = []
# base_url = "https://medium.com"  # Medium's base URL

# for img in images:
#     src = img.get("src")
#     if src:
#         full_url = urljoin(base_url, src)
#         image_links.append(full_url)


# for index, url in enumerate(image_links):
#     file_name = 'img_' + str(index) + '.jpg'
#     file_path = 'hwimages/'
#     full_path = '{}{}'.format(file_path, file_name)

#     try:
#         urllib.request.urlretrieve(url, full_path)
#         print(f"Downloaded {file_name}")
#     except HTTPError as err:
#         print(f"HTTPError: {err.code} for {url}")
#     except Exception as e:
#         print(f"Error: {str(e)}")

