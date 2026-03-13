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

    # Instead of waiting for networkidle, wait for something visible
    page.wait_for_selector('[data-testid="navigation"]', timeout=10000)
    
    # DEBUG: Take a screenshot
    page.screenshot(path="debug-homepage.png")
    print("📸 Screenshot saved")
    
    # ID first link with 'UK'
    uk_link = page.get_by_role("link", name=re.compile("UK", re.IGNORECASE)).first
    
    with page.expect_navigation():
        uk_link.click()

    page.wait_for_load_state("networkidle")

    # Take screenshot after navigation
    page.screenshot(path="debug-after-click.png")

    # Checking we're on the correct page via url
    expect(page).to_have_url(re.compile("/news/uk", re.IGNORECASE))
    
    # Checking for 'UK' heading to verify correct page
    expect(page.get_by_role("heading", name="UK", exact=False).first).to_be_visible()

    print('Navigated to UK Section successfully √')

if __name__ == "__main__":
    pytest.main(["-v", "-s", "--headed"])