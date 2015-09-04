from resources.lib import abcradionational


def test_get_podcasts_returns_list():
    podcast = abcradionational.get_playable_podcast("/podcasts")

    assert type(podcast) == list
