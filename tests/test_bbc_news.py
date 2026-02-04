import re
import pytest
from playwright.sync_api import Page, expect

def test_bbc_homepage(page):
    #navigate to homepage
    page.goto("https://www.bbc.co.uk/news")

    expect(page).to_have_title(re.compile("BBC News", re.IGNORECASE))

    print('Homepage loaded successfully √')

'''
#code from codegen. delete after compiling tests
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bbc.co.uk/news")
    page.get_by_test_id("navigation").get_by_role("link", name="UK").click()
    page.get_by_test_id("navigation").get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Search BBC").click()
    page.get_by_role("combobox", name="Input your search term").click()
    page.get_by_role("combobox", name="Input your search term").fill("technology")
    page.get_by_role("button", name="Search").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
'''

if __name__ == "__main__":
    import sys
    pytest.main(["-v", "-s", "--headed"])