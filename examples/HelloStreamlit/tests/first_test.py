# import playwright.sync_api import Page, expect
from playwright.sync_api import Page, expect


def test_something(page: Page):
    page.goto("http://localhost:8501/")

    page.wait_for_selector("h2")
    assert page.query_selector("h2").text_content() == "Sup?"

    # assert 1 == 2
    # pass
