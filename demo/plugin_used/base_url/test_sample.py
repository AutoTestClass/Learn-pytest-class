import urllib.request


def test_example(base_url):
    assert 200 == urllib.request.urlopen(base_url).getcode()
