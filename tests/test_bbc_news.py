import re
import pytest
import sys
from playwright.sync_api import Page, expect

def test_bbc_homepage(page: Page):
    #navigate to homepage
    page.goto("https://www.bbc.co.uk/news")

    #verify page title
    expect(page).to_have_title(re.compile("BBC News", re.IGNORECASE))

    print('Homepage loaded successfully √')

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--headed"])