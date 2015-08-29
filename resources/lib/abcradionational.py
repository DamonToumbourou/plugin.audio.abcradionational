import requests
import re
from bs4 import BeautifulSoup



ABC_URL= "http://abc.net.au/radionational"


def get_podcasts(url_id):
    
    output = []

    # scrape site and return data in array
    url = ABC_URL + url_id
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
        
    for content in soup.find_all('div', class_= "cs-teaser"):
        link = content.find('a', {'class': 'ico ico-download'})
        link = link.get('href')
        
        title = content.find('h3', {'class': 'title'})
        title = title.get_text()

        desc = content.find('div', {'class': 'summary'})
        desc = desc.get_text()

        try:
            thumbnail = content.find('img')
            thumbnail = thumbnail.get('src')
        except AttributeError:
            continue

        item = {
                'url': link,
                'title': title,
                'desc': desc,
                'thumbnail': thumbnail
        }

        output.append(item) 

    return output


def podcasts_get(url):
    """
    returns playable podcasts depending on arg
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    urls = soup.findAll('a', 'ico-download')
    titles = soup.findAll('h3', 'title')
    
    titles_out = []
    for title in titles:
        titles_out.append(re.sub('&#039;', "'", title.text))

    output = []
    for i in range(len(titles_out)):
        try:
            url = urls[i]['href']
            title = titles_out[i]
            output.append({'url': url, 'title': title})
        except IndexError:
            pass

    return output


def get_programs(url_id):
    """
    returns program info from ABC website
    """
    url = ABC_URL + url_id
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    urls = soup.findAll(href=re.compile("/radionational/programs/"))
    programs = []
    for i in range(len(urls)):
        path = urls[i]['href']
        path_final = "http://www.abc.net.au" + path
        title = re.sub('&#039;', "'", urls[i].text)
        programs.append({'url': path_final, 'title': title})
        program_final = programs[40:131]
    
    return program_final


def get_subjects(url_id):
    """
    returns subject info from ABC website
    """
    url = ABC_URL + url_id
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    urls = soup.findAll(href=re.compile("/radionational/subjects/"))
    programs = []

    for i in range(len(urls)):
        path = urls[i]['href']
        path_final = "http://www.abc.net.au" + path
        title = re.sub('&#039;', "'", urls[i].text)
        programs.append({'url': path_final, 'title': title})
        sorted_programs = sorted(programs, key=lambda item: item['title'])
        programs_final = programs[10:30]
    
    return programs_final

