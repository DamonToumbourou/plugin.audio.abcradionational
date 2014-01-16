from xbmcswift2 import Plugin


plugin = Plugin()

@plugin.route('/')
def main_menu():
    return plugin.redirect(plugin.url_for('show_podcasts', page_no=1))


@plugin.route('/podcasts/<page_no>')
def show_podcasts(page_no):
    url = 'http://www.abc.net.au/radionational/programs/page/{0}?load'.format(page_no)
    next_page = int(page_no) + 1

    items = [{
        'label': "All in the mind",
        'path': plugin.url_for('play_podcast', podcast="http://mpegmedia.abc.net.au/rn/podcast/2014/01/aim_20140105.mp3"),
        'thumbnail': "",
        'is_playable': True,
    }]
    return items
    
@plugin.route('/podcasts/play/<podcast>/')
def play_podcast(podcast):
    url = 'http://mpegmedia.abc.net.au/rn/podcast/2014/01/aim_20140105.mp3'
    plugin.set_resolved_url(url)

if __name__ == '__main__':
    plugin.run()
