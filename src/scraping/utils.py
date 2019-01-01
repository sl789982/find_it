import requests
from bs4 import BeautifulSoup as BS
import codecs
import time
import datetime

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


def djinni():
    session = requests.Session()
    base_url = 'https://djinni.co/jobs/?primary_keyword=Python&location=%D0%9A%D0%B8%D0%B5%D0%B2'

    domain = 'https://djinni.co'
    urls = []
    jobs = []
    urls.append(base_url)
    urls.append(base_url + '&page-2')

    for url in urls:
        time.sleep(2)
        req = session.get(url, headers=headers)
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")
            li_list = bsObj.find_all('li', attrs={'class': 'list-jobs__item'})
            for li in li_list:
                div = li.find('div', attrs={'class': 'list-jobs__title'})
                title = div.a.text
                href = div.a['href']
                print(domain + href)
                short = "No description"
                desc = li.find('div', attrs={'class': 'list-jobs__description'})
                if desc:
                    short = desc.p.text
                jobs.append({'href': domain + href,
                             'title': title,
                             'desc': short,
                             'company': "Noname"})
    return jobs


def rabota():
    session = requests.Session()
    base_url = 'https://rabota.ua/jobsearch/vacancy_list?regionId=1&keyWords=python&period=2&lastdate='

    domain = 'https://rabota.ua'
    urls = []
    jobs = []
    yesterday = datetime.date.today() - datetime.timedelta(1)
    one_day_ago = yesterday.strftime('%d.%m.%Y')
    base_url = base_url + one_day_ago
    urls.append(base_url)

    req = session.get(base_url, headers=headers)
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        pagination = bsObj.find('dl', attrs={'id': 'content_vacancyList_gridList_pagerInnerTable'})
        if pagination:
            pages = pagination.find_all('a', attrs={'class': 'f-always-blue'})
            for page in pages:
                urls.append(domain + page['href'])

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
                    print(domain + href)
                    short = "No description"
                    company = "Noname"
                    p = tr.find('p', attrs={'class': 'f-vacancylist-companyname'})
                    if p:
                        company = p.a.text
                    desc = tr.find('p', attrs={'class': 'f-vacancylist-shortdescr'})
                    if desc:
                        short = desc.text
                    jobs.append({'href': domain + href,
                                 'title': title,
                                 'desc': short,
                                 'company': company})
    return jobs


def work():
    session = requests.Session()

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

    for url in urls:
        time.sleep(2)
        req = session.get(url, headers=headers)
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")
            div_list = bsObj.find_all('div', attrs={'class': 'job-link'})
            for div in div_list:
                title = div.find('h2')
                print(div.find('p', attrs={'class': 'overflow'}).text.encode('utf8'))
                href = title.a['href']
                print('work.ua' + href)
                short = div.p.text
                company = "Noname"
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({'href': domain + href,
                             'title': title.text,
                             'desc': short,
                             'company': company})
    return jobs


def dou():
    session = requests.Session()

    base_url = 'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D0%B5%D0%B2&category=Python'

    urls = []
    jobs = []
    urls.append(base_url)

    for url in urls:
        time.sleep(2)
        req = session.get(url, headers=headers)
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")
            div = bsObj.find('div', attrs={'id': 'vacancyListId'})
            if div:
                li_list = bsObj.find_all('li', attrs={'class': 'l-vacancy'})
                for li in li_list:
                    a = li.find('a', attrs={'class': 'vt'})
                    title = a.text
                    href = a['href']
                    print(href)
                    short = "No description"
                    company = "Noname"
                    a_company = li.find('a', attrs={'class': 'company'})
                    if a_company:
                        company = a_company.text
                    desc = li.find('div', attrs={'class': 'sh-info'})
                    if desc:
                        short = desc.text
                    jobs.append({'href': href,
                                 'title': title,
                                 'desc': short,
                                 'company': company})
    return jobs