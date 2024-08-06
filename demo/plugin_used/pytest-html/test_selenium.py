def test_bing(browser):
    browser.get("http://www.bing.com")
    title = browser.title
    assert title == "bing"  # 为了截图，这个断言是失败的
