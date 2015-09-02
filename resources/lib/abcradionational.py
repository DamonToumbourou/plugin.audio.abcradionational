import requests
import re
from bs4 import BeautifulSoup


def get_soup(url):
    """
    @param: website url to be scraped
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    return soup


def find_subjects(soup):
    """
    @param: html as text 
    """
    subjects = []

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
        
        #needto check that item is not null here
        subjects.append(item) 
    
    return subjects


def list_subjects(subjects):

    items = [{
        'label': subject['title'],
        'thumbnail': subject['thumbnail'],
        'path': subject['url'],
        'info': subject['desc'],
        'is_playable': True,
    } for subject in subjects]

    return items

"""
soup = get_soup("http://abc.net.au/radionational/podcasts")
subjects = find_content(soup)
print list_items(subjects)
"""
#print list_items(find):
