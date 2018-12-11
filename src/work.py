import requests
from bs4 import BeautifulSoup as BS
import codecs

session = requests.Session()
headers = {'User Agent': 'Mozilla/5.0'}

base_url = 'https://www.work.ua/jobs-kyiv-python/'

domain = 'https://www.work.ua'
urls = []
jobs = []
urls.append(base_url)

req = session.get(base_url, headers=headers)
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    pagination = bsObj.find('ul', attrs={'class': 'pagination'})
    if pagination:
        pages = pagination.find_all('li', attrs={'class': False})
        for page in pages:
            urls.append(domain + page.a['href'])

# if req.status_code == 200:
#     bsObj = BS(req.content, "html.parser")
#     div_list = bsObj.find_all('div', attrs={'class': 'job-link'})
#     for div in div_list:
#         title = div.find('h2')
#         print(div.find('p', attrs={'class': 'overflow'}).text.encode('utf8'))
        # href = title.a['href']
        # print('work.ua'+href)
        # short = div.p.text
        # company = "Noname"
        # logo = div.find('img')
        # if logo:
        #     company = logo['alt']
        # jobs.append({'href': domain+href,
        #              'title': title.text,
        #              'desc': short,
        #              'company': company})

#data = bsObj.prettify()#.encode('utf8')


handle = codecs.open('urls.html', "w", 'utf8')
handle.write(str(urls))
#handle.write(str(div.contents))
handle.close()
