import urllib.request


def test_example(base_url):
    # https://httpbin.org/get
    print("base URL-->", base_url)
    url = base_url + "/get"
    print("fill URL -->", url)
    assert 200 == urllib.request.urlopen(url).getcode()


def test_my_base_url(my_base_url):
    print("base URL-->", my_base_url)
    url = my_base_url + "/get"
    print("fill URL -->", url)
    assert 200 == urllib.request.urlopen(url).getcode()
