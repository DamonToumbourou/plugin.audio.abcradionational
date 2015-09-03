from xbmcswift2 import Plugin, xbmcgui
from resources.lib import abcradionational


plugin = Plugin()

URL = "http://abc.net.au/radionational"


@plugin.route('/')
def main_menu():

    items = [
        {'label': plugin.get_string(30000), 'path': "http://www.abc.net.au/res/streaming/audio/aac/news_radio.pls",
            'thumbnail': "http://abc.net.au/res/sites/rn/css/img/rn-icon.png", 'is_playable': True},
        {'label': plugin.get_string(30001), 'path': plugin.url_for('just_in')},
        {'label': plugin.get_string(30002), 'path': plugin.url_for('subject_list')}
    ]

    return items


@plugin.route('/just_in/')
def just_in():

    soup = abcradionational.get_soup(URL + "/podcasts")
    
    playable_podcast = abcradionational.get_playable_podcast(soup)
    
    items = abcradionational.compile_playable_podcast(playable_podcast)


    return items


@plugin.route('/subject_list/')
def subject_list():
   
    soup = abcradionational.get_soup(URL + "/podcasts/subjects")
    
    subject_heading = abcradionational.get_subject_heading(soup)

    items = []
    
    for subject in subject_heading:
        items.append({
            'label': subject['title'],
            'path': plugin.url_for('subject_item', url=subject['url']),
        })

    return items


@plugin.route('/subject_item/<url>/')
def subject_item(url):

    soup = abcradionational.get_soup(url)
    
    playable_podcast = abcradionational.get_playable_podcast(soup)

    items = abcradionational.compile_playable_podcast(playable_podcast)


    return items



if __name__ == '__main__':
    plugin.run()
