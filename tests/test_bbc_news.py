import re
import pytest
import sys
from playwright.sync_api import Page, expect

def test_bbc_homepage(page: Page):
    # Navigate to homepage
    page.goto("https://www.bbc.co.uk/news")

    # Verify page title
    expect(page).to_have_title(re.compile("BBC News", re.IGNORECASE))

    print('Homepage loaded successfully √')

def test_navigation_to_uk_section(page: Page):
    # Starting on homepage
    page.goto("https://www.bbc.co.uk/news")

    page.wait_for_load_state("networkidle")
    
    # Clicking on UK section link
    uk_link = page.get_by_test_id("navigation").get_by_role("link", name="UK")
    uk_link.click()

    page.wait_for_load_state("networkidle")

    # Checking we're on the correct page
    expect(page).to_have_url("https://www.bbc.co.uk/news/uk")
    expect(page.get_by_role("heading", name="UK", exact=False).first).to_be_visible()

    print('Navigated to UK Section successfully √')

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--headed"])