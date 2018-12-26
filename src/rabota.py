import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

base_url = 'https://rabota.ua/jobsearch/vacancy_list?regionId=1&keyWords=Python'

domain = 'https://rabota.ua'
urls = []
jobs = []
urls.append(base_url)

for url in urls:
    time.sleep(2)
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        table = bsObj.find('table', attrs={'id': 'ctl00_content_VacancyListAws_gridList'})
        if table:
            tr_list = bsObj.find_all('tr', attrs={'id': True})
            for tr in tr_list:
                h3 = tr.find('h3', attrs={'class': 'f-vacancylist-vacancytitle'})
                title = h3.a.text
                href = h3.a['href']
                print(domain+href)
                short = "No description"
                company = "Noname"
                p = tr.find('p', attrs={'class': 'f-vacancylist-companyname'})
                if p:
                    company = p.a.text
                desc = tr.find('p', attrs={'class': 'f-vacancylist-shortdescr'})
                if desc:
                    short = desc.text
                jobs.append({'href': domain+href,
                             'title': title,
                             'desc': short,
                             'company': company})

#data = bsObj.prettify()#.encode('utf8')

template = '<!doctype html><html lang="en"><head><meta charset="utf8"></head><body>'
content = '<h2>Rabota.ua</h2>'
end = '</body></html>'

for job in jobs:
    content += '<a href="{href}" target="_blank">{title}</a><br/><p>{desc}</p><p>{company}</p><br/>'.format(**job)
    content += '<hr/><br/><br/>'
data = template + content + end

handle = codecs.open('jobs.html', "w", 'utf8')
handle.write(str(data))
handle.close()
