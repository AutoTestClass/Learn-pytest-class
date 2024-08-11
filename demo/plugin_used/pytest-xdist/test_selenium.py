def test_bing(browser):
    browser.get("http://www.bing.com")
    title = browser.title
    assert title == "bing"
