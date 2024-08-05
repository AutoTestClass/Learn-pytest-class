import allure
from pathlib import Path


def test_attach(page):
    page.goto("https://playwright.dev/")
    png_bytes = page.screenshot()
    allure.attach(
        png_bytes,
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )


def test_attach_file(page):
    page.goto("https://playwright.dev/")
    png_bytes = page.screenshot()
    Path("full-page.png").write_bytes(png_bytes)
    allure.attach.file(
        "full-page.png",
        name="full-page",
        attachment_type=allure.attachment_type.PNG
    )
