from resources.lib import abcradionational


def test_get_podcasts_returns_list():
    podcasts = abcradionational.get_podcasts("/podcasts")

    assert type(podcasts) == list
